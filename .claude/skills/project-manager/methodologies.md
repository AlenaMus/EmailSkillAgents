# Project Management Methodologies

## Scrum Framework

### Overview
Scrum is an iterative and incremental agile framework for managing complex work, with an emphasis on software development.

### Core Roles

**Product Owner**
- Owns and prioritizes the product backlog
- Defines acceptance criteria
- Makes decisions about scope and priorities
- Available to team for clarifications
- Accepts or rejects work results

**Scrum Master**
- Facilitates scrum ceremonies
- Removes impediments
- Coaches team on agile practices
- Protects team from distractions
- Promotes continuous improvement

**Development Team**
- Self-organizing and cross-functional
- 3-9 members optimal size
- Collectively responsible for deliverables
- Estimates work
- Commits to sprint goals

### Ceremonies (Events)

**Sprint Planning (4-8 hours for 2-week sprint)**
- Review prioritized backlog
- Discuss sprint goal
- Team commits to work they can complete
- Break down stories into tasks
- Output: Sprint backlog and sprint goal

**Daily Standup (15 minutes)**
- What did I do yesterday?
- What will I do today?
- What blockers do I have?
- Purpose: Synchronize and plan the day

**Sprint Review/Demo (2-4 hours)**
- Demonstrate completed work
- Gather stakeholder feedback
- Discuss what was and wasn't completed
- Update product backlog
- Output: Updated backlog, feedback

**Sprint Retrospective (1-3 hours)**
- What went well?
- What could be improved?
- What will we commit to improve?
- Output: Action items for improvement

**Backlog Refinement (Ongoing, ~10% of sprint)**
- Add detail to user stories
- Estimate stories
- Prioritize backlog
- Split large stories
- Review acceptance criteria

### Artifacts

**Product Backlog**
- Prioritized list of features/stories
- Owned by Product Owner
- Living document, continuously refined
- Contains epics, stories, bugs, tech debt

**Sprint Backlog**
- Stories committed for current sprint
- Task breakdown
- Updated daily by team
- Visible on sprint board

**Increment**
- Sum of all completed backlog items
- Must be potentially shippable
- Meets Definition of Done

### Metrics
- Velocity: Story points per sprint
- Sprint burndown: Work remaining in sprint
- Release burnup: Work completed toward release
- Sprint goal success rate

