# Product Management Templates

## Product Requirements Document (PRD)

```markdown
# [Feature/Product Name] - PRD

**Version:** 1.0
**Date:** [Date]
**Author:** [Your Name]
**Status:** [Draft / In Review / Approved]

## Executive Summary
[2-3 sentences: What is this, why are we building it, what's the expected impact?]

## Problem Statement

### Background
[Context: What's the current situation? What pain points exist?]

### User Problem
[Specific problem users are facing. Use quotes or data from user research.]

### Business Problem
[Why does this matter to the business? Revenue, retention, strategic importance?]

## Goals & Success Metrics

### Objectives
1. [Primary objective with measurable outcome]
2. [Secondary objective with measurable outcome]

### Success Metrics

| Metric | Baseline | Target | Timeline |
|--------|----------|--------|----------|
| [Metric 1] | [Current value] | [Goal value] | [When] |
| [Metric 2] | [Current value] | [Goal value] | [When] |

### Key Performance Indicators (KPIs)
- **Leading Indicators:** [Metrics to track during development]
- **Lagging Indicators:** [Outcome metrics after launch]

## Target Users

### Primary Users
- **Who:** [User segment description]
- **Characteristics:** [Demographics, behaviors, needs]
- **Pain Points:** [What problems do they have?]

### Secondary Users
[If applicable]

### User Personas
[Link to detailed personas or include brief descriptions]

## Scope

### In Scope (v1.0)
- [Feature/capability 1]
- [Feature/capability 2]
- [Feature/capability 3]

### Out of Scope (Future Considerations)
- [Explicitly excluded item 1]
- [Explicitly excluded item 2]

### MVP Definition
[What's the minimum viable version? What can we cut?]

## User Stories

### Core User Flows

**User Story 1: [Title]**
```
As a [user type]
I want to [action]
So that [benefit]

Acceptance Criteria:
- [ ] Given [context], when [action], then [outcome]
- [ ] Given [context], when [action], then [outcome]
- [ ] Given [context], when [action], then [outcome]

