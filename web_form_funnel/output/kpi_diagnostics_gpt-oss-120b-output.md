**1️⃣ Top‑line understanding**

- **KPI:** Number of “Contact Sales” form submissions on the public website.  
- **Observed change:** ‑25 % week‑over‑week (WoW).  
- **Assumptions** (that we need to confirm):  
  - The form is the primary inbound‑sales lead capture point (not duplicated elsewhere).  
  - Tracking (Google Analytics / Mixpanel / Snowplow) and CRM ingestion have been stable – no recent changes to the “lead‑to‑CRM” pipeline.  
  - The comparison week is a “typical” week (no known holidays, product launches, or major events).  
- **Missing context that would affect interpretation:**  
  - Overall website traffic change (sessions, unique visitors).  
  - Traffic source mix (organic, paid, referral, direct).  
  - Any recent site or product updates (copy, UI, A/B tests).  
  - Changes to ad spend, campaign targeting, or audience segments.  
  - Seasonality / regional holidays that could suppress demand.  
  - Lead‑routing or CRM validation changes that could reject submissions.  

---

## 2️⃣ Potential Causes (Breadth)

| # | Category | Hypothesis |
|---|----------|------------|
| 1 | **External – Traffic volume** | Overall site sessions dropped (e.g., SEO ranking loss, referral link removed). |
| 2 | **External – Traffic quality** | Shift from high‑intent sources (paid search, referral) to low‑intent sources (social, direct). |
| 3 | **External – Seasonality / holidays** | Target market is on vacation / fiscal year‑end, reducing buying intent. |
| 4 | **External – Competitive actions** | Competitor launched a promotion or new feature pulling leads away. |
| 5 | **External – Paid‑media changes** | Decrease in ad spend, budget reallocation, or bid changes lowered impressions/click‑through. |
| 6 | **External – Search‑engine algorithm update** | SEO drop caused by Google core update affecting landing‑page rankings. |
| 7 | **Internal – Site bug / tracking break** | JavaScript error, form validation failure, or broken “submit” event preventing actual submissions. |
| 8 | **Internal – UI/UX change** | Recent redesign made the form less visible, added extra fields, or changed CTA copy. |
| 9 | **Internal – Copy / messaging shift** | Headline or value‑prop change reduced perceived relevance. |
|10 | **Internal – A/B test** | Ongoing experiment (e.g., different form layout) is under‑performing. |
|11 | **Internal – Funnel friction** | New captcha, reCAPTCHA, or required login step increased friction. |
|12 | **Internal – Lead routing / deduplication** | CRM now deduplicates or rejects leads that previously would have been accepted. |
|13 | **Internal – Data‑layer / analytics mis‑alignment** | Event name changed, causing under‑count in dashboards while actual submissions are unchanged. |
|14 | **Internal – Load‑time / performance** | Page load time slowed, especially on mobile, causing drop‑off before reaching the form. |
|15 | **Internal – Bot / spam filter** | New anti‑spam filter mistakenly blocks legitimate submissions. |
|16 | **Internal – Personalization / geo‑targeting** | New personalization logic hides the form for certain regions or visitor segments. |
|17 | **Internal – Email / outreach mis‑alignment** | Sales outreach emails now link to a different landing page that lacks the form. |
|18 | **Internal – Pricing / product change** | Recent price increase or packaging change lowered buying intent. |
|19 | **Internal – Operational change** | Sales team stopped responding promptly, leading to lower conversion on follow‑up (if measured as “submitted & qualified”). |
|20 | **External – Economic factors** | Macro‑level slowdown (e.g., budget cuts) affecting target market. |

---

## 3️⃣ Ranked Hypotheses (Most to Least Likely)

| Rank | Hypothesis | Why it’s likely first |
|------|------------|-----------------------|
| **1** | **Traffic volume dropped** | A 25 % drop in form submissions often mirrors a similar drop in overall sessions. It’s the simplest, most data‑driven explanation. |
| **2** | **Paid‑media spend or targeting change** | Many B2B SaaS firms rely heavily on paid search/LinkedIn ads for high‑intent leads; a modest budget tweak can instantly bite the form volume. |
| **3** | **Site bug / broken form submission** | A JavaScript error or broken endpoint can silently stop submissions while traffic stays flat. Operators frequently see “invisible” bugs. |
| **4** | **Recent UI/UX or copy change** | Even small visual tweaks (e.g., moving the CTA lower) can reduce click‑through dramatically, especially when the form is near the fold. |
| **5** | **Shift in traffic quality (source mix)** | If high‑intent channels (organic search, referral) fell and low‑intent (social, direct) rose, conversion would drop even with stable overall traffic. |
| **6** | **Seasonality / market holiday** | Week‑over‑week can be noisy; a regional holiday could explain a dip but usually shows a pattern over multiple weeks. |
| **7** | **A/B test under‑performing** | Ongoing experiments sometimes under‑deliver; however, most teams monitor test‑level metrics before full rollout. |
| **8** | **SEO ranking loss / algorithm update** | SEO changes affect organic traffic more gradually; a sudden 25 % dip is possible but less common week‑to‑week. |
| **9** | **Lead routing / deduplication change** | CRM‑side filters can reduce recorded leads, but they usually affect downstream metrics, not the front‑end “submission” count (unless the form UI shows an error). |
| **10**| **Performance / load‑time degradation** | Slower page loads, especially on mobile, can increase bounce before the form is reached. |

