## 📊 Topline Understanding

**KPI:** “Contact Sales” form submissions are down **25 % week‑over‑week (WoW)**.  
**Assumptions:**  
- The 25 % drop is a direct comparison of the same 7‑day period (e.g., last Monday‑Sunday vs. the previous Monday‑Sunday).  
- “Contact Sales” is a single‑step form (or a modal) on the website whose submissions are tracked via a client‑side event (e.g., `form_submit`) and pushed to analytics and the CRM.  
- No known data‑pipeline delays or reporting outages have been announced.  

**Missing Context Needed for Deeper Diagnosis**  
- Baseline volume (e.g., 100 vs. 75 submissions).  
- Exact calendar weeks (holiday week? end of quarter?).  
- Any recent website or marketing deployments (code, GTM, campaigns).  
- Traffic mix (% paid, organic, direct) and typical conversion rates by source.  
- Whether the drop is uniform across devices, geos, or personas.  

---

## 🌍 Potential Causes (Breadth)

### **Internal – Technical & Product**
1. Form submission endpoint returning 4xx/5xx errors or timing out.  
2. JavaScript error on the page that blocks the submit handler (e.g., `null` reference, CORS issue).  
3. GTM tag for `form_submit` misconfigured, removed, or misfiring.  
4. Cookie‑consent banner now suppresses tracking until explicit opt‑in (e.g., new CMP implementation).  
5. CDN or server outage affecting the form handler (e.g., Cloudflare worker error).  
6. New code deployment introduced a bug (e.g., validation rule, field ID mismatch).  
7. Third‑party script conflict (e.g., new chat widget, A/B test snippet) hijacking the submit event.  
8. Page‑load performance degradation (LCP, FID regression) causing users to abandon before the form renders.  

### **Internal – Marketing & Traffic**
9. Paid search or social campaign paused, budget reduced, or bid strategy changed.  
10. Ad creative or landing page URL updated, breaking the expected flow.  
11. Organic ranking drop due to a Google algorithm update or SERP feature change.  
12. Referral traffic from a key partner dropped (e.g., they removed a backlink).  
13. Email nurture campaign that drove high‑intent visitors ended.  
14. A/B test on the Contact Sales page inadvertently hurts conversion (e.g., new copy, layout).  
15. Increased form friction: new required fields, stricter validation, CAPTCHA added.  

### **Internal – Data & Reporting**
16. Analytics tracking pixel removed or mis‑installed (e.g., GA4 config tag).  
17. Data pipeline / ETL job failing to process raw events into the dashboard.  
18. CRM sync issue (e.g., API quota, authentication failure) causing leads to be dropped.  
19. Internal dashboard bug or caching issue showing stale/incorrect numbers.  

### **External – Seasonal & Market**
20. Holiday week (e.g., 4th of July, Labor Day) or local vacation period reducing B2B activity.  
21. Industry event (e.g., major conference, competitor product launch) distracting target audience.  
22. Economic shift (e.g., budget freeze, recession fears) reducing inbound interest.  
23. Regulatory change (e.g., new privacy law) prompting stricter consent behaviors.  
24. Unforeseen news event (e.g., natural disaster, geopolitical tension) affecting business operations.  

---

## 🎯 Ranked Hypotheses (Most → Least Likely)

| Rank | Hypothesis | Rationale |
|------|------------|-----------|
| **1** | **Tracking or Data Issue** | Sudden 25 % drops are most often caused by mis‑firing tags, GTM changes, or cookie‑consent updates that prevent events from being recorded. Easy to verify and cheap to fix. |
| **2** | **Website Form or Technical Regression** | A broken form endpoint, JavaScript error, or recent deploy can instantly halt submissions. Usually appears as a sharp step‑function drop. |
| **3** | **Paid Campaign or Budget Changes** | Pausing or slashing budget on high‑intent paid channels (e.g., branded search, LinkedIn) can produce an immediate, large decline in qualified traffic. |
| **4** | **Traffic Volume/Quality Drop** | If total sessions are down or the mix shifts to lower‑intent sources (e.g., more organic blog traffic vs. direct), the raw number of form fills will fall even if the form itself is unchanged. |
| **5** | **Seasonality or External Event** | A holiday, industry conference, or competitor announcement can temporarily depress demand; this is more plausible if the drop aligns with known calendar events. |
| 6 | **A/B Test or UX Change** | A new test variant may reduce conversion, but the effect is usually gradual; a 25 % drop suggests a more systemic issue. |
| 7 | **Increased Form Friction** | Adding fields or validation typically shows a smaller, incremental decline rather than a steep 25 % fall. |