Priority: [High/Medium/Low]
Estimated Effort: [Story points or days]
```

**User Story 2: [Title]**
[Same format]

### Edge Cases & Error Handling
- **Edge Case 1:** [Scenario] → [Expected behavior]
- **Error State 1:** [Error condition] → [User-facing message and action]

## Functional Requirements

### Feature 1: [Name]

**Description:**
[What does this feature do?]

**User Interface:**
- [UI element or screen]
- [Interaction behavior]
- [Visual design notes]

**Business Logic:**
- [Rule 1]
- [Rule 2]

**Data Requirements:**
- Input: [What data is collected?]
- Processing: [How is it processed?]
- Output: [What is displayed/stored?]

### Feature 2: [Name]
[Same structure]

## Non-Functional Requirements

### Performance
- Page load time: [< X seconds]
- API response time: [< X ms]
- Concurrent users: [Support X users]
- Uptime: [99.X%]

### Security
- Authentication: [Method]
- Authorization: [Rules]
- Data encryption: [At rest and in transit]
- Compliance: [GDPR, HIPAA, etc.]

### Accessibility
- WCAG 2.1 Level [A/AA/AAA]
- Screen reader support
- Keyboard navigation
- Color contrast requirements

### Scalability
- Handle [X] users/requests
- Database capacity
- Infrastructure requirements

### Compatibility
- Browsers: [List supported versions]
- Mobile: [iOS X+, Android X+]
- Screen sizes: [Desktop, tablet, mobile]

## User Experience (UX)

### Mockups & Wireframes
[Link to Figma/design files or embed images]

### User Flow Diagrams
[Visual representation of user journey]

### Design Specifications
- Design system components used
- Typography and colors
- Spacing and layout
- Responsive behavior

## Technical Design

### Architecture Overview
[High-level technical approach]

### API Endpoints

**Endpoint 1: [Name]**
```
Method: POST
Path: /api/v1/resource
Request Body: { ... }
Response: { ... }
Status Codes: 200, 400, 401, 500
```

### Database Schema
[New tables, fields, relationships]

### Third-Party Integrations
- [Service 1]: [Purpose and API]
- [Service 2]: [Purpose and API]

### Technical Dependencies
- [Dependency 1]
- [Dependency 2]

## Implementation Plan

### Development Phases

**Phase 1: Foundation (Sprint 1-2)**
- [Task 1]
- [Task 2]

**Phase 2: Core Features (Sprint 3-4)**
- [Task 1]
- [Task 2]

**Phase 3: Polish & Launch (Sprint 5)**
- [Task 1]
- [Task 2]

### Timeline

| Milestone | Date | Owner | Deliverable |
|-----------|------|-------|-------------|
| Design complete | [Date] | [Name] | [Output] |
| Backend API ready | [Date] | [Name] | [Output] |
| Frontend complete | [Date] | [Name] | [Output] |
| QA complete | [Date] | [Name] | [Output] |
| Launch | [Date] | [Name] | [Output] |

## Testing Plan

### Test Scenarios
1. [Scenario 1]: [Expected result]
2. [Scenario 2]: [Expected result]

### QA Requirements
- Unit tests: [Coverage target]
- Integration tests: [Critical paths]
- E2E tests: [User flows]
- Performance tests: [Load scenarios]

### Beta Testing
- Beta users: [Target number and profile]
- Duration: [Timeline]
- Success criteria: [Metrics]

## Launch Plan

### Go-to-Market Strategy
[How will we announce and promote this?]

### Launch Checklist
- [ ] All tests passing
- [ ] Documentation complete
- [ ] Analytics tracking implemented
- [ ] Marketing materials ready
- [ ] Sales team trained
- [ ] Support team prepared
- [ ] Rollout plan defined
- [ ] Rollback plan ready

### Rollout Strategy
- **Approach:** [Gradual rollout / Feature flag / Big bang]
- **Phases:** [% of users per phase]
- **Monitoring:** [What to watch]

## Risks & Mitigation

| Risk | Probability | Impact | Mitigation Strategy | Owner |
|------|-------------|--------|---------------------|-------|
| [Risk 1] | H/M/L | H/M/L | [Strategy] | [Name] |
| [Risk 2] | H/M/L | H/M/L | [Strategy] | [Name] |

## Dependencies

### Internal Dependencies
- [Team/system 1]: [What's needed]
- [Team/system 2]: [What's needed]

### External Dependencies
- [Vendor/partner 1]: [What's needed]
- [Vendor/partner 2]: [What's needed]

## Assumptions & Constraints

### Assumptions
- [Assumption 1]
- [Assumption 2]

### Constraints
- Budget: [Limit]
- Timeline: [Deadline]
- Resources: [Team size]
- Technical: [Platform limitations]

## Open Questions
- [ ] [Question 1] - Owner: [Name] - Due: [Date]
- [ ] [Question 2] - Owner: [Name] - Due: [Date]

## Appendix

### References
- User research: [Link]
- Competitive analysis: [Link]
- Technical specs: [Link]

### Change Log

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | [Name] | Initial draft |
| 1.1 | [Date] | [Name] | [Description] |

### Approval

| Stakeholder | Role | Status | Date |
|-------------|------|--------|------|
| [Name] | Product Lead | Pending | |
| [Name] | Engineering Lead | Pending | |
| [Name] | Design Lead | Pending | |
```

---

## Product Roadmap Template

### Theme-Based Roadmap

```markdown
# [Product Name] Roadmap - [Year]

## Product Vision
[One paragraph: Where are we going? What's our north star?]

## Strategic Themes
1. **[Theme 1]**: [Description and why it matters]
2. **[Theme 2]**: [Description and why it matters]
3. **[Theme 3]**: [Description and why it matters]

## Q1 [Year]: [Quarter Theme]

**Goals:**
- [Goal 1 with metric]
- [Goal 2 with metric]

**Key Initiatives:**

### Initiative 1: [Name]
- **Theme:** [Which strategic theme]
- **Problem:** [What problem does this solve?]
- **Impact:** [Expected business/user impact]
- **Status:** [Not Started / In Progress / Completed]
- **Owner:** [Team/Person]
- **Timeline:** [Weeks/Months]

### Initiative 2: [Name]
[Same structure]

**Expected Outcomes:**
- [Metric 1]: [Target]
- [Metric 2]: [Target]

## Q2 [Year]: [Quarter Theme]
[Same structure]

## Q3 [Year]: [Quarter Theme]
[Same structure - less detail, higher level]

## Q4 [Year]: [Quarter Theme]
[Same structure - even higher level]

## Future Considerations (Beyond [Year])
- [Idea 1]: [Brief description]
- [Idea 2]: [Brief description]

## Recently Shipped ✅
- [Feature 1] - [Date] - [Impact achieved]
- [Feature 2] - [Date] - [Impact achieved]
```

