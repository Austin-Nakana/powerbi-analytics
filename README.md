
## Backstory

EduReach NGO, a Johannesburg-based non-profit that partners with the Gauteng Department of Education to drive post-school registrations at TVET colleges and universities among Grade 11 and 12 learners in under-resourced communities.
The Problem: EduReach runs targeted social media campaigns across 7 schools in 4 districts. Their programme coordinator, Thandi, has a R50,000 quarterly budget split across Instagram, TikTok, Facebook, and WhatsApp. She suspects she's overspending on Facebook and under-investing in TikTok, but she has no data to prove it. She also doesn't know which schools are converting well vs which ones need on-the-ground support. At the end of Q2 2026, the board is asking: "Are we reaching the right learners, and is the money being spent wisely?"

## Thandi's actual questions:

- Which campaign drove the most registrations per rand spent?
- Which platform is pulling its weight, and which is draining budget?
- Are there schools where impressions are high but registrations are low, meaning awareness exists but something is breaking in   the follow-through?
- Which content type resonates with Grade 12s vs Grade 11s?
- Are we accelerating or stalling as the quarter closes?


## Dashboard Walkthrough

### Page 1 - Executive Summary
<img width="1252" height="892" alt="bi_p1" src="https://github.com/user-attachments/assets/02118227-286b-48e7-9842-2652b3e493dd" />


The first page answers the most fundamental question the board asks before anything else:
# 1. *"At a high level, did the campaign work?"*

The five KPI cards at the top give an immediate snapshot:
- **Total Registrations** - how many learners completed the registration form
- **Confirmed Enrollments** - how many of those registrations were followed up and confirmed
- **Total Spend (ZAR)** - the total budget consumed across all platforms and campaigns
- **Cost per Registration** - the single most important efficiency metric: how much did each registration cost?
- **Budget Utilisation** - what percentage of the allocated budget was actually spent

Below the cards, the **Campaign Conversion Funnel** is the centrepiece of this page. It tracks every learner from first exposure to final enrollment:

> Impressions → Clicks → Link Clicks → Page Views → Form Starts → Registrations → Enrollments

The funnel reveals that EduReach reached over **1.3 million impressions** across the quarter, but only **2,053 learners completed registration** - an end-to-end conversion rate of 0.15%. The most significant drop in the funnel occurs between **Form Starts and Registrations**, meaning learners are finding the campaign, clicking through, and even opening the registration form, but not completing it. This is not a reach problem. It is a form completion problem, and it is the most actionable finding in the entire dashboard.

The slicers on the right allow the board to filter the entire page by campaign, campaign phase, and date range to isolate specific periods or initiatives.

---

### Page 2 - Platform ROI
<img width="1547" height="892" alt="bi_p2" src="https://github.com/user-attachments/assets/88d435d9-f414-4cfc-9514-c70256383e6d" />

This page answers Thandi's second question directly:
# 2. *"Which platform is pulling its weight, and which is draining budget?"*

The **Cost per Registration by Platform** bar chart is the anchor visual. It shows:
- **WhatsApp** - R3.34 per registration (most efficient)
- **TikTok** - R14.04 per registration
- **Instagram** - R20.61 per registration
- **Facebook** - R46.63 per registration (least efficient, 14× more expensive than WhatsApp)

This confirms Thandi's suspicion. Facebook is consuming a disproportionate share of the budget relative to the registrations it delivers. WhatsApp, despite having the smallest reach (only 6.11% of total impressions), delivers the highest conversion intent, learners who engage via WhatsApp are far more likely to register than those who scroll past an Instagram post.

The **Registrations and Spend by Platform** chart shows the volume trade-off. TikTok generates the highest absolute number of registrations (1,069) because it commands the largest share of impressions (51.12%). But when cost is factored in, WhatsApp is the most efficient channel per rand spent.

The **Full Platform Breakdown** table at the bottom ties it all together, showing impressions, clicks, registrations, total spend, cost per registration, and CTR in a single view. The conditional colour formatting on Cost per Registration makes the Facebook inefficiency immediately visible in red.

**Recommendation this page supports:** Reallocate budget away from Facebook toward WhatsApp and TikTok. A 20% reduction in Facebook spend redirected to WhatsApp could yield a significant improvement in cost per registration without reducing total reach.

---

### Page 3 - School Heatmap
<img width="1557" height="897" alt="bi_p3" src="https://github.com/user-attachments/assets/d4f19a28-e335-4d48-a1ee-2dab71c9709c" />


## This page answers Thandi's third question:
# 3. *"Are there schools where impressions are high but registrations are low?"*

The **Impressions vs Registrations Scatter Chart** plots every school as a bubble, where bubble size represents total spend and colour represents school type (Public vs No-Fee Public). Schools in the bottom-right of the chart, high impressions, low registrations — are the ones where digital reach exists but conversion is breaking down.

