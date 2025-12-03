# Product Metrics & Analytics Guide

## North Star Metric

### What is a North Star Metric?
The single metric that best captures the core value your product delivers to customers.

### Characteristics of Good North Star Metrics
- Captures value delivered to customers
- Reflects engagement and stickiness
- Actionable by the team
- Leading indicator of revenue
- Easy to understand and communicate

### Examples by Product Type

**Social/Communication:**
- WhatsApp: Messages sent per day
- Slack: Messages sent by teams
- LinkedIn: Weekly active users

**Marketplaces:**
- Airbnb: Nights booked
- Uber: Rides completed per week
- eBay: Gross merchandise value (GMV)

**SaaS:**
- HubSpot: Weekly active teams
- Notion: Collaborative documents created
- Figma: Files created with 3+ collaborators

**Content/Media:**
- Netflix: Hours watched
- Spotify: Time spent listening
- YouTube: Watch time

**E-commerce:**
- Amazon: Purchases per month
- Shopify: Stores with revenue > $X

---

## AARRR Metrics (Pirate Metrics)

### 1. Acquisition
**Definition:** How users find your product

**Key Metrics:**
- **Traffic Sources:** Organic, paid, referral, direct
- **Visitors:** Unique visitors, page views
- **Signup Rate:** % of visitors who sign up
- **Cost per Acquisition (CPA):** Marketing spend / new users
- **Traffic Quality:** Bounce rate, time on site

**Formulas:**
```
Signup Rate = (Signups / Visitors) × 100%
CPA = Total Marketing Spend / New Users Acquired
```

**Targets:**
- B2C: 2-5% signup rate
- B2B: 5-15% signup rate
- CPA < LTV/3 (healthy ratio)

### 2. Activation
**Definition:** Users experience core value ("aha moment")

**Key Metrics:**
- **Activation Rate:** % who complete key action
- **Time to Value:** How long to reach aha moment
- **Onboarding Completion:** % who finish onboarding
- **Feature Adoption:** % who use core features

**Common Activation Moments:**
- Slack: Send 2,000 messages
- Dropbox: Upload first file
- Twitter: Follow 30 users
- Facebook: Connect with 7 friends in 10 days

**Formulas:**
```
Activation Rate = (Users Who Hit Aha Moment / Total Signups) × 100%
Time to Activation = Average time from signup to aha moment
```

**Targets:**
- Activation rate: 30-50% (good), 50%+ (excellent)
- Time to activation: < 5 minutes (ideal)

### 3. Retention
**Definition:** Users return and continue using product

**Key Metrics:**
- **DAU (Daily Active Users):** Users active each day
- **MAU (Monthly Active Users):** Users active each month
- **DAU/MAU Ratio:** Stickiness measure
- **Retention Curves:** % users returning over time
- **Churn Rate:** % users who leave

**Cohort Retention:**
```
Day 1:  100% (baseline)
Day 7:  40%
Day 30: 25%
Day 90: 20%
```

**Formulas:**
```
Stickiness (DAU/MAU) = (DAU / MAU) × 100%
Retention Rate = ((Users End - New Users) / Users Start) × 100%
Churn Rate = (Users Lost / Users Start) × 100%
```

**Benchmarks:**
- DAU/MAU Ratio:
  - 20%+ = Good
  - 50%+ = Excellent (Facebook ~60%)
- B2B SaaS Monthly Churn:
  - < 5% = Good
  - < 2% = Excellent

### 4. Revenue
**Definition:** Users pay for your product

**Key Metrics:**

**For Subscription Products:**
- **MRR (Monthly Recurring Revenue)**
- **ARR (Annual Recurring Revenue)**
- **ARPU (Average Revenue Per User)**
- **LTV (Lifetime Value)**
- **Expansion Revenue:** Upgrades and upsells

**For Transaction Products:**
- **GMV (Gross Merchandise Value)**
- **Take Rate:** % of transaction value
- **Average Order Value (AOV)**

**For Advertising Products:**
- **ARPU (Average Revenue Per User)**
- **RPM (Revenue Per Mille/Thousand)**
- **Ad Fill Rate**

**Formulas:**
```
MRR = Sum of all subscription revenue for the month
ARR = MRR × 12
ARPU = Total Revenue / Number of Users
LTV = ARPU × Average Customer Lifetime (months)
CAC Payback = CAC / (ARPU × Gross Margin)
LTV:CAC Ratio = LTV / CAC
```

**Targets:**
- LTV:CAC Ratio > 3:1 (healthy)
- CAC Payback < 12 months
- Net Revenue Retention > 100% (for SaaS)

### 5. Referral
**Definition:** Users recommend product to others

