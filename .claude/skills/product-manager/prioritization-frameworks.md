# Feature Prioritization Frameworks

## 1. RICE Score

### Formula
**RICE = (Reach × Impact × Confidence) / Effort**

### Components

**Reach** - How many users will this impact in a given time period?
- Number of users per quarter
- Example: 5,000 users/quarter = 5000

**Impact** - How much will this impact each user?
- Scale: 0.25 (minimal), 0.5 (low), 1 (medium), 2 (high), 3 (massive)
- Example: High impact = 2

**Confidence** - How confident are you in your estimates?
- Scale: 100% (high data), 80% (medium), 50% (low)
- Example: Medium confidence = 80% = 0.8

**Effort** - How many person-months will this take?
- Estimate team effort in person-months
- Example: 2 person-months = 2

### Calculation Example

```
Feature: Advanced Search
- Reach: 10,000 users/quarter
- Impact: 1 (medium)
- Confidence: 80% (0.8)
- Effort: 3 person-months

RICE = (10,000 × 1 × 0.8) / 3 = 2,667

Feature: Push Notifications
- Reach: 50,000 users/quarter
- Impact: 2 (high)
- Confidence: 100% (1.0)
- Effort: 1 person-month

RICE = (50,000 × 2 × 1.0) / 1 = 100,000

Priority: Push Notifications (100,000) > Advanced Search (2,667)
```

### When to Use
- Multiple competing features
- Need objective, quantifiable comparison
- Have data or reasonable estimates
- Team wants structured decision-making

### Pros & Cons

**Pros:**
- Quantitative and objective
- Forces explicit thinking about impact and effort
- Good for comparing diverse features
- Easy to explain and defend

**Cons:**
- Requires estimates (which can be subjective)
- Time-consuming to score many items
- Can give false sense of precision
- Doesn't account for strategic fit

---

## 2. Value vs. Effort Matrix (2×2)

### Framework

```
         High Value
              │
  Quick Wins  │  Major Projects
     ⭐       │      🎯
──────────────┼──────────────
              │
  Low Priority│  Time Sinks
     ❌       │      ⚠️
              │
         Low Value

    Low Effort ← → High Effort
```

### Quadrants

**Quick Wins (High Value, Low Effort)**
- Priority: Do first
- Examples: Small UI improvements, bug fixes with big impact
- Action: Implement immediately

**Major Projects (High Value, High Effort)**
- Priority: Plan carefully
- Examples: New major features, platform migrations
- Action: Roadmap for next quarter, break down

**Time Sinks (Low Value, High Effort)**
- Priority: Avoid
- Examples: Nice-to-haves that are complex
- Action: Deprioritize or reject

**Low Priority (Low Value, Low Effort)**
- Priority: Do if time permits
- Examples: Minor tweaks, experimental features
- Action: Backlog, fill gaps

### How to Use

1. List all features
2. Rate each on Value (1-10) and Effort (1-10)
3. Plot on matrix
4. Focus on Quick Wins first
5. Plan Major Projects with proper resources
6. Avoid Time Sinks

### Example

| Feature | Value | Effort | Quadrant |
|---------|-------|--------|----------|
| Dark mode toggle | 8 | 2 | Quick Win ⭐ |
| Real-time collaboration | 9 | 9 | Major Project 🎯 |
| Custom themes | 3 | 8 | Time Sink ❌ |
| Export to CSV | 4 | 2 | Low Priority |

### When to Use
- Quick prioritization needed
- Simple visualization for stakeholders
- Limited resources
- Need to identify quick wins

---

## 3. MoSCoW Method

### Categories

**Must Have (M)**
- Critical for launch
- Non-negotiable requirements
- System won't work without it
- Legal/compliance requirements

**Should Have (S)**
- Important but not critical
- Significant value
- Can work around if needed
- High priority for future

**Could Have (C)**
- Nice to have
- Adds value but not essential
- Include if time/resources permit
- Low impact if excluded

**Won't Have (W)**
- Explicitly out of scope
- Maybe in future releases
- Helps manage expectations
- Prevents scope creep