### Best Practices
- Keep sprints time-boxed and consistent (1-4 weeks)
- Don't change sprint scope mid-sprint
- Definition of Done must be clear and agreed
- Maintain consistent velocity over time
- Protect team capacity (don't over-commit)

---

## Kanban Method

### Overview
Kanban is a visual workflow management method focused on continuous delivery without fixed iterations.

### Core Principles

1. **Visualize Workflow**
   - Make all work visible on kanban board
   - Columns represent workflow stages
   - Cards represent work items

2. **Limit Work in Progress (WIP)**
   - Set WIP limits per column
   - Prevents multitasking and context switching
   - Exposes bottlenecks
   - Forces completion before starting new work

3. **Manage Flow**
   - Optimize for smooth flow of work
   - Minimize lead time and cycle time
   - Remove bottlenecks
   - Balance work across team

4. **Make Policies Explicit**
   - Clear definition for each column
   - Entry and exit criteria
   - WIP limits rationale
   - Prioritization rules

5. **Implement Feedback Loops**
   - Daily standup
   - Regular replenishment meetings
   - Service delivery review
   - Retrospectives

6. **Improve Collaboratively**
   - Use data to drive improvements
   - Experiment with changes
   - Evolutionary change over revolution

### Kanban Board Structure

Typical columns:
- Backlog → Ready → In Development → In Review → Testing → Done

With WIP limits:
```
Backlog | Ready [3] | Development [5] | Review [3] | Testing [2] | Done
```

### Key Metrics

**Cycle Time**
- Time from work start to completion
- Lower is better
- Track distribution and trends

**Lead Time**
- Time from request to delivery
- Includes waiting time
- Customer-facing metric

**Throughput**
- Number of items completed per time period
- Measures productivity

**Cumulative Flow Diagram (CFD)**
- Shows work items in each stage over time
- Identifies bottlenecks
- Reveals WIP trends

**Blocker Tracking**
- Number of blocked items
- Time items are blocked
- Blocker categories

### Best Practices
- Start with existing process, evolve gradually
- Pull work, don't push
- Focus on flow efficiency over resource efficiency
- Make bottlenecks visible
- Class of service for different work types (expedite, standard, etc.)

---

## Scaled Agile Framework (SAFe)

### Overview
SAFe is a framework for scaling agile practices to large enterprises with multiple teams working together.

### Levels

**Team Level**
- Scrum/Kanban teams
- 5-11 people per team
- Iterations (2 weeks typical)

**Program Level**
- Agile Release Train (ART)
- 50-125 people
- 5-12 teams
- Program Increments (PIs) - 8-12 weeks

**Large Solution Level**
- Multiple ARTs
- Solution Train
- Complex solutions requiring coordination

**Portfolio Level**
- Strategic themes
- Portfolio backlog
- Budget allocation
- Epic approval

### Program Increment (PI) Planning

**Preparation (2 weeks before)**
- Product Management prepares features
- Architecture defines enablers
- Teams review capacity

**Day 1**
- Business context presentation
- Product vision
- Architecture vision
- Team breakouts for planning
- Draft plans review

**Day 2**
- Continue team planning
- Risk identification (ROAM)
- PI objectives finalization
- Management review and commitment
- Final plan presentation

**Outputs**
- Committed PI objectives per team
- Program board showing dependencies
- Risk identification (ROAM log)
- Confidence vote

### Key Events

**ART Sync (weekly/bi-weekly)**
- Cross-team coordination
- Dependency management
- Risk and impediment discussion

**System Demo (every 2 weeks)**
- Integrated demo of all teams' work
- Stakeholder feedback
- Progress toward PI objectives

**Inspect & Adapt (end of PI)**
- PI System Demo
- Quantitative assessment
- Problem-solving workshop
- Improvement backlog

### Best Practices
- Commit to PI planning attendance (all hands)
- Make dependencies visible on program board
- Address risks immediately (ROAM: Resolved, Owned, Accepted, Mitigated)
- Maintain architectural runway
- 80% planned, 20% buffer for emergent work

---

## Hybrid Approaches

### Scrumban
Combines Scrum's ceremonies with Kanban's flow and WIP limits.

**Structure**
- Time-boxed iterations (optional)
- Kanban board with WIP limits
- Scrum ceremonies (standup, retro, review)
- On-demand planning
- Continuous improvement focus

**When to Use**
- Transition from Scrum to Kanban
- Maintenance and support teams
- Teams with high interrupt rate
- Need structure but also flow optimization

### Scrum with Kanban Metrics
- Keep Scrum framework
- Add WIP limits to sprint board
- Track cycle time and flow
- Use CFD for sprint health

---

## Waterfall (Traditional PM)

### Overview
Sequential phases with formal gates between stages. Still relevant for certain project types.

### Phases

1. **Requirements**
   - Gather and document all requirements
   - Requirements specification document
   - Sign-off before moving forward

2. **Design**
   - System architecture
   - Database design
   - UI/UX design
   - Design documents

3. **Implementation**
   - Code development
   - Unit testing
   - Code reviews

4. **Testing**
   - Integration testing
   - System testing
   - User acceptance testing

5. **Deployment**
   - Production release
   - Training
   - Documentation

6. **Maintenance**
   - Bug fixes
   - Enhancements
   - Support

### When to Use
- Fixed scope, timeline, and budget
- Regulatory requirements demand extensive documentation
- Well-understood domain with stable requirements
- Hardware/infrastructure projects
- Contract-based projects with fixed deliverables

### Challenges
- Requirements changes are expensive
- Late feedback from users
- Risk discovered late in project
- Long time to market
- All-or-nothing delivery

---

## Shape Up (Basecamp Method)

### Overview
A unique approach focusing on 6-week cycles with cool-down periods.

### Core Concepts

**Shaping**
- Senior team shapes work upfront
- Creates pitch with problem, appetite, solution, risks
- Rough scope, not detailed specs
- Defines boundaries

**Betting**
- Every 6 weeks, decide what to work on
- Bet on pitched work
- No backlog of old ideas (if important, it'll come back)
- Small team owns entire project

**Building**
- Team has full 6 weeks
- No interruptions or distractions
- Team figures out details
- Shows progress with hill charts
- Ship or don't ship at end

**Cool-down**
- 2 weeks between cycles
- Fix bugs, refactor, explore ideas
- No scheduled work
- Recharge

### Key Differences from Scrum
- Fixed time (6 weeks), flexible scope
- No daily standups
- No sprints or velocity tracking
- Senior people shape work upfront
- Teams own entire project end-to-end

### When to Use
- Product development teams
- Need for focused, uninterrupted work
- Senior team can shape effectively
- Comfortable with variable scope

---

## Extreme Programming (XP)

### Core Practices

**Technical Practices**
- Pair programming
- Test-driven development (TDD)
- Continuous integration
- Refactoring
- Simple design
- Collective code ownership

**Team Practices**
- Sit together
- Whole team
- Informative workspace
- Sustainable pace

**Planning Practices**
- User stories
- Weekly/quarterly cycles
- Slack in schedule
- Stories estimated in ideal days

### When to Use
- High code quality requirements
- Rapidly changing requirements
- Need for technical excellence
- Close customer collaboration

---

## Choosing a Methodology

### Decision Matrix

| Factor | Scrum | Kanban | SAFe | Scrumban | Waterfall |
|--------|-------|--------|------|----------|-----------|
| Team Size | 3-9 | Any | 50+ | 3-15 | Any |
| Requirements Stability | Medium | Any | Medium | Low | High |
| Complexity | High | Medium | Very High | Medium | Low |
| Customer Involvement | High | Medium | Medium | Medium | Low |
| Delivery Frequency | Sprint end | Continuous | PI end | Continuous | Project end |
| Change Tolerance | High | Very High | Medium | Very High | Low |

### Questions to Ask

1. **How stable are requirements?**
   - Stable → Waterfall
   - Changing → Agile

2. **How large is the organization?**
   - Single team → Scrum/Kanban
   - Multiple teams → SAFe/LeSS

3. **What's the work type?**
   - Projects → Scrum
   - Flow/Support → Kanban
   - Both → Scrumban

4. **What's the team maturity?**
   - New to agile → Start with Scrum
   - Mature → Kanban or Shape Up

5. **What are regulatory requirements?**
   - Heavy documentation → Waterfall or hybrid

6. **What's the delivery cadence?**
   - Regular releases → Scrum
   - Continuous → Kanban

### Hybrid Approaches

Don't be dogmatic. Mix and match based on needs:
- Scrum with Kanban WIP limits
- Waterfall with agile development phase
- SAFe with Scrumban at team level
- Core Scrum with XP practices

The best methodology is the one that works for your team, organization, and project context.