The **School Performance Table** tells the same story in numbers, sorted by conversion rate ascending:
- **Soweto Academy** - 105,430 impressions, 144 registrations, 0.03 conversion rate (lowest)
- **Alexandra School** - 175,805 impressions, 185 registrations, 0.05 conversion rate

Both are **No-Fee Public** schools. Both sit at the bottom of the conversion table despite receiving significant campaign exposure. This is not a coincidence, learners in these communities face additional barriers to completing registration: limited data access, shared devices, lower digital literacy, and less peer or family support navigating post-school options.

By contrast, **Rosebank Academy** achieves a 0.11 conversion rate - more than 3× that of Soweto Academy, with a similar spend profile.

The `on_ground_support` count column in the table reveals another pattern: schools with more field officer visits correlate with higher conversion rates. Randburg High (39 visits, 0.08 conversion) and Rosebank Academy (54 visits, 0.11 conversion) outperform schools with fewer visits.

**Recommendation this page supports:** Digital spend alone is insufficient for No-Fee Public schools. Soweto Academy and Alexandra School need increased field officer presence to bridge the gap between awareness and action. The data makes the case for a blended outreach model, not more ads, but more people on the ground.

---

### Page 4 - Campaign & Content Performance
<img width="1552" height="897" alt="bi_p4" src="https://github.com/user-attachments/assets/a258b073-34bc-4fa0-9717-5f361f6d0670" />

This page answers two of Thandi's questions simultaneously:
# 4. *"Which campaign drove the most registrations per rand spent?"* and *"Which content type resonates with Grade 12s vs Grade 11s?"*

The **Registrations by Campaign** bar chart broken down by campaign phase shows that **Career Day** and **STEM Drive** led registration volumes across the quarter. Crucially, both peaked during the **Mid phase**, the core campaign period, and tapered off in Close, which points to urgency messaging underperforming in the final stretch (this is explored further on Page 5).

The **Content Type Performance by Platform** stacked bar chart shows how different content formats drive engagement across platforms:
- **TikTok** is almost entirely driven by **Video** content, consistent with platform behaviour globally
- **Facebook** skews toward **Static** content, its audience engages differently
- **Instagram** shows a balanced split between Video and Carousel
- **WhatsApp** is predominantly Static images and direct links

This matters for budget allocation: running Video content on Facebook will underperform relative to running that same content on TikTok. Content format and platform must be matched.

The **Engagement Rate by Content Type and Target Grade** chart answers the demographic question. Filtering to Grade 11 and Grade 12 specifically:
- **Grade 12 learners** respond most strongly to **Video** content, urgency and storytelling formats align with their decision-making timeline (matric year, applications closing)
- **Grade 11 learners** show relatively more engagement with **Carousel** content, browsable, informational formats suit early-stage exploration

**Recommendation this page supports:** For the Close phase of any future campaign, prioritise Video content on TikTok and WhatsApp targeted specifically at Grade 12 learners. This is the combination with the highest conversion potential during the registration deadline window.

---

### Page 5 - Campaign Momentum
<img width="1552" height="895" alt="bi_p5" src="https://github.com/user-attachments/assets/6e94c1e4-e586-4dfe-aca7-21f6043825c4" />

This page answers Thandi's final question:
# 5. *"Are we accelerating or stalling as the quarter closes?"*

The **Registrations Over Time by Campaign Phase** line chart shows the campaign arc clearly. The Mid phase dominates the registration peak, the period of highest activity, spend, and conversion. The Close phase shows a visible decline in registrations despite spend remaining active, which is precisely the pattern that should concern the board.

The **Spend vs Registrations Over Time** dual-axis chart makes this visible side by side. In the Close phase, the spend line stays elevated while the registrations line drops, this is budget waste in motion. Money is still being deployed, but learners are no longer converting at the same rate. The creative has fatigued, urgency messaging is not landing, or the remaining learners in the pipeline are harder to convert without direct intervention.

The **Campaign Phase Dominance Ribbon Chart** shows how different campaigns traded dominance across the quarter, with Career Day and STEM Drive competing for the top position through Mid phase before all campaigns taper into Close.

The **KPI Visual** sets the quarter registration target at 2,500. Actual performance of 2,053 represents an 82% achievement rate, a credible result, but the gap of 447 registrations is attributable almost entirely to the Close phase underperformance. Had the Close phase maintained Mid-phase conversion rates, the target would have been exceeded.

**Recommendation this page supports:** Future campaigns need a dedicated Close phase strategy distinct from Mid — specific deadline-driven creative, direct WhatsApp outreach to learners who started but did not complete forms, and intensified field officer activity in the final two weeks. The data shows the audience exists; the follow-through mechanism is what needs to be built.
