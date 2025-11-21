### 🎯 Topline Understanding

**KPI:** "Contact Sales" form submissions (typically bottom-of-funnel conversion on website)  
**Change:** -25% Week-over-Week (WoW)  
**Assumptions:**  
- Metric is captured via web analytics (GA4, Segment, etc.) and pushed to CRM  
- "Week" compares last full week vs. prior full week (e.g., week of June 10 vs. June 3)  
- B2B SaaS context: sales cycle likely 2-8 weeks, deal sizes $5k–$100k+ ARR  

**Critical Missing Context Needed:**  
- Absolute volume: 25% of 40 vs. 25% of 4,000 leads (is this statistically significant?)  
- Baseline volatility: typical WoW variance % (is 25% abnormal or within noise?)  
- Traffic composition: % change in overall website sessions  
- Recent changes: Any deploys, A/B tests, campaign pauses, or calendar events (holiday, fiscal year-end)  
- Data freshness: Is the drop fully captured, or is there a data lag?

---

### 📋 Potential Causes (Breadth)

**Internal — Data & Tracking**
1. Form tracking pixel or GTM event broken/firing incorrectly  
2. CRM sync delay or failure (leads not reaching dashboard)  
3. Attribution window/model change in analytics platform  
4. Data pipeline job failed or backfilled incorrectly  

**Internal — Website & Product**
5. Form broken on specific devices, browsers, or screen sizes  
6. JavaScript error on page blocking form interaction  
7. Page load time degradation (CDN, hosting, new script)  
8. Recent deploy introduced bug or removed form element  
9. A/B test running that inadvertently hurt conversion  

**Internal — Traffic & Marketing**
10. Paid ad spend paused, reduced, or budget capped (LinkedIn, Google, etc.)  
11. Paid ad creative fatigue or auction dynamics (CPC up, CTR down)  
12. Organic search ranking drop (Google algorithm update, technical SEO issue)  
13. Referral traffic source dried up (partner link removed, PR cycle ended)  
14. Email campaign not sent, bounced, or landed in spam  
15. Direct traffic drop (brand search decline, offline awareness dip)  

**Internal — Sales & GTM**
16. Pricing page updated with new numbers or packaging causing sticker shock  
17. Sales team headcount/territory change affecting lead routing display  
18. “Contact Sales” CTA copy or placement changed  

**External & Seasonal**
19. Holiday or long weekend (US: July 4th, Memorial Day; EU: Bank holiday)  
20. Industry event (conference, competitor launch) distracting target audience  
21. Macroeconomic shock (interest rate news, layoffs in target sector)  
22. Competitor launched aggressive promo or POV campaign  

---

### 📊 Ranked Hypotheses (Most → Least Likely)

1. **Tracking or Form Functionality Issue** – *Most common root cause; immediate and binary*  
2. **Paid Traffic Reduction or Performance Decay** – *Largest typical driver of WoW volatility*  
3. **Website Technical Bug Post-Deploy** – *Friday deploys often surface Monday morning*  
4. **Holiday/Calendar Effect** – *Simple calendar check; frequent in summer/Q4*  
5. **A/B Test or CTA Change** – *Unintended consequence of optimization*  
6. **Organic Search Ranking Drop** – *Slower-moving but can cause step-change*  
7. **Referral or Direct Traffic Drop** – *Depends on channel mix*  
8. **Market/Competitive Event** – *Less likely to cause immediate 25% drop*

---

### 🔬 Validation Plan (Top 5)

| Hypothesis | How to Validate (2–3 checks) |
|---|---|
| **H1: Tracking or Form Functionality Issue** | 1. **Live form test:** Submit test lead on desktop Chrome, mobile Safari, incognito mode; verify CRM receipt and GA4 event fire.<br>2. **Console & network check:** Open DevTools on `/contact-sales` page, look for JavaScript errors, failed POST requests, or GTM tag misconfiguration.<br>3. **Data layer audit:** Compare raw server logs (Nginx/Apache) for POST to form endpoint vs. GA4 "form_submit" events WoW; check for 400/500 errors. |
| **H2: Paid Traffic Reduction or Performance Decay** | 1. **Spend & status audit:** Log into LinkedIn Ads & Google Ads → compare last week’s spend, impressions, campaign status (on/paused) vs. prior week.<br>2. **Traffic source drilldown:** In GA4, filter `session_source` for "google" and "linkedin" → check sessions, users, and conversion rate WoW; overlay cost data.<br>3. **Auction diagnostics:** Review CPC, CTR, and impression share trends; check if new competitors entered auctions (Auction Insights). |
| **H3: Website Technical Bug Post-Deploy** | 1. **Deploy log review:** Check GitHub/GitLab merge history for Friday or weekend commits; identify any changes to contact page, form component, or global header/footer.<br>2. **Performance & error monitoring:** Query Datadog/New Relic for 5xx/4xx errors on `/contact-sales`, page load time (LCP), and JavaScript error rate spikes.<br>3. **Device/browser segmentation:** In GA4, segment form submissions by device category and browser; check if drop is isolated to Safari iOS or Chrome desktop. |
| **H4: Holiday/Calendar Effect** | 1. **Calendar mapping:** Identify if last week contained a US federal holiday, major EU bank holiday, or school vacation period for core ICP (e.g., CTOs with kids).<br>2. **YoY comparison:** Pull same week last year submissions; check if seasonal pattern repeats (e.g., 20–30% dip during July 4th week).<br>3. **Day-of-week drilldown:** In GA4, breakdown submissions by day; look for full-day zeroes or low weekdays suggesting OOO patterns. |
| **H5: A/B Test or CTA Change** | 
