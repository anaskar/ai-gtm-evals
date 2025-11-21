!pip install openai -q

from getpass import getpass
from openai import OpenAI

# 1️⃣ Enter your Baseten API key securely
api_key = getpass("Enter your Baseten API key: ")

# 2️⃣ Initialize the client for Baseten inference
client = OpenAI(
    api_key=api_key,
    base_url="https://inference.baseten.co/v1"
)

# 3️⃣ Full KPI Diagnostics prompt (same as your markdown)
prompt = """
# 📉 KPI Diagnostics — Contact Sales Form Submissions Down WoW

**Category:** Business / Marketing Analysis  
**Task Type:** KPI Diagnostics  
**Evaluator Goal:** Assess how well the model can reason through a real-world GTM performance issue, generate structured hypotheses, and propose validation actions.

---

## 🧠 Scenario

You’re a senior growth or marketing operator at a B2B SaaS company.  
It’s Monday morning, and the dashboard shows that **“Contact Sales” form submissions on the website are down 25% week-over-week (WoW)**.

This is a classic GTM diagnostic problem — common across nearly every company.  
Your goal is to think like a pragmatic operator and diagnose what’s going on.

---

## 🔍 Prompt

> Contact Sales form submissions are down week-over-week by ~25%.  
> Tell me the breadth of possible reasons, stack rank the most likely, and list 2–3 concrete actions to validate each hypothesis.

---

## 🧱 Instructions for the Model

1. **Topline Understanding**
   - Restate the KPI and clarify assumptions.
   - Identify any missing context that would affect interpretation.

2. **Potential Causes (Breadth)**
   - List as many plausible causes as possible across internal and external reasons.

3. **Stack Rank by Likelihood**
   - Reorder hypotheses from *most* to *least* likely.
   - Explain the rationale behind the ranking.

4. **Validation Plan**
   - For each of the top 5 hypotheses, provide 2–3 *specific checks* you’d perform to confirm or rule it out.
   - Include examples like:
     - “Check CRM lead source mix WoW”
     - “Compare conversion rate by device type”
     - “Inspect tracking events for form submit ID mismatches”

5. **Next Steps**
   - Outline what you’d do in the next 24–48 hours to narrow the issue down.

6. **Output Format**

### Potential Causes
1. ...
2. ...
3. ...

### Ranked Hypotheses
1. ...
2. ...
3. ...

### Validation Plan (Top 5)
| Hypothesis | How to Validate (2–3 checks) |
|---|---|
| H1 | ... |
| H2 | ... |
| H3 | ... |
| H4 | ... |
| H5 | ... |

### Next 24–48 Hours
- ...
- ...
"""

# 4️⃣ Stream using .create(..., stream=True) so chunks have `.choices`
response = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[{"role": "user", "content": prompt}],
    temperature=0.8,
    max_tokens=7500,
    stream=True,
)

full_text = ""

for chunk in response:
    if chunk.choices and chunk.choices[0].delta.content is not None:
        content = chunk.choices[0].delta.content
        print(content, end="", flush=True)
        full_text += content

# 5️⃣ Save to a markdown file for your repo
filename = "kpi_diagnostics_gpt-oss-120b_output.md"
with open(filename, "w") as f:
    f.write(full_text)

print(f"\n\n✅ Saved to {filename}")
