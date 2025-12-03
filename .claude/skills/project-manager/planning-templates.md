# Planning Templates & Tools

## User Story Template

### Standard Format

```
As a [type of user]
I want [goal/desire]
So that [benefit/value]

Acceptance Criteria:
- [ ] Given [context], when [action], then [outcome]
- [ ] Given [context], when [action], then [outcome]
- [ ] Given [context], when [action], then [outcome]

Definition of Done:
- [ ] Code complete and reviewed
- [ ] Unit tests written and passing
- [ ] Integration tests passing
- [ ] Documentation updated
- [ ] Deployed to staging
- [ ] Acceptance criteria met
- [ ] Product owner sign-off

Technical Notes:
[Any technical considerations, dependencies, or constraints]

Story Points: [Fibonacci: 1, 2, 3, 5, 8, 13]
Priority: [High/Medium/Low]
Dependencies: [List any dependencies]
```

### Example User Story

```
As a registered user
I want to reset my password via email
So that I can regain access to my account if I forget my password

Acceptance Criteria:
- [ ] Given I'm on the login page, when I click "Forgot Password", then I see a password reset form
- [ ] Given I enter a valid email, when I submit, then I receive a reset link within 5 minutes
- [ ] Given I click the reset link, when it's less than 24 hours old, then I can set a new password
- [ ] Given I set a new password, when I submit, then I'm logged in automatically
- [ ] Given the reset link is older than 24 hours, when I click it, then I see an "expired link" message

Definition of Done:
- [ ] Code complete and peer reviewed
- [ ] Unit tests covering happy path and edge cases
- [ ] Email templates created and tested
- [ ] Rate limiting implemented (max 3 requests per hour)
- [ ] Security review completed
- [ ] User documentation updated
- [ ] Tested on all supported browsers
- [ ] Product owner approved

Technical Notes:
- Use bcrypt for password hashing
- Token stored with 24-hour expiration
- Rate limiting at API gateway level
- Email service: SendGrid
- Database: Add password_reset_tokens table

Story Points: 5
Priority: High
Dependencies: Email service integration (Story-123)
```

---

## Sprint Planning Template

### Sprint Information

```
Sprint Number: [X]
Sprint Goal: [One-sentence description of what we aim to achieve]
Sprint Duration: [Start Date] to [End Date] ([X] working days)
Team Capacity: [X] story points (based on historical velocity)

Team Members Present:
- [Name] - [Role] - Available: [X%]
- [Name] - [Role] - Available: [X%]

Holidays/PTO This Sprint:
- [Date]: [Person] - [Reason]
```

### Sprint Backlog

```
| Story ID | Title | Story Points | Assigned To | Status |
|----------|-------|--------------|-------------|--------|
| US-101 | User authentication | 8 | Team | To Do |
| US-102 | Password reset | 5 | Team | To Do |
| BUG-45 | Fix login timeout | 3 | Team | To Do |
| TECH-12 | Refactor auth module | 5 | Team | To Do |

Total Committed: 21 story points
Team Capacity: 25 story points
Buffer: 4 story points (16%)
```

### Sprint Goals & Risks

```
Sprint Goal:
Complete user authentication flow enabling users to sign up, log in, and reset passwords securely.

Success Criteria:
- [ ] All authentication stories completed
- [ ] Security review passed
- [ ] Zero critical bugs in production
- [ ] Documentation updated

Known Risks:
- Risk: Third-party email service integration not tested
  Mitigation: Mock service ready for testing, vendor support ticket open

- Risk: Security review might uncover issues
  Mitigation: Scheduled early in sprint, buffer time allocated

Dependencies:
- Email service API credentials (blocker: waiting on IT)
- SSL certificate renewal (due mid-sprint)
```

---

## Project Charter Template