(Items 11‑20 are retained for completeness but are considered lower probability given the limited information.)

---

## 4️⃣ Validation Plan (Top 5 Hypotheses)

| Hypothesis | How to Validate (2–3 concrete checks) |
|------------|----------------------------------------|
| **H1 – Traffic volume dropped** | 1. Pull sessions/unique visitors for the same page (or site‑wide) WoW from GA/Amplitude. <br>2. Compare total page‑views of the “Contact Sales” landing page WoW. <br>3. Segment by device & geography – see if the drop is uniform or localized. |
| **H2 – Paid‑media spend or targeting change** | 1. Export paid‑search / LinkedIn campaign spend, impressions, clicks WoW. <br>2. Check CPL (cost‑per‑lead) and click‑through‑rate trends; a dip in clicks should line up with form drop. <br>3. Verify any recent audience or keyword list changes in the ad platform that could have narrowed the reach. |
| **H3 – Site bug / broken form submission** | 1. Open the form in a staging environment and fire a test submission; watch the network tab for 4xx/5xx responses. <br>2. Review error logs (server‑side endpoint, Cloudflare, Sentry) for spikes in “form submit” errors WoW. <br>3. Check the analytics event that records “form_submit” – ensure the event fires for a test submission (real‑time view). |
| **H4 – Recent UI/UX or copy change** | 1. Review the CMS / git commit history for any changes to the form page in the last 2‑3 weeks. <br>2. Use heat‑map / session‑replay tools (Hotjar, FullStory) to compare click‑through rates on the CTA button before vs. after the change. <br>3. Run an instant A/B test (original vs. current) on a small traffic slice to measure conversion difference. |
| **H5 – Shift in traffic quality (source mix)** | 1. Break down sessions by source/medium (organic, paid, direct, referral, social) WoW. <br>2. Compute conversion rate (form submissions ÷ sessions) per source – identify any source where rate fell dramatically. <br>3. Look at new vs. returning visitor ratios; a surge of low‑intent new visitors can dilute conversion. |

---

## 5️⃣ Next 24‑48 Hours – Action Plan

1. **Pull the data dashboard**  
   - Export overall sessions, source/medium breakdown, and page‑view counts for the “Contact Sales” page for the past 4 weeks.  
   - Overlay the form‑submission trend to see if the dip aligns with traffic changes.

2. **Run a quick health check on the form**  
   - In a private/incognito window, submit the form using a test email. Capture the network request and confirm a 200/302 response and that the CRM record appears.  
   - Scan error‑monitoring logs for any spikes in “form submit” errors (Sentry, New Relic) for the same period.

3. **Audit paid‑media and SEO**  
   - Pull ad spend, impressions, clicks, and CPL for the last two weeks from Google Ads / LinkedIn Campaign Manager.  
   - Check Google Search Console for any sudden drop in impressions/CTR for the target keywords.

4. **Review recent product/website changes**  
   - Ask the engineering / product team for any deployments affecting the contact page (feature flags, copy updates, new captcha, etc.).  
   - If a change is identified, roll it back on a staging environment or create a hot‑fix to test impact.

5. **Set up an immediate A/B test (if needed)**  
   - If the UI/UX change is suspected but not confirmed, duplicate the current form page, revert to the previous version, and split traffic 50/50 using a feature flag. Monitor conversions for 24‑48 h.

6. **Communicate with the sales ops team**  
   - Verify that the CRM is still ingesting leads from the web form and that no new validation rules were added that could silently discard records.

**Outcome expected:** By the end of the 48‑hour window we should know whether the drop is traffic‑driven, a technical blockage, or a UX issue, allowing us to prioritize a fix (budget rebalance, bug patch, or quick UI rollback) before the trend compounds.