### Now-Next-Later Roadmap

```markdown
# Product Roadmap: Now-Next-Later

## NOW (Current Quarter)
**We are focused on:**

### 🎯 [Initiative 1]
- **Why:** [Problem and opportunity]
- **What:** [Key features]
- **Success:** [Metrics]
- **Teams:** [Who's working on it]

### 🎯 [Initiative 2]
[Same structure]

## NEXT (Next 1-2 Quarters)
**Coming up:**

### [Initiative 1]
- **Why:** [Brief rationale]
- **What:** [High-level scope]

### [Initiative 2]
[Same structure]

## LATER (Future / Ideas)
**Under consideration:**

- [Idea 1]: [One-line description]
- [Idea 2]: [One-line description]
- [Idea 3]: [One-line description]

*These are not commitments and may change based on learnings.*
```

---

## Product Strategy Template

```markdown
# [Product Name] Strategy - [Year]

## Mission
[Why does this product exist? What's our purpose?]

## Vision (3-5 years)
[Where are we going? What will success look like?]

## Current State

### Market Position
- Market size: [TAM/SAM/SOM]
- Market share: [%]
- Competitors: [List key competitors]

### Product Metrics
- Users: [MAU/DAU]
- Revenue: [MRR/ARR]
- NPS: [Score]
- Key trends: [Growth/challenges]

## Target Market

### Primary Segment
- **Who:** [Description]
- **Size:** [Market size]
- **Needs:** [Top 3 pain points]
- **Value:** [Why they'll pay]

### Secondary Segments
[List briefly]

## Value Proposition
[Clear statement of unique value we provide]

**For** [target customer]
**Who** [need/opportunity]
**Our product** [product category]
**That** [key benefit]
**Unlike** [competitors]
**We** [unique differentiator]

## Strategic Priorities

### Priority 1: [Title]
- **Goal:** [Specific objective]
- **Why:** [Strategic rationale]
- **Success Metrics:** [KPIs]
- **Key Initiatives:** [What we'll do]
- **Timeline:** [When]

### Priority 2: [Title]
[Same structure]

### Priority 3: [Title]
[Same structure]

## Competitive Strategy

### Competitive Advantages
1. [Advantage 1]: [How we're differentiated]
2. [Advantage 2]: [How we're differentiated]

### Positioning
[How we position vs. competitors]

## Growth Strategy

### Acquisition
- [Channel 1]: [Strategy]
- [Channel 2]: [Strategy]

### Activation
- [Strategy to get users to "aha moment"]

### Retention
- [Strategy to keep users engaged]

### Revenue
- [Monetization strategy]
- [Pricing strategy]

## Product Principles
1. [Principle 1]: [What it means]
2. [Principle 2]: [What it means]
3. [Principle 3]: [What it means]

## Success Metrics

### North Star Metric
[The one metric that matters most]: [Target]

### Supporting Metrics
- [Metric 1]: [Current] → [Target]
- [Metric 2]: [Current] → [Target]
- [Metric 3]: [Current] → [Target]

## Risks & Challenges
1. [Risk 1]: [Mitigation approach]
2. [Risk 2]: [Mitigation approach]

## Resource Requirements
- Team size: [Current / Needed]
- Budget: [Amount]
- Key hires: [Roles needed]
```

---

## User Story Template