```
# Project Charter: [Project Name]

## Executive Summary
[2-3 sentence overview of the project]

## Business Case
**Problem Statement:**
[What problem are we solving?]

**Opportunity:**
[What opportunity are we pursuing?]

**Expected Benefits:**
- [Quantifiable benefit 1]
- [Quantifiable benefit 2]
- [Quantifiable benefit 3]

## Project Objectives

**SMART Goals:**
1. [Specific, Measurable, Achievable, Relevant, Time-bound goal]
2. [SMART goal]
3. [SMART goal]

**Success Criteria:**
- [ ] [Measurable success criterion]
- [ ] [Measurable success criterion]
- [ ] [Measurable success criterion]

## Scope

**In Scope:**
- [Feature/capability 1]
- [Feature/capability 2]
- [Feature/capability 3]

**Out of Scope:**
- [Explicitly excluded item 1]
- [Explicitly excluded item 2]

**Assumptions:**
- [Assumption 1]
- [Assumption 2]

**Constraints:**
- Budget: [Amount]
- Timeline: [Date range]
- Resources: [Team size, skills]
- Technical: [Platforms, technologies]

## Stakeholders

| Name | Role | Responsibility | Communication Frequency |
|------|------|----------------|------------------------|
| [Name] | Executive Sponsor | Funding, strategic direction | Monthly |
| [Name] | Product Owner | Requirements, prioritization | Daily |
| [Name] | Tech Lead | Architecture, technical decisions | Daily |
| [Name] | QA Lead | Quality standards, testing | Weekly |

## High-Level Timeline

| Phase | Duration | Key Deliverables | End Date |
|-------|----------|------------------|----------|
| Discovery | 2 weeks | Requirements doc, architecture | [Date] |
| Design | 3 weeks | Mockups, API specs | [Date] |
| Development | 12 weeks | Working software, tests | [Date] |
| Testing | 2 weeks | Test reports, bug fixes | [Date] |
| Deployment | 1 week | Production release | [Date] |

## Budget

| Category | Estimated Cost |
|----------|----------------|
| Personnel | $[Amount] |
| Infrastructure | $[Amount] |
| Third-party services | $[Amount] |
| Contingency (15%) | $[Amount] |
| **Total** | **$[Amount]** |

## Risks

| Risk | Probability | Impact | Mitigation Strategy |
|------|-------------|--------|---------------------|
| [Risk 1] | High/Med/Low | High/Med/Low | [Strategy] |
| [Risk 2] | High/Med/Low | High/Med/Low | [Strategy] |

## Approvals

| Name | Role | Signature | Date |
|------|------|-----------|------|
| [Name] | Sponsor | | |
| [Name] | Product Owner | | |
| [Name] | Project Manager | | |
```

---

## Sprint Retrospective Templates

### Start-Stop-Continue Format

```
Sprint [X] Retrospective - [Date]

What should we START doing?
- [Action item with owner and deadline]
- [Action item with owner and deadline]

What should we STOP doing?
- [Action item with owner and deadline]
- [Action item with owner and deadline]

What should we CONTINUE doing?
- [Practice to maintain]
- [Practice to maintain]

Action Items:
1. [Owner] will [action] by [date]
2. [Owner] will [action] by [date]

Impediments Raised:
- [Impediment] - Status: [Resolved/In Progress/Escalated]
```

### 4 Ls Format (Liked, Learned, Lacked, Longed For)

```
What we LIKED:
- Daily standups were efficient
- Code reviews were thorough
- Great collaboration between frontend/backend

What we LEARNED:
- API design needs more upfront planning
- Parallel testing reduces bottlenecks
- Earlier security review catches issues

What we LACKED:
- Clear acceptance criteria on some stories
- Sufficient staging environment capacity
- Time for technical debt reduction

What we LONGED FOR:
- More automated testing
- Better monitoring tools
- Dedicated time for learning

Action Items:
- [Owner]: Implement acceptance criteria template by [date]
- [Owner]: Request staging environment upgrade by [date]
- [Owner]: Allocate 20% sprint capacity for tech debt
```

---

## Status Report Template

```
# Project Status Report
**Project:** [Name]
**Period:** [Start Date] - [End Date]
**Prepared by:** [PM Name]
**Date:** [Date]

## Executive Summary
[2-3 sentences: overall status, key achievements, critical issues]

## Status Dashboard

| Metric | Status | Trend |
|--------|--------|-------|
| Schedule | 🟢 On Track | → |
| Budget | 🟢 On Track | → |
| Scope | 🟡 At Risk | ↓ |
| Quality | 🟢 On Track | ↑ |
| Team Health | 🟢 Good | → |

Legend: 🟢 On Track | 🟡 At Risk | 🔴 Off Track
Trend: ↑ Improving | → Stable | ↓ Declining

## Progress This Period

**Completed:**
- [Major deliverable or milestone]
- [Feature completed]
- [Achievement]

**In Progress:**
- [Work item] - [% complete]
- [Work item] - [% complete]

**Velocity:**
- Planned: [X] story points
- Completed: [Y] story points
- Sprint Goal: [Achieved / Not Achieved]

## Key Metrics

- **Velocity Trend:** [X] points (3-sprint average: [Y] points)
- **Defect Count:** [X] open bugs (P0: [X], P1: [X], P2: [X])
- **Test Coverage:** [X]%
- **Technical Debt:** [X] hours estimated
- **Team Capacity:** [X]% utilized

## Upcoming Next Period

**Priorities:**
1. [Top priority deliverable]
2. [Second priority]
3. [Third priority]

**Milestones:**
- [Date]: [Milestone name]
- [Date]: [Milestone name]

## Risks & Issues

**Active Risks:**
1. **[Risk Title]** - Probability: [H/M/L] | Impact: [H/M/L]
   - Mitigation: [Strategy]
   - Owner: [Name]

**Open Issues:**
1. **[Issue Title]** - Severity: [Critical/High/Medium/Low]
   - Impact: [Description]
   - Action: [What's being done]
   - Owner: [Name]

**Blocked Items:**
- [Item] - Blocked by: [Blocker] - Days blocked: [X]

## Budget

| Item | Budget | Actual | Variance | % Used |
|------|--------|--------|----------|--------|
| Personnel | $[X] | $[Y] | $[Z] | [%] |
| Infrastructure | $[X] | $[Y] | $[Z] | [%] |
| **Total** | **$[X]** | **$[Y]** | **$[Z]** | **[%]** |

## Decisions Needed

1. **[Decision required]**
   - Options: [A, B, C]
   - Recommendation: [Option X] because [rationale]
   - Needed by: [Date]

## Stakeholder Feedback

**Recent Feedback:**
- [Stakeholder]: [Feedback summary]
- [Stakeholder]: [Feedback summary]

**Actions Taken:**
- [Action in response to feedback]

## Appendix

**Burn-up Chart:** [Link or embedded chart]
**Velocity Chart:** [Link or embedded chart]
**Detailed Sprint Backlog:** [Link]
```