**Key Metrics:**
- **Viral Coefficient (K-factor):** Invites per user × conversion rate
- **Net Promoter Score (NPS)**
- **Referral Rate:** % users who refer
- **Invite Conversion Rate:** % invites that convert

**Formulas:**
```
K-factor = (Invites per User) × (Invite Conversion Rate)
NPS = % Promoters - % Detractors
```

**K-factor Interpretation:**
- K < 1: Not viral (need paid acquisition)
- K = 1: Break-even virality
- K > 1: Viral growth

**NPS Benchmarks:**
- < 0: Poor
- 0-30: Good
- 30-70: Excellent
- 70+: World-class

---

## SaaS-Specific Metrics

### Customer Metrics

**Customer Lifetime Value (LTV)**
```
LTV = ARPU × Gross Margin % × (1 / Churn Rate)

Example:
ARPU = $100/month
Gross Margin = 80%
Monthly Churn = 5%

LTV = $100 × 0.8 × (1 / 0.05) = $1,600
```

**Customer Acquisition Cost (CAC)**
```
CAC = Total Sales & Marketing Spend / New Customers Acquired

Example:
Marketing Spend = $50,000
New Customers = 100

CAC = $50,000 / 100 = $500
```

**CAC Payback Period**
```
CAC Payback = CAC / (ARPU × Gross Margin)

Example:
CAC = $500
ARPU = $100
Gross Margin = 80%

CAC Payback = $500 / ($100 × 0.8) = 6.25 months
```

### Growth Metrics

**Monthly Recurring Revenue (MRR) Components**
```
Net New MRR = New MRR + Expansion MRR - Churned MRR - Contraction MRR
```

- **New MRR:** Revenue from new customers
- **Expansion MRR:** Upgrades, upsells, cross-sells
- **Churned MRR:** Cancelled subscriptions
- **Contraction MRR:** Downgrades

**Net Revenue Retention (NRR)**
```
NRR = ((Starting MRR + Expansion - Churn - Contraction) / Starting MRR) × 100%

Example:
Starting MRR = $100,000
Expansion MRR = $15,000
Churned MRR = $5,000
Contraction MRR = $3,000

NRR = (($100,000 + $15,000 - $5,000 - $3,000) / $100,000) × 100% = 107%
```

**Benchmarks:**
- NRR > 100%: Excellent (growth from existing customers)
- NRR 90-100%: Good
- NRR < 90%: Concerning

### The "Rule of 40"
```
Rule of 40 = Revenue Growth Rate + Profit Margin ≥ 40%

Example:
Revenue Growth = 50%
Profit Margin = -5%
Rule of 40 = 50% + (-5%) = 45% ✅ (Healthy)
```

Good indicator of SaaS company health balancing growth and profitability.

---

## Engagement Metrics

### Activity Metrics

**Daily Active Users (DAU)**
- Users who perform core action daily
- Define "active" specifically (e.g., send message, view content)

**Weekly Active Users (WAU)**
- Users active at least once per week

**Monthly Active Users (MAU)**
- Users active at least once per month

**Stickiness Ratio**
```
Stickiness = DAU / MAU

Example:
DAU = 20,000
MAU = 100,000
Stickiness = 20,000 / 100,000 = 20%
```

### Session Metrics

**Session Length**
- Average time per session
- Longer isn't always better (depends on product)

**Session Frequency**
- Number of sessions per user per day/week
- Higher frequency = more engaged

**Bounce Rate**
- % of single-page sessions
- High bounce may indicate poor UX or targeting

### Feature Adoption

**Feature Adoption Rate**
```
Adoption Rate = (Users Using Feature / Total Active Users) × 100%
```

**Feature Retention**
```
Day 7 Feature Retention = (Users Still Using Feature / Users Who Tried It) × 100%
```

---

## Product-Market Fit Metrics

### Sean Ellis Test
Survey question: "How would you feel if you could no longer use [product]?"
- Very disappointed
- Somewhat disappointed
- Not disappointed

**PMF Benchmark:** 40%+ "very disappointed" indicates strong PMF

### Engagement Indicators
- Organic growth rate
- High retention rates (>40% month 1)
- Low churn (<5% monthly for SaaS)
- Strong NPS (>50)
- High DAU/MAU ratio (>20%)

### Market Signals
- Word-of-mouth growth
- Press coverage without PR
- Inbound sales inquiries
- Waiting list demand

---

## Funnel Metrics

### Conversion Funnel Example

```
Homepage Visit:        10,000 users (100%)
    ↓
Signup Page:           2,000 users (20%)
    ↓
Account Created:       1,000 users (10%)
    ↓
Onboarding Complete:   500 users (5%)
    ↓
First Core Action:     300 users (3%)
    ↓
Active User:           200 users (2%)
```

**Analyzing Funnels:**
- Identify biggest drop-offs
- Optimize steps with largest losses
- A/B test improvements
- Reduce friction at each step