```markdown
## [Story Title]

**As a** [type of user]
**I want** [goal/action]
**So that** [benefit/value]

### Acceptance Criteria
- [ ] Given [initial context], when [action], then [expected outcome]
- [ ] Given [another context], when [action], then [expected outcome]
- [ ] Given [edge case], when [action], then [expected outcome]

### Definition of Done
- [ ] Code complete and reviewed
- [ ] Unit tests written and passing
- [ ] Integration tests passing
- [ ] Acceptance criteria verified by PM
- [ ] Documentation updated
- [ ] Analytics tracking implemented
- [ ] Design review passed
- [ ] Accessibility requirements met
- [ ] Deployed to staging

### Details

**Background:**
[Additional context about why this story exists]

**Design:**
[Link to mockups/wireframes]

**Technical Notes:**
[Any technical considerations, APIs, dependencies]

**Edge Cases:**
- [Edge case 1 and how to handle]
- [Edge case 2 and how to handle]

**Open Questions:**
- [ ] [Question 1]
- [ ] [Question 2]

### Story Points
[Fibonacci: 1, 2, 3, 5, 8, 13, 21]

### Priority
[High / Medium / Low]

### Dependencies
- [Depends on Story-XXX]
- [Blocks Story-YYY]

### Labels
[Feature / Bug / Tech Debt / Enhancement]
```

---

## Go-to-Market Plan Template

```markdown
# Go-to-Market Plan: [Feature/Product Name]

## Executive Summary
[What we're launching, when, and expected impact]

## Product Overview

### What We're Launching
[Description of feature/product]

### Target Audience
- Primary: [User segment]
- Secondary: [User segment]

### Value Proposition
[Key benefit and differentiation]

## Launch Goals

| Goal | Metric | Target | Timeline |
|------|--------|--------|----------|
| [Goal 1] | [Metric] | [Number] | [Date] |
| [Goal 2] | [Metric] | [Number] | [Date] |

## Positioning & Messaging

### Key Messages
1. **Headline:** [Main message]
2. **Supporting Points:**
   - [Point 1]
   - [Point 2]
   - [Point 3]

### Messaging by Audience

**For [Segment 1]:**
- Problem: [Their pain point]
- Solution: [How we solve it]
- Benefit: [What they gain]

**For [Segment 2]:**
[Same structure]

## Marketing Strategy

### Pre-Launch (Weeks -4 to 0)
- [ ] [Activity 1] - Owner: [Name] - Date: [Date]
- [ ] [Activity 2] - Owner: [Name] - Date: [Date]

### Launch Week
- [ ] [Activity 1] - Owner: [Name] - Date: [Date]
- [ ] [Activity 2] - Owner: [Name] - Date: [Date]

### Post-Launch (Weeks +1 to +4)
- [ ] [Activity 1] - Owner: [Name] - Date: [Date]
- [ ] [Activity 2] - Owner: [Name] - Date: [Date]

### Marketing Channels
- **Email:** [Campaign details]
- **Blog:** [Post topics]
- **Social:** [Platform strategy]
- **PR:** [Media targets]
- **Paid:** [Ad strategy]

## Sales Enablement

### Sales Collateral
- [ ] Feature one-pager
- [ ] Demo script
- [ ] Sales deck updates
- [ ] Competitive battle cards
- [ ] Pricing/packaging updates
- [ ] FAQ document

### Sales Training
- Training date: [Date]
- Training materials: [Link]
- Demo environment: [Link]

## Customer Success

### Support Preparation
- [ ] Help center articles
- [ ] FAQ updates
- [ ] Support ticket templates
- [ ] Escalation process
- [ ] Team training complete

### Onboarding Updates
- [ ] Product tours updated
- [ ] Email sequences updated
- [ ] Video tutorials created

## Launch Timeline

| Date | Milestone | Owner | Status |
|------|-----------|-------|--------|
| [Date] | Feature complete | Eng | ✅ |
| [Date] | QA complete | QA | ✅ |
| [Date] | Marketing ready | Marketing | 🟡 |
| [Date] | Sales trained | Sales | ⬜ |
| [Date] | Launch! | PM | ⬜ |

## Success Metrics

### Week 1 Targets
- [Metric]: [Target]
- [Metric]: [Target]

### Month 1 Targets
- [Metric]: [Target]
- [Metric]: [Target]

### Quarter 1 Targets
- [Metric]: [Target]
- [Metric]: [Target]

## Risk Mitigation

| Risk | Mitigation | Owner |
|------|------------|-------|
| [Risk 1] | [Plan] | [Name] |
| [Risk 2] | [Plan] | [Name] |

## Budget
- Marketing: $[Amount]
- Sales: $[Amount]
- Other: $[Amount]
- **Total:** $[Amount]
```

---

These templates are starting points. Customize them for your product, team, and company culture. The best template is one that provides structure while remaining flexible and actually gets used by the team.
