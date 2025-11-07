# 🧩 **AtlasFlow Demand-Gen Take-Home Exercise**

## 🏢 Company Context  
AtlasFlow is a **workflow orchestration platform** used across data engineering, product operations, and customer support. The platform helps teams automate runbooks, coordinate releases, and connect cross-functional tools.  

Roughly **77 %** of customers are SMB, **18 %** mid-market, and **5 %** enterprise.  
Sales-assisted accounts generate **~9.4× higher ARPA** than self-serve.  

To improve CAC payback and expansion efficiency, AtlasFlow wants to:
- Increase the share of **sales-assisted** deals.  
- Grow leads from **mid-market and enterprise** segments.  
- Improve **digital growth and retention** of SMB users to lift NDR and ARPA.  

Each segment requires different motions, but the goal is the same:  
**invest where upside to ARPA / NDR is highest.**

---

## 🧪 **Experimentation**
> What are 3 classic demand-gen initiatives you’d run to get early wins?  
> For each, describe your ingoing hypothesis and how you’d test / measure impact.

---

## 📊 **Analysis**
You’re given a dataset of **Product-Qualified Leads (PQLs)** generated from free workspaces.  

Use:
- `Cleaned_Test_Data_step4_corrected.csv` → actual PQLs (each row = converted workspace)  
- `weekly_ws_created_cohorts_nonlinear.csv` → all weekly free workspace sign-ups, including non-converting workspaces  

**Answer:**
1. What trends do you see in the data?  
2. What stands out or feels unique based on your experience?  
3. Using these datasets, build or describe a **forward-looking forecast** for PQLs based on free workspace sign-ups.  
   - *(Hint: cohort by `ws_created_at` and model lag from WS → PQL to forecast future conversion.)*

---

## 🚀 **Strategy & Execution**
- Many mid-market / enterprise PQLs lack buyer personas among active users.  
  → What channels or methods would you use to reach true buyers? (3 examples)  
- Which **KPIs / unit economics** would you track to evaluate channel success?  
- Would you pursue any “moonshots”?  
- What **tooling** or programmatic engines would you need to operationalize these efforts?

---

## 📁 **Files**

| File | Description | Download |
|------|--------------|-----------|
| `dg_test_data_1.csv` | Historical PQL dataset (9 ,770 rows). Includes `customer_id`, `ws_created_at`, `pql_created_at`, `company_segment`, `company_sales_region`, `company_employees`. | [📥 Download](https://github.com/anaskar/ai-gtm-evals/blob/a98d677faddb06d228bb41af4f73e7c33120db55/campaign_analysis/data/dg_test_data_1.csv) |
| `weekly_ws_created_cohorts_nonlinear.csv` | Weekly workspace-creation cohorts with improving free → PQL conversion (≈ 4.7 → 6.4 %). Columns: `week_created`, `workspaces_created_that_week`, `applied_conversion_rate`. | [📥 Download](sandbox:/mnt/data/weekly_ws_created_cohorts_nonlinear.csv) |

---

You can copy this block directly into your doc or notebook — it contains the **entire prompt + both CSVs** needed to complete and reproduce the exercise.