**Conversion Rate**
```
Overall Conversion = (Final Step Users / Initial Step Users) × 100%

Example: 200 / 10,000 = 2%
```

---

## Cohort Analysis

### What is Cohort Analysis?
Group users by shared characteristic (signup date, acquisition channel) and track behavior over time.

### Retention Cohort Example

| Cohort | Month 0 | Month 1 | Month 2 | Month 3 |
|--------|---------|---------|---------|---------|
| Jan    | 100%    | 40%     | 30%     | 25%     |
| Feb    | 100%    | 45%     | 35%     | 28%     |
| Mar    | 100%    | 50%     | 38%     | -       |

**Analysis:**
- February and March cohorts show improving retention
- Product improvements working
- Still losing 60-70% of users (opportunity)

### Revenue Cohort Example

Track revenue generated by each cohort over time to measure LTV.

---

## Experiment Metrics

### A/B Testing

**Sample Size Calculator**
```
Visitors Needed = (Z-score² × Variance) / (Effect Size²)
```

Use online calculators (Optimizely, VWO) for practical calculations.

**Statistical Significance**
- Typically p < 0.05 (95% confidence)
- Don't stop tests early
- Run for full business cycle

**Measuring Results**
```
Improvement = ((Variant Conversion - Control Conversion) / Control Conversion) × 100%

Example:
Control: 10% conversion
Variant: 12% conversion
Improvement = ((12% - 10%) / 10%) × 100% = 20% improvement
```

---

## Dashboard Best Practices

### Key Principles
1. **Focus on outcomes, not outputs**
   - Bad: "We shipped 5 features"
   - Good: "Activation rate increased 15%"

2. **Use the right chart type**
   - Trends over time: Line charts
   - Comparisons: Bar charts
   - Parts of whole: Pie charts (use sparingly)
   - Relationships: Scatter plots

3. **Highlight what matters**
   - Use color to draw attention
   - Show targets/benchmarks
   - Include context and trends

4. **Make it actionable**
   - Clear labels and units
   - Drill-down capability
   - Link metrics to actions

### Example Dashboard Structure

**Executive Dashboard:**
- North Star Metric (large display)
- Key supporting metrics (4-6 metrics)
- Recent trend (up/down indicator)
- Target progress

**Product Team Dashboard:**
- Acquisition metrics
- Activation metrics
- Engagement metrics
- Retention metrics
- Feature adoption
- Funnel analysis

**Growth Dashboard:**
- User growth (daily, weekly, monthly)
- Retention cohorts
- Viral coefficient
- Channel performance
- Conversion funnels

---

## Tools & Platforms

### Analytics Platforms
- **Google Analytics**: Web analytics, free
- **Mixpanel**: Product analytics, event tracking
- **Amplitude**: Product analytics, retention focus
- **Heap**: Automatic event tracking
- **Segment**: Data pipeline, connects tools

### Specialized Tools
- **Pendo**: Product analytics + in-app guidance
- **Hotjar**: Heatmaps, session recordings
- **FullStory**: Session replay, user insights
- **Looker**: Business intelligence, custom dashboards
- **Tableau**: Data visualization

### Survey & Feedback
- **SurveyMonkey**: User surveys
- **Typeform**: Beautiful forms
- **Delighted**: NPS surveys
- **UserTesting**: Usability testing
- **Intercom**: In-app messaging, surveys

---

## Metrics by Product Stage

### Early Stage (Pre-PMF)
Focus on:
- Retention cohorts
- Qualitative feedback
- Core action completion
- Time to value
- "Aha moment" discovery

### Growth Stage (Post-PMF)
Focus on:
- User acquisition & CAC
- Activation rates
- Retention & churn
- Viral coefficient
- Revenue metrics

### Maturity Stage
Focus on:
- LTV optimization
- Market share
- NPS & CSAT
- Operational efficiency
- New market expansion

---

## Common Metric Mistakes

1. **Vanity Metrics**: Metrics that look good but don't predict outcomes
   - Bad: Total registered users
   - Good: Active users (DAU/MAU)

2. **Metric Overload**: Tracking too many metrics
   - Focus on 5-7 key metrics
   - Everything else is supporting

3. **No Benchmarks**: Not comparing to targets or industry
   - Always set targets
   - Know industry benchmarks

4. **Not Segmenting**: Viewing all users as one group
   - Segment by cohort, channel, persona
   - Understand differences

5. **Ignoring Statistical Significance**
   - Don't celebrate noise
   - Understand confidence intervals

---

Remember: Metrics are tools to guide decisions, not goals in themselves. Focus on metrics that reflect real customer value and business outcomes. The best metric is one that drives the right behaviors and helps you make better product decisions.
