# 🧠 AI Marketing Model Evaluations

This project compares large-language-model (LLM) performance on **marketing and go-to-market (GTM)** tasks — things like campaign ideation, product positioning, and business reasoning.  
The goal is to understand how different models perform on *real-world marketing workflows*, not synthetic benchmarks.

---

## 🎯 What We’re Doing

We run structured evaluations of leading AI models, both closed and open source, on marketing-relevant use cases.  
Each model is given identical prompts across a consistent taxonomy of GTM tasks.  
The goal: to see how well each model handles **strategic reasoning, marketing creativity, and execution-quality writing**.

All tests are run **via the models’ chat interfaces**, not APIs — to mirror how real marketers actually use these tools.
Though, we'll also be running evals in the future that are more suited for API use. 

---

## 🧩 Taxonomy of Marketing Tasks

The evaluation is organized around three key GTM categories.  
Each category contains specific scenarios (in Markdown or CSV format) that reflect everyday marketing work.

### 1️⃣ Product Marketing & Positioning  
*How well can the model synthesize differentiators, messaging, and positioning?*  
Example tasks:
- Write positioning statements and messaging pillars  
- Compare products or competitors  
- Generate headlines and subheads for a landing page  

---

### 2️⃣ Demand Generation & Campaign Ideation  
*Can the model design actionable campaigns that a marketer could actually run?*  
Example tasks:
- Draft a 30-day conversion program  
- Propose a channel mix and budget allocation  
- Define KPIs, risks, and mitigation plans  

---

### 3️⃣ Business Analysis & Marketing Logic  
*Can the model reason through performance metrics like a growth operator?*  
Example tasks:
- Interpret CAC/LTV or pipeline data  
- Diagnose conversion drops  
- Recommend data-backed next steps  

Each category measures different dimensions of “marketing intelligence,” from strategic clarity to tactical creativity.

---

## ⚙️ How We Run Evaluations

All evaluations are performed **manually via chat UIs** for each model:

- **OpenAI ChatGPT** 
- **Anthropic Claude** 
- **Google Gemini**  
- **Open Source** (Kimi-K2, GTP-OSS, etc.)

### Workflow
1. Open the chat interface for the model being tested  
2. Paste the same prompt from `/tasks`  
3. Record the model’s response in Markdown or CSV  
4. Score it manually across the five evaluation criteria  
5. Note qualitative observations (tone, hallucinations, logic gaps)

The goal is to simulate *actual marketer usage* — no fine-tuning, no temperature hacks, just out-of-the-box reasoning.

---

## 🧾 Evaluation Criteria

Each model’s output is rated **1–5** on five key dimensions:

| Criterion | Description |
|------------|--------------|
| **Accuracy / Validity** | Is it factually grounded and logically correct? |
| **Structure / Clarity** | Does it communicate clearly and follow a coherent structure? |
| **Creativity / Specificity** | Does it go beyond generic ideas and show original thought? |
| **Business Realism** | Would a PMM, marketer, or founder find this plausible and useful? |
| **Utility / Actionability** | Can you directly use or lightly edit the output for production? |

Each task produces a mix of **quantitative scores** and **qualitative insights** — which together form the model’s overall “GTM IQ” for marketing work.

---

## 📈 Output & Results

- **Raw outputs:** stored in `/data` (Markdown or CSV)  
- **Scored evaluations:** summarized in `/results`  
- **Commentary & takeaways:** published as brief reports or posts  

Example insights:
> “Claude 4.5 Sonnet nails messaging nuance but struggles with numeric reasoning.”  
> “GPT-4o-mini provides concise, usable campaign plans ideal for fast-moving PMMs.”  

Over time, this will evolve into a public leaderboard of models for marketing and GTM workflows.

---

## 🧭 Contributing

Want to contribute new marketing tasks or help evaluate outputs?

- Add a new Markdown file under `/tasks` with your prompt and sample data  
- Log your model outputs in `/data`  
- Score using the 1–5 rubric and add to `/results`  
- Open a pull request with your addition or analysis

---

## 📜 License

MIT License — free to use, remix, and reference.

---

*Maintained by [Arjun Naskar / @anaskar]*  
*Exploring how modern AI models reason, write, and strategize like marketers.*
