# =========================
# Colab: Batched LLM Lead Scoring
# =========================

!pip -q install openai pandas tenacity

import os
import json
import math
import pandas as pd
from typing import Dict, Any, List
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type
from openai import OpenAI
import getpass
from google.colab import files

# -------------------------
# 1) Config
# -------------------------
INPUT_PATH = "/content/synthetic_inbound_leads.csv"
OUTPUT_PATH = "/content/scored_leads.csv"
MODEL_NAME = "moonshotai/Kimi-K2.5"

BATCH_SIZE = 10          # increase to 20–25 if responses remain well-formed
TEMPERATURE = 0.2        # keep low for consistent JSON formatting
MAX_TOKENS = 1200        # increase if you bump batch size

REQUIRED_COLS = [
    "company_name",
    "company_size",
    "domain",
    "industry",
    "job_title",
    "seniority",
    "inbound_message",
    "source",
]

# -------------------------
# 2) API key
# -------------------------
if not os.getenv("BASETEN_API_KEY"):
    os.environ["BASETEN_API_KEY"] = getpass.getpass("Enter your BASETEN_API_KEY: ")

client = OpenAI(
    api_key=os.environ["BASETEN_API_KEY"],
    base_url="https://inference.baseten.co/v1",
)

# -------------------------
# 3) Load CSV
# -------------------------
df = pd.read_csv(INPUT_PATH)

missing = [c for c in REQUIRED_COLS if c not in df.columns]
if missing:
    raise ValueError(f"Missing required columns: {missing}")

# -------------------------
# 4) Prompt
# -------------------------
SCORING_PROMPT = """
You are a senior data analyst and inbound SDR responsible for qualifying inbound leads for a B2B SaaS company.

You will receive a JSON array of inbound leads. For EACH lead, you must return a corresponding JSON object with:
- lead_score: number 0 to 100
- lead_label: "high" | "medium" | "low"
- justification: 1–2 sentences

Scoring criteria:
- Company size and likelihood of budget
- Role seniority / decision-making authority
- Commercial intent (evaluation, pricing, timelines, production)
- Relevance to production/commercial use
- Urgency / buying signals
- Source credibility (referral > email/blog/paid_social > unknown)

Definitions:
HIGH:
- Usually 50+ employees (often 100+)
- Clear commercial or production intent
- Mentions scaling, reliability, security, pricing, timelines, evaluation
- Director/VP/C-level/founder or strong influencer
- Likely budget / near-term buying window

MEDIUM:
- Relevant but unclear urgency/budget
- Smaller co or non-final decision-maker
- Exploratory intent
- Could convert with nurturing

LOW:
- Student/hobbyist/personal/non-commercial
- Very small, no budget signals
- Vague/generic
- Mentions coursework/learning/personal project/“just curious”

Edge cases:
- Agencies/consultants => medium unless clear resale at scale
- Nonprofits/research => low/medium unless enterprise deployment stated
- If ambiguous, score conservatively

OUTPUT FORMAT (STRICT):
Return JSON ONLY: a JSON array the SAME LENGTH as the input array, in the SAME ORDER.
Each element must contain ONLY: lead_score, lead_label, justification.
No markdown, no extra text.
""".strip()

# -------------------------
# 5) Helpers
# -------------------------
class LLMResponseError(Exception):
    pass

def _extract_json_any(text: str) -> Any:
    text = (text or "").strip()
    # direct parse
    try:
        return json.loads(text)
    except Exception:
        pass
    # salvage JSON array or object
    start = min([i for i in [text.find("["), text.find("{")] if i != -1], default=-1)
    end_bracket = text.rfind("]")
    end_brace = text.rfind("}")
    end = max(end_bracket, end_brace)
    if start != -1 and end != -1 and end > start:
        snippet = text[start:end+1]
        try:
            return json.loads(snippet)
        except Exception:
            pass
    raise LLMResponseError(f"Could not parse JSON. Response head: {text[:200]}")

def _validate_item(obj: Dict[str, Any]) -> Dict[str, Any]:
    for k in ("lead_score", "lead_label", "justification"):
        if k not in obj:
            raise LLMResponseError(f"Missing '{k}' in item: {obj}")

    try:
        score = float(obj["lead_score"])
    except Exception:
        raise LLMResponseError(f"lead_score not numeric: {obj.get('lead_score')}")

    score = max(0.0, min(100.0, score))
    label = str(obj["lead_label"]).lower().strip()
    if label not in {"high", "medium", "low"}:
        raise LLMResponseError(f"Invalid lead_label: {label}")

    justification = str(obj["justification"]).strip() or "No justification provided."
    return {"lead_score": score, "lead_label": label, "justification": justification}

@retry(
    reraise=True,
    stop=stop_after_attempt(4),
    wait=wait_exponential(multiplier=1, min=2, max=20),
    retry=retry_if_exception_type((LLMResponseError, TimeoutError)),
)
def score_batch(leads: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    # keep payload compact
    payload = [{k: lead.get(k) for k in REQUIRED_COLS} for lead in leads]

    resp = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": SCORING_PROMPT + "\n\nLeads:\n" + json.dumps(payload, ensure_ascii=False)}],
        stream=False,
        top_p=1,
        max_tokens=MAX_TOKENS,
        temperature=TEMPERATURE,
        presence_penalty=0,
        frequency_penalty=0,
    )

    text = resp.choices[0].message.content
    parsed = _extract_json_any(text)

    if not isinstance(parsed, list):
        raise LLMResponseError(f"Expected a JSON array, got: {type(parsed)}")

    if len(parsed) != len(leads):
        raise LLMResponseError(f"Expected {len(leads)} items, got {len(parsed)}")

    return [_validate_item(item) for item in parsed]

# -------------------------
# 6) Run scoring in batches
# -------------------------
n = len(df)
all_results: List[Dict[str, Any]] = []
errors = 0

num_batches = math.ceil(n / BATCH_SIZE)
print(f"Scoring {n} leads in {num_batches} batches (batch_size={BATCH_SIZE})")

for b in range(num_batches):
    start = b * BATCH_SIZE
    end = min((b + 1) * BATCH_SIZE, n)
    batch_df = df.iloc[start:end]
    batch_leads = [row._asdict() if hasattr(row, "_asdict") else row.to_dict() for _, row in batch_df.iterrows()]

    try:
        batch_scores = score_batch(batch_leads)
        all_results.extend(batch_scores)
        print(f"✅ Batch {b+1}/{num_batches} scored ({end-start} leads)")
    except Exception as e:
        # fallback: mark batch as errored but keep alignment
        errors += (end - start)
        print(f"❌ Batch {b+1}/{num_batches} failed: {e}")
        all_results.extend([{"lead_score": None, "lead_label": None, "justification": f"ERROR: {e}"} for _ in range(end-start)])

# Ensure alignment
assert len(all_results) == n, (len(all_results), n)

scored_df = pd.concat([df.reset_index(drop=True), pd.DataFrame(all_results)], axis=1)
print(f"Done. Total errors: {errors}")

# -------------------------
# 7) Save + download
# -------------------------
scored_df.to_csv(OUTPUT_PATH, index=False)
print("Wrote:", OUTPUT_PATH)
files.download(OUTPUT_PATH)
