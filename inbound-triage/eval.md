# Synthetic Inbound Lead Scoring Dataset

## Overview

This project creates a synthetic dataset of inbound B2B leads and uses it to develop and evaluate a lead quality scoring system.

The goal is to simulate realistic inbound traffic (ranging from highly qualified buyers to low-intent or non-commercial inquiries), score those leads consistently, and use the resulting data to train or evaluate a lead scoring model.

This dataset is intentionally synthetic so that:
- It can be generated and iterated on quickly
- It avoids using real customer or prospect data
- It allows controlled variation in lead quality and intent

---

## Dataset Description

Each row in the dataset represents a single inbound lead.

### Schema

| Field | Description |
|------|------------|
| company_name | Name of the company or organization |
| company_size | Approximate employee count |
| domain | Company website or domain |
| industry | Industry the company operates in |
| job_title | Title of the person submitting the inbound request |
| seniority | Seniority level (entry, manager, senior, director, vp, c-suite/founder) |
| inbound_message | Free-text inbound message describing interest or use case |
| source | Inbound source (paid_social, blog, referral, email, unknown) |

The dataset intentionally includes:
- Enterprise, mid-market, startup, and individual leads
- Decision-makers and non-decision-makers
- Clear buyers, exploratory leads, and non-commercial inquiries

---

## Objective

The primary objective is to assign a **lead quality score** to each inbound lead that reflects its likelihood of converting into a meaningful sales opportunity.

This score can be used to:
- Prioritize inbound follow-up
- Route leads to sales vs nurture flows
- Train or evaluate automated lead scoring models
- Benchmark heuristic vs LLM-based scoring approaches

---

## Lead Scoring Task

For each inbound lead, the system assigns:

- **lead_score**: A numeric score from 0–100
- **lead_label**: A categorical label (`high`, `medium`, `low`)
- **justification**: A short explanation for the score

Scoring is based on signals such as:
- Company size and expected budget
- Seniority and decision-making authority
- Evidence of commercial or production intent
- Urgency, timelines, or evaluation language
- Relevance to a real production use case
- Credibility of inbound source

---

## Lead Quality Definitions

### High-Quality Leads
- Typically companies with 50+ employees (often 100+)
- Clear commercial or production intent
- Mentions scaling, reliability, security, pricing, timelines, or vendor evaluation
- Submitted by decision-makers or strong influencers (director, VP, head, CTO, founder)
- Likely to have budget and near-term buying intent

### Medium-Quality Leads
- Relevant use case but unclear urgency or budget
- Smaller companies or roles without final decision authority
- Exploratory or educational intent rather than active buying
- Could convert with education or nurturing

### Low-Quality Leads
- Individuals, students, hobbyists, or non-commercial usage
- Very small companies with no clear budget
- Vague or generic messages with no buying signals
- Mentions coursework, learning, or personal projects

### Edge Cases
- Agencies and consultants default to medium unless there is clear resale or multi-client scale intent
- Nonprofits and research labs default to low or medium unless enterprise deployment is stated
- When signals are ambiguous, scoring should be conservative

---

## Intended Use

This dataset and scoring framework can be used for:
- Training supervised lead scoring models
- Evaluating LLM-based classifiers
- Comparing heuristic vs learned scoring approaches
- Simulating inbound sales workflows

Because the data is synthetic, it should be treated as a proxy for real inbound behavior, not a replacement for production data.

---

## Future Extensions

Potential next steps include:
- Expanding the dataset size and diversity
- Introducing explicit noise or mislabeling
- Adding firmographic enrichment fields
- Comparing multiple scoring prompts or models
- Calibrating scores against real conversion data

---
Model: Kimi K2.5