### Example: E-commerce Checkout

**Must Have:**
- Add items to cart
- Enter shipping address
- Enter payment information
- Complete purchase
- Order confirmation email

**Should Have:**
- Guest checkout option
- Save payment methods
- Order tracking
- Apply discount codes

**Could Have:**
- Gift wrapping option
- Save multiple addresses
- Wish list integration
- Estimated delivery date

**Won't Have (this release):**
- Buy now, pay later integration
- Subscription options
- International shipping
- Mobile app

### When to Use
- Defining MVP scope
- Managing scope creep
- Stakeholder alignment on priorities
- Release planning

---

## 4. Kano Model

### Categories

**Basic Needs (Threshold)**
- Expected by users
- Absence causes dissatisfaction
- Presence doesn't increase satisfaction
- Example: Website loads quickly, no bugs

**Performance Needs (Linear)**
- More is better
- Linearly related to satisfaction
- Competitive differentiators
- Example: Search speed, feature completeness

**Excitement Needs (Delighters)**
- Unexpected features
- Absence doesn't hurt
- Presence creates delight
- Example: AI suggestions, delightful animations

**Indifferent**
- Users don't care either way
- No impact on satisfaction
- Avoid investing here
- Example: Unused features

**Reverse**
- Actually decreases satisfaction
- Example: Too many notifications, complex UI

### Satisfaction Matrix

```
Satisfaction
     ↑
  +  │     Performance ↗
     │   ╱
  0  │  ╱  Excitement 📈
     │ ╱Basic (expected)
  -  │╱_______________→
     0        Functionality
```

### How to Apply

1. **Identify Basic Needs** - Must have, table stakes
2. **Optimize Performance Needs** - Competitive advantage
3. **Add Delighters** - Create memorable experiences
4. **Avoid Indifferent/Reverse** - Don't waste effort

### Example: Email Client

**Basic Needs:**
- Send/receive email reliably
- Search emails
- Organize with folders

**Performance Needs:**
- Fast search results
- Large attachment support
- Mobile sync speed

**Excitement Needs:**
- Smart reply suggestions
- Email scheduling
- Beautiful design
- Undo send

### When to Use
- Understanding user satisfaction drivers
- Balancing feature types
- Creating delightful products
- Innovation planning

---

## 5. Weighted Scoring

### Process

1. **Define Criteria** - What matters for prioritization?
2. **Assign Weights** - How important is each criterion? (total = 100%)
3. **Score Features** - Rate each feature per criterion (1-10)
4. **Calculate** - Weighted score = Σ(score × weight)
5. **Rank** - Highest score = highest priority

### Example Criteria & Weights

| Criterion | Weight | Rationale |
|-----------|--------|-----------|
| User Value | 30% | Most important |
| Revenue Impact | 25% | Business goal |
| Strategic Alignment | 20% | Long-term vision |
| Technical Feasibility | 15% | Can we build it? |
| Time to Market | 10% | Speed matters |
| **Total** | **100%** | |

### Example Scoring

**Feature A: Advanced Analytics**

| Criterion | Weight | Score (1-10) | Weighted Score |
|-----------|--------|--------------|----------------|
| User Value | 30% | 8 | 2.4 |
| Revenue Impact | 25% | 9 | 2.25 |
| Strategic Alignment | 20% | 10 | 2.0 |
| Technical Feasibility | 15% | 6 | 0.9 |
| Time to Market | 10% | 5 | 0.5 |
| **Total** | | | **8.05** |

**Feature B: Mobile App**

| Criterion | Weight | Score (1-10) | Weighted Score |
|-----------|--------|--------------|----------------|
| User Value | 30% | 9 | 2.7 |
| Revenue Impact | 25% | 7 | 1.75 |
| Strategic Alignment | 20% | 8 | 1.6 |
| Technical Feasibility | 15% | 4 | 0.6 |
| Time to Market | 10% | 3 | 0.3 |
| **Total** | | | **6.95** |

**Result:** Feature A (8.05) > Feature B (6.95)

### When to Use
- Multiple complex criteria
- Need transparent, defendable decisions
- Stakeholder alignment needed
- Complex trade-offs