---

## 🔍 Validation Plan (Top 5 Hypotheses)

| Hypothesis | How to Validate (2–3 concrete checks) |
|------------|--------------------------------------|
| **H1: Tracking or Data Issue** | 1. **GTM Preview Mode** – open the site in GTM preview, submit the form, and verify the `form_submit` trigger fires and sends the event to GA4/Segment.<br>2. **Server‑vs‑Analytics Count** – pull raw access logs for the form endpoint (e.g., `POST /api/contact‑sales`) and compare the count of 2xx responses to the number of events recorded in analytics for the same period.<br>3. **Cookie Consent Audit** – check if the consent banner logic changed (e.g., new CMP version) and whether it now blocks analytics until explicit opt‑in, then segment submissions by consent status. |
| **H2: Website Form or Technical Regression** | 1. **Manual End‑to‑End Test** – submit the form on desktop, mobile, and incognito; watch the network tab for a successful 2xx response and check for console errors.<br>2. **Recent Deploy Log** – review the last 7 days of code commits and deployments to the Contact Sales page or API; look for changes to form fields, validation, or the submit handler.<br>3. **Error Rate Monitoring** – check APM/RUM tools (e.g., New Relic, Sentry) for a spike in JavaScript errors or form‑endpoint failures around the time the drop began. |
| **H3: Paid Campaign or Budget Changes** | 1. **Ad Platform Spend & Status** – log into Google Ads, LinkedIn, Facebook, etc., and compare daily spend, impressions, and campaign status WoW; note any paused or budget‑limited campaigns.<br>2. **Traffic Source Report** – in GA4, view the “Traffic Acquisition” report and isolate paid channels; check if sessions and conversion rate (Contact Sales) fell in lockstep.<br>3. **Impression Share & CTR** – for search campaigns, verify if impression share dropped due to budget or rank, and if CTR remained stable (ruling out creative fatigue). |
| **H4: Traffic Volume/Quality Drop** | 1. **Sessions & Users WoW** – pull GA4’s “Overview” report and compare total sessions, users, and new users for the two weeks; a 25 % drop in form submissions often mirrors a similar drop in sessions.<br>2. **Source/Medium Breakdown** – segment by `session source / medium` and identify which high‑intent sources (direct, organic branded, paid) declined the most.<br>3. **Engagement Quality Metrics** – check bounce rate, average session duration, and pages per session for each source; a rise in bounce rate suggests lower‑quality traffic. |
| **H5: Seasonality or External Event** | 1. **Calendar Check** – confirm if the week includes a public holiday, industry‑wide conference, or typical summer slowdown for your ICP.<br>2. **Google Trends & News** – search your brand name and core keywords on Google Trends; look for news about competitor launches, regulatory changes, or market shocks.<br>3. **Peer Benchmarking** – ask sales or CS teams if they’ve heard similar feedback from prospects (e.g., “budget freeze” or “waiting on Q1 planning”). |

---

## ⚡ Next 24–48 Hours

- **Hour 0–2:** **Confirm data integrity** – run GTM preview, check analytics real‑time view, and pull raw server logs to rule out a tracking or pipeline bug.  
- **Hour 2–6:** **Audit recent changes** – review last week’s deployment logs, GTM container versions, and any marketing campaign status (paid, email, referral).  
- **Hour 6–12:** **Manual form testing** – submit the form on multiple devices/networks; if it fails, escalate to engineering immediately.  
- **Hour 12–24:** **Segment the data** – break down submissions by source, device, geo, and persona to isolate the drop’s footprint.  
- **Hour 24–48:** **Hold a cross‑functional war room** – share findings with Marketing, Engineering, Sales, and Product; decide whether to roll back any recent changes, adjust campaign budgets, or implement a monitoring alert for the form conversion rate.  

*If the root cause remains unclear after these steps, expand the investigation to include deeper funnel analysis (e.g., MQL‑to‑SQL conversion) and consider a brief survey of recent non‑submitters to uncover friction points.*