---

## Risk Register Template

```
# Risk Register

## Risk Categories
- Technical (T): Architecture, technology, integration
- Resource (R): People, skills, availability
- Schedule (S): Deadlines, dependencies, delays
- Business (B): Requirements, market, stakeholder
- External (E): Vendors, regulations, infrastructure

---

| ID | Risk Description | Category | Probability | Impact | Score | Mitigation Strategy | Owner | Status |
|----|------------------|----------|-------------|--------|-------|---------------------|-------|--------|
| R001 | Key developer might leave | R | Medium (50%) | High (8) | 4.0 | Cross-training, documentation | PM | Active |
| T001 | API integration complexity unknown | T | High (70%) | High (9) | 6.3 | Spike, vendor support | Tech Lead | Mitigated |
| S001 | Third-party dependency delay | S | Medium (40%) | Medium (6) | 2.4 | Alternative identified | PM | Active |
| B001 | Requirements may change | B | High (60%) | Medium (7) | 4.2 | Agile approach, buffer | PO | Accepted |

**Risk Score Calculation:** Probability (%) × Impact (1-10) / 10

**Probability Levels:**
- Low: 0-33%
- Medium: 34-66%
- High: 67-100%

**Impact Levels:**
- Low: 1-3 (Minor inconvenience)
- Medium: 4-7 (Moderate impact on schedule/scope)
- High: 8-10 (Significant impact, project jeopardy)

**Risk Status:**
- Active: Being monitored
- Mitigated: Action taken, reduced probability/impact
- Resolved: No longer a risk
- Accepted: Acknowledged, no mitigation planned
- Occurred: Became an issue, response plan executing

---

## Risk Response Strategies

For each risk, choose appropriate response:

**Avoid:** Change plan to eliminate risk
**Mitigate:** Reduce probability or impact
**Transfer:** Shift risk to third party (insurance, outsourcing)
**Accept:** Acknowledge but take no action
**Exploit:** Take advantage of positive risks (opportunities)
```

---

## Definition of Done Checklist

### Story Level

```
- [ ] Code complete
- [ ] Code reviewed and approved
- [ ] Unit tests written and passing (>80% coverage)
- [ ] Integration tests passing
- [ ] No known defects
- [ ] Documentation updated (inline comments, README)
- [ ] Acceptance criteria met
- [ ] Deployed to dev environment
- [ ] Deployed to staging environment
- [ ] QA tested and approved
- [ ] Product owner accepted
- [ ] Security checklist completed (if applicable)
- [ ] Performance tested (if applicable)
- [ ] Accessibility tested (if applicable)
```

### Sprint Level

```
- [ ] All committed stories meet story-level DoD
- [ ] Sprint goal achieved
- [ ] No critical or high-priority bugs
- [ ] Code merged to main branch
- [ ] Regression tests passing
- [ ] Demo successfully completed
- [ ] Release notes drafted
- [ ] Monitoring/alerts configured
- [ ] Retrospective completed with action items
```

### Release Level

```
- [ ] All sprint-level DoD met
- [ ] User acceptance testing completed
- [ ] Performance testing completed
- [ ] Security assessment completed
- [ ] Load testing completed
- [ ] Documentation finalized (user docs, API docs)
- [ ] Deployment runbook created
- [ ] Rollback plan tested
- [ ] Monitoring dashboards configured
- [ ] Alerts and on-call rotation set up
- [ ] Training materials prepared
- [ ] Stakeholder sign-off obtained
- [ ] Production deployment completed
- [ ] Post-deployment verification passed
- [ ] Release retrospective completed
```

---

These templates are starting points. Adapt them to your team's context, tools, and preferences. The best template is one that your team actually uses consistently.