---

## 6. Opportunity Scoring (Jobs-to-be-Done)

### Process

1. Identify customer jobs (what users want to accomplish)
2. Survey users on:
   - **Importance**: How important is this job? (1-5)
   - **Satisfaction**: How satisfied are you with current solutions? (1-5)
3. Calculate **Opportunity Score** = Importance + (Importance - Satisfaction)
4. Focus on highest opportunity scores

### Opportunity Matrix

```
Importance
     ↑
   5 │  Overserved  │  Opportunities
     │              │      ⭐
   3 │──────────────┼──────────────
     │  Unimportant │  Table Stakes
   1 │              │
     └──────────────┴──────────────→
     1              3              5
                Satisfaction
```

### Example

| Job | Importance | Satisfaction | Opportunity Score |
|-----|------------|--------------|-------------------|
| Find relevant content quickly | 4.5 | 2.0 | 7.0 ⭐ |
| Share with team members | 4.0 | 3.5 | 4.5 |
| Track changes over time | 3.5 | 4.0 | 3.0 |
| Export reports | 3.0 | 4.5 | 1.5 |

**Priority:** "Find relevant content quickly" (7.0) has highest opportunity

### When to Use
- Understanding user pain points
- Customer-driven prioritization
- Finding product gaps
- Feature discovery

---

## 7. Stack Ranking

### Method

Simply rank features in order from most to least important. Force choices.

### Rules

- Only one feature can be #1
- No ties allowed
- Must make hard trade-offs
- Regularly re-evaluate

### Example

```
1. User authentication (must have for launch)
2. Payment processing (revenue critical)
3. Dashboard analytics (high user value)
4. Email notifications (engagement driver)
5. Dark mode (nice to have)
6. Custom themes (low priority)
```

### When to Use
- Simple, quick prioritization
- Small number of features
- Need forced ranking
- Executive decision-making

---

## 8. ICE Score

### Formula
**ICE = (Impact × Confidence × Ease) / 3**

Similar to RICE but without Reach component.

### Components

- **Impact** (1-10): How much will this move the needle?
- **Confidence** (1-10): How sure are you?
- **Ease** (1-10): How easy to implement?

### Example

| Feature | Impact | Confidence | Ease | ICE Score |
|---------|--------|------------|------|-----------|
| Onboarding tour | 8 | 9 | 7 | 8.0 |
| API integration | 9 | 6 | 3 | 6.0 |
| UI polish | 5 | 10 | 9 | 8.0 |

### When to Use
- Faster than RICE
- Don't have reach data
- Early-stage features
- Simpler scoring needed

---

## Choosing a Framework

| Framework | Best For | Complexity | Data Required |
|-----------|----------|------------|---------------|
| RICE | Quantitative decisions | Medium | Medium |
| Value/Effort | Quick visualization | Low | Low |
| MoSCoW | Scope definition | Low | Low |
| Kano | User satisfaction | Medium | High (surveys) |
| Weighted | Complex trade-offs | High | Medium |
| Opportunity | Customer-driven | Medium | High (surveys) |
| Stack Rank | Simple prioritization | Low | Low |
| ICE | Quick scoring | Low | Low |

## Best Practices

1. **Be Consistent**: Use same framework across features
2. **Involve Stakeholders**: Get input from team and leadership
3. **Use Data**: Support with user research and analytics
4. **Document Rationale**: Explain why features scored as they did
5. **Re-evaluate**: Priorities change, revisit regularly
6. **Communicate**: Share prioritization decisions transparently
7. **Say No**: Prioritization means saying no to good ideas
8. **Stay Flexible**: Frameworks guide, don't dictate

## Combined Approach

Many PMs use multiple frameworks:

1. **MoSCoW** to define MVP scope
2. **RICE** to prioritize "Should Have" features
3. **Value/Effort** to find quick wins
4. **Kano** to ensure delighters included

Remember: Frameworks are tools to guide decisions, not replace judgment. Use them to structure thinking and communicate clearly, but always apply product sense and strategic thinking.
