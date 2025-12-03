# PERSONALIZED GREETINGS AGENT - PRD

**Version:** 1.0
**Date:** 2025-11-23
**Status:** Ready for Development
**Product Owner:** Product Strategy Team

---

## Executive Summary

The Personalized Greetings Agent is an AI-powered motivational feedback system that adds personalized, persona-based greetings to student homework grades. By leveraging different communication styles based on grade ranges (0-50%, 51-70%, 71-90%, 91-100%), the agent provides contextually appropriate encouragement from four distinct personalities: Dudi Amsalem (tough love), Benjamin Netanyahu (diplomatic), Shahar Hasson (tech mentor), and Donald Trump (celebratory). This transforms cold numerical grades into engaging, motivational feedback that drives student improvement.

**Core Value:** Transform automated grading into personalized, motivational feedback that encourages struggling students, recognizes good work, and celebrates excellence - all while maintaining instructor efficiency.

**Position in Workflow:**
- **Agent 1 (GmailAgent):** Exports homework emails to Excel with repository URLs
- **Agent 2 (Repository Analyzer):** Analyzes repos, calculates grades, outputs graded Excel
- **Agent 3 (Personalized Greetings - NEW):** Adds motivational greetings based on grades

---

## Problem Statement

### User Problem

**Who:** Course instructors who want to provide personalized, motivational feedback to students but lack the time to write individual messages for 30+ students.

**What:** "I've automated my grading with the Repository Analyzer, which saves me hours. But now my feedback is just numbers - there's no personal touch, no encouragement for struggling students, no celebration for top performers. I want to motivate my students with personalized feedback, but writing 30 individual messages takes another hour. I need a way to add meaningful, grade-appropriate encouragement automatically."

**Why it matters:** Students respond better to personalized feedback than raw numbers. Motivational messaging can:
- Encourage struggling students to seek help and improve (0-50% range)
- Push average students to strive for excellence (51-70% range)
- Validate good performers and encourage consistency (71-90% range)
- Celebrate and reinforce outstanding achievement (91-100% range)

### Business Problem

- **Engagement gap:** Automated grading lacks the human touch that drives student motivation
- **Time constraint:** Instructors can't write personalized feedback for 30+ students (1-2 hours)
- **Inconsistency:** Manual feedback quality varies based on instructor fatigue
- **Scalability:** Personalized feedback doesn't scale beyond small class sizes
- **Educational impact:** Generic "Good job" or "Needs improvement" messages have minimal motivational value

### Educational Context

Research shows that personalized feedback improves:
- Student engagement (30-40% increase)
- Intrinsic motivation (students want to improve, not just get grades)
- Growth mindset (feedback focused on effort and improvement)
- Instructor-student relationship (students feel seen and valued)

However, this typically requires 2-3 minutes per student for quality feedback = 60-90 minutes for a class of 30.

---

## Goals & Success Metrics

### Objectives

1. **Primary:** Automate personalized motivational feedback for 30 students in <2 minutes (vs. 60-90 minutes manual)
2. **Secondary:** Achieve 85%+ student satisfaction with feedback quality ("felt personalized and helpful")
3. **Tertiary:** Increase student engagement metrics (re-submission rate, office hours attendance)

### North Star Metric

**Student Engagement with Feedback:** Percentage of students who report that feedback was "motivating and helpful" (Target: 85%+)

### Success Metrics

| Metric | Baseline | Target | Timeline | Measurement |
|--------|----------|--------|----------|-------------|
| **Time to Add Feedback** | 60-90 min | <2 min | Launch | Stopwatch timing |
| **Student Satisfaction** | N/A (no feedback) | 85%+ "motivating" | Week 4 | Student survey |
| **Feedback Appropriateness** | N/A | 90%+ contextually correct | Launch | Instructor review sample |
| **Persona Accuracy** | N/A | 95%+ match personality | Launch | Manual review |
| **Re-submission Rate** | 15% | 30% | Month 3 | Track improved submissions |
| **Instructor Adoption** | 0 | 90% of users | Month 2 | Usage logs |

### Key Performance Indicators (KPIs)

**Leading Indicators:**
- Greetings generated per session
- Average generation time per greeting (<3 seconds)
- Persona distribution (matches grade distribution)

**Lagging Indicators:**
- Student feedback sentiment (survey responses)
- Instructor retention (using tool for 3+ assignments)
- Student performance improvement (grades increase after feedback)
- Net Promoter Score from instructors

---

## Target Users

### Primary User Persona

**Professor Sarah Chen - Computer Science Instructor**
(Same persona from Repository Analyzer PRD)

**Additional Context for Greetings Agent:**

**Goals:**
- Provide motivational feedback that feels personal, not robotic
- Encourage struggling students without demotivating them
- Celebrate excellence to reinforce positive behavior
- Maintain consistent feedback quality across all students
- Save time while maintaining high educational standards

**Pain Points:**
- Automated grades feel cold and impersonal
- Can't afford 60-90 minutes to write individual feedback
- Generic "Good job!" messages feel insincere
- Struggling students need encouragement, but time is limited
- Top performers deserve recognition beyond just a number

**Desired Outcome:**
"I want my students to feel seen and motivated, whether they got 45% or 95%. I need feedback that's appropriate to their performance - tough love for those who need a wake-up call, celebration for top performers, and everything in between."

### Secondary Users

- Teaching Assistants providing feedback on behalf of instructors
- Bootcamp instructors with high student volume
- Online course creators scaling personalized feedback
- Department heads standardizing feedback quality

---

## Scope

### In Scope (v1.0 - MVP)

**Core Functionality:**
- Read Excel file from Repository Analyzer (`homework_emails_graded.xlsx`)
- Parse Grade column to determine grade range (0-50%, 51-70%, 71-90%, 91-100%)
- Generate personalized greeting using AI persona skills:
  - **Dudi Amsalem** (0-50%): Direct, tough love, motivational
  - **Benjamin Netanyahu** (51-70%): Diplomatic, constructive, formal
  - **Shahar Hasson** (71-90%): Tech mentor, encouraging, specific
  - **Donald Trump** (91-100%): Enthusiastic, superlatives, celebratory
- Add "Personalized Greeting" column to Excel
- Output enhanced Excel: `homework_emails_with_greetings.xlsx`
- Handle edge cases (no grade, failed repos, 0% grades)

**AI Skills/Personas (4 total):**
1. `dudi_amsalem_skill.md` - Tough love for 0-50%
2. `netanyahu_skill.md` - Diplomatic for 51-70%
3. `shahar_hasson_skill.md` - Tech mentor for 71-90%
4. `trump_skill.md` - Celebratory for 91-100%

**Technical:**
- Claude API integration for greeting generation
- Excel I/O with openpyxl
- CLI interface (click)
- Persona prompt engineering
- Grade range detection logic
- Progress tracking for 30 greetings
- Error handling (API failures, malformed grades)

**Cultural Considerations:**
- Respectful portrayal of real public figures
- Educational value over entertainment
- Avoid offensive or inappropriate content
- Greetings focus on student performance, not politics
- Personality styles are caricatures, not exact impersonations

### Out of Scope (Future Versions)

**v1.1** (Next 3 months):
- Custom persona creation (instructors define their own)
- Multiple language support (Hebrew, Spanish, etc.)
- Adjustable grade range thresholds (e.g., 0-40%, 40-70%, 70-85%, 85-100%)
- Greeting length control (short, medium, long)
- Tone adjustment (gentle vs. assertive)
- Student name personalization (use name from email)

**v2.0** (Next 6 months):
- Historical context (reference previous assignments)
- Improvement tracking ("Your grade improved from 60% to 85%!")
- Custom instructor personas (create persona from instructor's style)
- Multi-student comparison ("Top 10% of class!")
- Integration with LMS (Canvas, Blackboard)
- Automated email sending with greetings

**v3.0** (Future):
- AI-generated motivational action plans ("Here's how to improve...")
- Sentiment analysis (adjust tone based on student history)
- Video/audio greetings (text-to-speech with persona voices)
- Interactive feedback (students can respond)
- Peer comparison anonymized ("You're in the top third!")

### MVP Definition

**Minimum Viable Version** includes:
- Read graded Excel successfully
- Generate 1 greeting per grade range (4 total test cases)
- Persona prompts produce appropriate style
- Output Excel with Personalized Greeting column
- Handle API failures gracefully

**Success Criteria:**
- Processes 30 students in <2 minutes
- Greetings match persona style (95%+ manual review)
- No inappropriate content (100% safe for educational use)
- Instructors rate quality 4/5 or higher

---

## User Stories

### Epic 1: Excel Input Processing

**User Story 1.1: Read Graded Excel from Repository Analyzer**
```
As an instructor
I want to load the graded Excel file from Repository Analyzer
So that I can add personalized greetings to existing grades

Acceptance Criteria:
- Given Excel file with columns [ID, Date, Subject, URL, Grade, Total Files, Files <130, Total Lines, Status, Error Message]
- When I run the greetings agent with that file
- Then all rows with valid grades are identified
- And rows with errors (no grade) are flagged for skip or default greeting
- And the row count matches the input file

Priority: CRITICAL
Effort: 2 points
```

**User Story 1.2: Parse Grade Values**
```
As the system
I want to parse grade values and determine grade ranges
So that I can select the appropriate persona for each student

Acceptance Criteria:
- Given a grade value (e.g., "80.00", "45.50", "100.00")
- When I parse and categorize it
- Then I correctly identify the range:
  - 0-50%: Dudi Amsalem persona
  - 51-70%: Netanyahu persona
  - 71-90%: Shahar Hasson persona
  - 91-100%: Trump persona
- And handle edge cases:
  - 50.00 → Dudi Amsalem (inclusive)
  - 70.00 → Netanyahu (inclusive)
  - 90.00 → Shahar Hasson (inclusive)
  - 100.00 → Trump
  - 0.00 → Dudi Amsalem
  - No grade/Error → Default encouraging message

Priority: CRITICAL
Effort: 2 points
```

### Epic 2: AI Persona Skills

**User Story 2.1: Create Dudi Amsalem Skill (0-50%)**
```
As an instructor
I want struggling students (0-50%) to receive tough love feedback
So that they understand the severity and are motivated to improve

Acceptance Criteria:
- Given a grade of 0-50%
- When the Dudi Amsalem skill generates a greeting
- Then it includes:
  - Direct acknowledgment of poor performance
  - No sugarcoating, but respectful
  - Clear expectation to improve
  - Confidence that student can do better
  - Motivational push to action
- And avoids:
  - Being mean or demeaning
  - Political references
  - Offensive language
- Example tone: "Listen, 45%? We need to talk. This isn't good enough.
  I've seen worse, but not by much. Time to stop making excuses and start
  making progress. You can do better - I know it. Now get to work!"

Priority: CRITICAL
Effort: 5 points (includes prompt engineering and testing)

Persona Characteristics:
- Style: Direct, blunt, no-nonsense
- Sentiment: Tough but supportive
- Vocabulary: Simple, forceful, action-oriented
- Tone: Serious, commanding, expectant
```

**User Story 2.2: Create Benjamin Netanyahu Skill (51-70%)**
```
As an instructor
I want average-performing students (51-70%) to receive diplomatic encouragement
So that they feel supported and motivated to reach the next level

Acceptance Criteria:
- Given a grade of 51-70%
- When the Netanyahu skill generates a greeting
- Then it includes:
  - Formal, diplomatic acknowledgment of effort
  - Recognition of progress
  - Constructive guidance for improvement
  - Gravitas and seriousness
  - Forward-looking perspective
- And avoids:
  - Political policy references
  - Controversial statements
  - Condescension
- Example tone: "Your current performance stands at 65%. This represents
  a foundation upon which we can build. I encourage you to refine your
  approach and strive for greater excellence. The path to improvement
  requires dedication and focus. I have confidence in your ability to rise
  to this challenge."

Priority: CRITICAL
Effort: 5 points

Persona Characteristics:
- Style: Formal, diplomatic, measured
- Sentiment: Constructive, authoritative
- Vocabulary: Sophisticated, political rhetoric
- Tone: Serious, statesman-like, encouraging
```

**User Story 2.3: Create Shahar Hasson Skill (71-90%)**
```
As an instructor
I want good-performing students (71-90%) to receive tech mentor encouragement
So that they feel validated and inspired to reach excellence

Acceptance Criteria:
- Given a grade of 71-90%
- When the Shahar Hasson skill generates a greeting
- Then it includes:
  - Warm recognition of good work
  - Specific, actionable feedback
  - Tech industry perspective
  - Encouragement to push for excellence
  - Mentorship tone (peer-to-peer)
- And avoids:
  - Generic "good job" messages
  - Tech jargon without educational value
  - Complacency ("you're done")
- Example tone: "Hey, 85% - that's solid work! You're clearly getting the
  concepts and your code shows good structure. This is the kind of foundation
  that leads to great things in tech. Want to hit that 90%+? Focus on
  breaking down those larger files even more. You're almost there - keep
  pushing!"

Priority: CRITICAL
Effort: 5 points

Persona Characteristics:
- Style: Conversational, mentor-like, specific
- Sentiment: Encouraging, validating, aspirational
- Vocabulary: Tech-friendly, modern, relatable
- Tone: Warm, supportive, growth-focused
```

**User Story 2.4: Create Donald Trump Skill (91-100%)**
```
As an instructor
I want top-performing students (91-100%) to receive enthusiastic celebration
So that they feel proud and their excellence is reinforced

Acceptance Criteria:
- Given a grade of 91-100%
- When the Trump skill generates a greeting
- Then it includes:
  - Superlatives and enthusiastic language
  - Celebration of achievement
  - Reinforcement of excellence
  - Confidence-building
  - Encouragement to maintain high standards
- And avoids:
  - Political policy or controversial statements
  - Excessive exaggeration (stay educational)
  - Inappropriate content
- Example tone: "TREMENDOUS work! 95%! This is what I call WINNING!
  You're doing an absolutely FANTASTIC job - the best! Your code organization
  is excellent, really excellent. Keep it up, you're going to be HUGE in this
  field. AMAZING achievement!"

Priority: CRITICAL
Effort: 5 points

Persona Characteristics:
- Style: Enthusiastic, superlative-heavy, celebratory
- Sentiment: Extremely positive, confident
- Vocabulary: Superlatives, business language, winning
- Tone: Energetic, proud, encouraging
```

### Epic 3: Greeting Generation

**User Story 3.1: Generate Greeting via Claude API**
```
As the system
I want to generate personalized greetings using Claude API
So that each greeting is unique and contextually relevant

Acceptance Criteria:
- Given a student's grade and selected persona skill
- When I call Claude API with the persona prompt
- Then the API returns a personalized greeting (50-150 words)
- And the greeting references the specific grade
- And the style matches the persona
- And generation takes <3 seconds per greeting
- And API errors are handled gracefully (retry 3x, fallback to template)

Priority: CRITICAL
Effort: 5 points

Technical Requirements:
- Use Claude API (Anthropic SDK)
- Pass grade value to prompt
- Prompt engineering for consistency
- Temperature: 0.7 (balance creativity and consistency)
- Max tokens: 200
- Retry logic: 3 attempts with exponential backoff
```

**User Story 3.2: Ensure Greeting Quality**
```
As an instructor
I want all generated greetings to be appropriate and high-quality
So that I can confidently share them with students

Acceptance Criteria:
- Given any generated greeting
- When I review it
- Then it meets quality standards:
  - No offensive or inappropriate content
  - Grade-appropriate encouragement
  - Matches persona style
  - Educational and motivational
  - Proper grammar and spelling
  - References the specific grade
  - 50-150 words (not too long or short)
- And has content filtering:
  - No profanity
  - No political controversies
  - No personal attacks
  - No stereotypes or discrimination

Priority: HIGH
Effort: 3 points

Validation Strategy:
- Keyword blocklist check
- Sentiment analysis (ensure appropriate tone)
- Length validation
- Manual review sample (first 5 of each persona)
```

### Epic 4: Excel Output Generation

**User Story 4.1: Add Personalized Greeting Column**
```
As an instructor
I want a new Excel column with personalized greetings
So that I can review and send feedback to students

Acceptance Criteria:
- Given graded Excel and generated greetings
- When I generate output
- Then new Excel includes all original columns PLUS:
  - "Personalized Greeting" column (new, after Error Message)
- And greeting text is properly formatted (no truncation)
- And column width is auto-sized for readability
- And row order matches input order
- And original data is preserved exactly

Output Columns:
1. ID
2. Date
3. Subject
4. URL
5. Grade
6. Total Files
7. Files <130
8. Total Lines
9. Status
10. Error Message
11. **Personalized Greeting** (NEW)

Priority: CRITICAL
Effort: 3 points
```

**User Story 4.2: Handle Edge Cases in Output**
```
As the system
I want to handle edge cases gracefully in output
So that the Excel is complete even for failed repos

Acceptance Criteria:
- Given rows with errors (Status = "Error", no grade)
- When I generate greetings
- Then for error rows:
  - Greeting column shows: "No grade available - please review repository error."
  - OR: Default encouraging message: "Keep trying! Reach out if you need help with your submission."
- And for 0% grades:
  - Use Dudi Amsalem persona (not error message)
- And for missing/null grades:
  - Use default placeholder message
- And Excel is always valid (no blank required cells)

Priority: HIGH
Effort: 2 points
```

### Epic 5: CLI Interface

**User Story 5.1: Simple CLI for Greetings Generation**
```
As an instructor
I want a simple command to add greetings to my graded Excel
So that I can complete the workflow easily

Acceptance Criteria:
- Given a command like:
  `greetings-agent generate --input homework_emails_graded.xlsx`
- When I run it
- Then the tool:
  - Reads graded Excel
  - Generates personalized greetings for all students
  - Outputs to: homework_emails_with_greetings.xlsx
  - Shows progress: [15/30 greetings generated]
  - Displays completion message with file location
  - Completes in <2 minutes for 30 students

CLI Options:
--input, -i: Input Excel file (required)
--output, -o: Output Excel file (optional, auto-generated if not specified)
--verbose, -v: Show detailed logs
--help: Display usage information

Priority: CRITICAL
Effort: 3 points
```

**User Story 5.2: Progress Tracking**
```
As an instructor
I want to see real-time progress while greetings are generated
So that I know the tool is working and how long to wait

Acceptance Criteria:
- Given a greetings generation session in progress
- When I watch the console output
- Then I see:
  - "Generating personalized greetings for 30 students..."
  - Progress bar: [████████------] 15/30 (50%) - ETA: 45s
  - Per-student status: "✓ Student 1 (85%): Shahar Hasson greeting"
  - API errors: "⚠ Student 5: API timeout, retrying..."
  - Final summary: "Completed: 30/30 greetings in 1 minute 23 seconds"
  - Output location: "Saved to: output/homework_emails_with_greetings.xlsx"

Priority: MEDIUM
Effort: 3 points
```

### Epic 6: Error Handling & Reliability

**User Story 6.1: Handle API Failures Gracefully**
```
As the system
I want to handle Claude API failures without crashing
So that the tool is reliable even with network issues

Acceptance Criteria:
- Given API failures (timeout, rate limit, network error)
- When generating greetings
- Then the system:
  - Retries 3 times with exponential backoff (1s, 2s, 4s)
  - Falls back to template greeting if all retries fail
  - Logs the error for debugging
  - Continues processing remaining students
  - Reports API failure count in summary

Fallback Templates:
- 0-50%: "Your grade is [X]%. This needs significant improvement. Let's work together to get you on track. Don't hesitate to reach out for help."
- 51-70%: "You scored [X]%. Good effort, but there's room for improvement. Focus on refining your code structure and you'll reach the next level."
- 71-90%: "Great work with [X]%! You're demonstrating strong understanding. Keep pushing for excellence - you're almost at the top!"
- 91-100%: "Excellent work! [X]% shows mastery of the concepts. Keep up this outstanding performance!"

Priority: HIGH
Effort: 4 points
```

**User Story 6.2: Validate Input Excel Structure**
```
As the system
I want to validate the input Excel before processing
So that I catch errors early and provide helpful guidance

Acceptance Criteria:
- Given an input Excel file
- When I validate it
- Then I check:
  - File exists and is readable
  - Has required columns: Grade (minimum)
  - Grade column contains parseable numbers or "N/A"
  - At least one row with valid grade
- And if validation fails:
  - Display clear error message
  - Suggest fix (e.g., "Missing 'Grade' column. Expected Excel from Repository Analyzer.")
  - Exit gracefully (no crash)
- And if validation succeeds:
  - Show summary: "Found 30 students with grades, 2 with errors"
  - Prompt for confirmation to proceed

Priority: HIGH
Effort: 3 points
```

---

## Functional Requirements

### FR-1: Excel Input Processing

**Description:** Read and parse graded Excel from Repository Analyzer

**Inputs:**
- Excel file path: `homework_emails_graded.xlsx`
- Expected columns: ID, Date, Subject, URL, Grade, Total Files, Files <130, Total Lines, Status, Error Message

**Processing:**
1. Validate file exists and is .xlsx format
2. Open with openpyxl
3. Read "Graded Results" sheet
4. Validate required column "Grade" exists
5. Parse each row:
   - Extract Grade value (string → float)
   - Handle errors (Status = "Error" → no grade)
   - Handle edge cases (0.00, 100.00, null)
6. Create list of students with parsed grades

**Outputs:**
- List of student records: `[{id, grade, row_index}, ...]`
- Validation summary: count of valid grades, errors
- Warning messages for malformed data

**Business Logic:**
```python
def parse_grade(grade_value):
    """Parse grade string to float"""
    if grade_value is None or grade_value == "":
        return None  # No grade

    # Remove percentage sign if present
    if isinstance(grade_value, str):
        grade_value = grade_value.replace("%", "").strip()

    try:
        grade = float(grade_value)
        return grade
    except ValueError:
        return None  # Invalid grade
```

**Acceptance Criteria:**
- Successfully reads Repository Analyzer Excel
- Handles missing/invalid grades gracefully
- Preserves all original data
- Validates before expensive AI operations

---

### FR-2: Grade Range Detection

**Description:** Categorize grade into persona range (0-50%, 51-70%, 71-90%, 91-100%)

**Inputs:**
- Grade value (float, 0.00 to 100.00)

**Processing:**
1. Check if grade is None/null → Return "no_grade"
2. Categorize based on ranges:
   - 0.00 ≤ grade ≤ 50.00 → "dudi_amsalem" (tough love)
   - 50.01 ≤ grade ≤ 70.00 → "netanyahu" (diplomatic)
   - 70.01 ≤ grade ≤ 90.00 → "shahar_hasson" (tech mentor)
   - 90.01 ≤ grade ≤ 100.00 → "trump" (celebratory)
3. Return persona identifier

**Outputs:**
- Persona identifier (string): "dudi_amsalem" | "netanyahu" | "shahar_hasson" | "trump" | "no_grade"

**Business Logic:**
```python
def determine_persona(grade: float) -> str:
    """Determine which persona to use based on grade"""
    if grade is None:
        return "no_grade"

    if 0 <= grade <= 50:
        return "dudi_amsalem"
    elif 50 < grade <= 70:
        return "netanyahu"
    elif 70 < grade <= 90:
        return "shahar_hasson"
    elif 90 < grade <= 100:
        return "trump"
    else:
        # Out of range (shouldn't happen)
        return "no_grade"
```

**Edge Cases:**
- Exactly 50.00 → dudi_amsalem (lower bound inclusive)
- Exactly 70.00 → netanyahu (lower bound inclusive)
- Exactly 90.00 → shahar_hasson (lower bound inclusive)
- Exactly 0.00 → dudi_amsalem (valid grade, just very low)
- Exactly 100.00 → trump (perfect score)
- Grade > 100.00 → treat as 100.00 (shouldn't happen in normal flow)
- Grade < 0.00 → treat as error (shouldn't happen in normal flow)

**Acceptance Criteria:**
- Correct categorization for all valid grades
- Handles edge cases (0, 50, 70, 90, 100)
- Returns clear identifier for each persona
- Handles null/missing grades

---

### FR-3: AI Persona Skill Prompts

**Description:** Engineered prompts for each persona to generate consistent, appropriate greetings

#### Persona 1: Dudi Amsalem (0-50%)

**Skill File:** `skills/dudi_amsalem_skill.md`

**System Prompt:**
```markdown
You are Dudi Amsalem, an Israeli politician known for your direct, no-nonsense communication style.

You are providing feedback to a student who scored {grade}% on their homework assignment - a very low grade that indicates serious issues with their work.

Your role is to:
- Be direct and honest about the poor performance (no sugarcoating)
- Show that you expect better and know they can do better
- Provide tough love - firm but ultimately supportive
- Motivate them to take immediate action to improve
- Avoid being mean or demeaning - be tough but respectful

Style Guidelines:
- Use simple, forceful language
- Be blunt but not cruel
- Express confidence they can improve
- Create urgency (this needs to change NOW)
- Keep it 50-100 words
- Focus on action and accountability

IMPORTANT CONSTRAINTS:
- NO political references or policy discussions
- NO offensive language or personal attacks
- Focus ONLY on the academic performance
- Be tough but educational, not demotivating
- This is for educational purposes

Generate a personalized greeting for this student.
```

**Example Output:**
```
Listen, {grade}%? We need to talk. This isn't good enough - not even close.
I've seen students struggle before, but you're not putting in the work. Time to
stop making excuses and start making real progress. I know you can do better
than this. Now get serious, seek help if you need it, and show me what you're
actually capable of. Let's go.
```

#### Persona 2: Benjamin Netanyahu (51-70%)

**Skill File:** `skills/netanyahu_skill.md`

**System Prompt:**
```markdown
You are Benjamin Netanyahu, Prime Minister of Israel, known for your formal, diplomatic, and measured communication style.

You are providing feedback to a student who scored {grade}% on their homework assignment - a decent but not excellent grade that shows room for improvement.

Your role is to:
- Acknowledge the effort and foundation they've built
- Provide constructive, diplomatic encouragement
- Speak with gravitas and seriousness
- Encourage them to strive for excellence
- Use formal, sophisticated language

Style Guidelines:
- Formal, statesman-like tone
- Diplomatic and measured
- Use sophisticated vocabulary
- Forward-looking and constructive
- Express confidence in their potential
- Keep it 60-120 words
- Focus on refinement and progress

IMPORTANT CONSTRAINTS:
- NO political policy references
- NO controversial political statements
- Focus ONLY on academic performance
- Be diplomatic and encouraging, not condescending
- This is for educational purposes

Generate a personalized greeting for this student.
```

**Example Output:**
```
Your performance stands at {grade}%. This represents a solid foundation upon
which we can build something greater. I recognize the effort you have invested,
and I see potential for advancement. The path to excellence requires dedication,
refinement of technique, and unwavering focus on your objectives. I have
confidence in your ability to rise to this challenge and achieve the higher
standards you are capable of reaching. Continue forward with determination.
```

#### Persona 3: Shahar Hasson (71-90%)

**Skill File:** `skills/shahar_hasson_skill.md`

**System Prompt:**
```markdown
You are Shahar Hasson, an Israeli tech influencer and educator known for your encouraging, mentor-like communication style.

You are providing feedback to a student who scored {grade}% on their homework assignment - good work that shows strong understanding, but with room to reach excellence.

Your role is to:
- Warmly acknowledge their good performance
- Provide specific, actionable encouragement
- Speak as a mentor/peer in the tech industry
- Inspire them to push for that top-tier excellence
- Be conversational and relatable

Style Guidelines:
- Warm, encouraging tone
- Conversational but professional
- Use tech industry perspective
- Provide specific validation
- Growth mindset focused
- Keep it 60-120 words
- Balance validation with aspiration

IMPORTANT CONSTRAINTS:
- NO generic "good job" - be specific
- Focus on code quality and learning
- Be encouraging, not complacent
- This is for educational purposes
- Keep tech references educational, not jargon-heavy

Generate a personalized greeting for this student.
```

**Example Output:**
```
Hey, {grade}% - that's solid work! You're clearly getting the concepts, and your
code structure shows you understand what good organization looks like. This is
exactly the kind of foundation that leads to great things in the tech world.
You're in that sweet spot where you're doing well, but there's still room to
level up to truly excellent. Want to hit that 90%+? Focus on breaking down
those larger files even more and keep refining your approach. You're almost
there - keep pushing!
```

#### Persona 4: Donald Trump (91-100%)

**Skill File:** `skills/trump_skill.md`

**System Prompt:**
```markdown
You are Donald Trump, known for your enthusiastic, superlative-filled communication style.

You are providing feedback to a student who scored {grade}% on their homework assignment - outstanding, top-tier performance that deserves celebration.

Your role is to:
- Celebrate their excellent achievement enthusiastically
- Use superlatives and energetic language
- Build their confidence and reinforce excellence
- Encourage them to maintain these high standards
- Be positive and motivating

Style Guidelines:
- Enthusiastic, energetic tone
- Use superlatives (TREMENDOUS, FANTASTIC, AMAZING, WINNING)
- Celebratory and confident
- Short, punchy sentences
- Lots of exclamation marks (but not excessive)
- Keep it 50-100 words
- Focus on achievement and excellence

IMPORTANT CONSTRAINTS:
- NO political statements or policy references
- NO controversial content
- Focus ONLY on academic achievement
- Be celebratory and educational
- Keep it appropriate for educational context
- Don't overdo it - stay genuine

Generate a personalized greeting for this student.
```

**Example Output:**
```
TREMENDOUS work! {grade}%! This is what I call WINNING! You're doing an
absolutely FANTASTIC job - really, the best! Your code organization is excellent,
just excellent. This is top-tier work, the kind of quality that leads to big
success in tech. Keep it up, maintain these high standards, and you're going to
go far - I mean really far. AMAZING achievement!
```

---

### FR-4: Greeting Generation via Claude API

**Description:** Generate personalized greetings using Claude API with persona prompts

**Inputs:**
- Student grade (float)
- Persona identifier (string)
- Persona skill prompt (loaded from skills/)

**Processing:**
1. Load appropriate persona skill file
2. Inject grade value into prompt: `{grade}` → actual grade
3. Call Claude API:
   - Model: claude-sonnet-4-5-20250929 (latest)
   - Temperature: 0.7 (balance creativity and consistency)
   - Max tokens: 200 (50-150 word greetings)
   - System prompt: persona skill content
   - User prompt: "Generate a personalized greeting for this student."
4. Retry logic: 3 attempts with exponential backoff (1s, 2s, 4s)
5. Validate output:
   - Length: 10-300 words
   - No offensive content (keyword blocklist check)
   - Contains grade reference (optional but preferred)
6. Return greeting text

**Outputs:**
- Personalized greeting (string, 50-150 words)
- Generation status (success/fallback/error)
- Error message (if failed)

**API Configuration:**
```python
import anthropic

client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

def generate_greeting(grade: float, persona: str) -> str:
    """Generate personalized greeting using Claude API"""

    # Load persona prompt
    prompt = load_persona_prompt(persona)
    prompt = prompt.replace("{grade}", str(grade))

    # Call Claude API
    try:
        message = client.messages.create(
            model="claude-sonnet-4-5-20250929",
            max_tokens=200,
            temperature=0.7,
            system=prompt,
            messages=[
                {"role": "user", "content": "Generate a personalized greeting for this student."}
            ]
        )

        greeting = message.content[0].text
        return greeting

    except Exception as e:
        # Retry logic or fallback
        return get_fallback_greeting(grade, persona)
```

**Performance:**
- Target: <3 seconds per greeting
- Batch processing: Process 5-10 at a time (rate limits)
- Total time for 30 students: <2 minutes

**Error Handling:**
- API timeout → Retry 3x, then fallback
- Rate limit → Wait and retry
- Authentication error → Exit with clear message
- Network error → Retry 3x, then fallback

**Acceptance Criteria:**
- Generates contextually appropriate greetings
- Matches persona style (95%+ manual review)
- No inappropriate content (100% safe)
- Handles API failures gracefully
- Completes 30 greetings in <2 minutes

---

### FR-5: Excel Output Generation

**Description:** Generate Excel with all original data plus Personalized Greeting column

**Inputs:**
- Original graded Excel data
- Generated greetings (list of strings)
- Output file path (optional, auto-generated if not provided)

**Processing:**
1. Create new Excel workbook
2. Copy "Graded Results" sheet from original
3. Add new column: "Personalized Greeting" (after Error Message)
4. Populate greeting values:
   - Match by row index
   - Handle errors (use default message)
5. Copy "Summary" sheet (unchanged)
6. Format new column:
   - Auto-size column width
   - Text wrap enabled (for multi-line greetings)
   - Alignment: Top-left
7. Save to output path

**Output Format:**

**Sheet 1: Graded Results (Enhanced)**
| ID | Date | Subject | URL | Grade | Total Files | Files <130 | Total Lines | Status | Error Message | **Personalized Greeting** |
|----|------|---------|-----|-------|-------------|------------|-------------|--------|---------------|-----------------------------|
| 1 | 2025-11-20 | HW1 | github.com/... | 85.00 | 5 | 4 | 469 | Success | - | "Hey, 85% - that's solid work!..." |
| 2 | 2025-11-20 | HW1 | github.com/... | 45.00 | 3 | 1 | 520 | Success | - | "Listen, 45%? We need to talk..." |
| 3 | 2025-11-20 | HW1 | github.com/... | 0.00 | 0 | 0 | 0 | Error | Repository not found | "No grade available - please review repository error." |

**Sheet 2: Summary (Unchanged)**
- Preserved exactly as from Repository Analyzer

**File Naming:**
- Input: `homework_emails_graded.xlsx`
- Output: `homework_emails_with_greetings.xlsx`
- Location: `output/` directory (auto-created if doesn't exist)

**Excel Formatting:**
```python
# Column configuration
columns = [
    "ID", "Date", "Subject", "URL", "Grade",
    "Total Files", "Files <130", "Total Lines",
    "Status", "Error Message",
    "Personalized Greeting"  # NEW
]

# Format Personalized Greeting column
greeting_col = ws['K']  # Column K
for cell in greeting_col:
    cell.alignment = Alignment(
        wrap_text=True,
        vertical='top',
        horizontal='left'
    )

# Auto-size columns
ws.column_dimensions['K'].width = 60  # Wide enough for greetings
```

**Acceptance Criteria:**
- Excel includes all original data + new column
- Greetings properly formatted (readable, wrapped)
- File opens correctly in Excel/Google Sheets
- Summary sheet preserved
- Output saved to correct location

---

## Non-Functional Requirements

### Performance

**Target Metrics:**
- **30 greetings**: <2 minutes total (including API calls)
- **Single greeting**: <3 seconds (API latency)
- **File I/O**: <5 seconds (read + write Excel)
- **Total end-to-end**: <2 minutes for typical class of 30

**Optimization Strategies:**
- Batch API calls if supported (future enhancement)
- Async processing for API calls (future enhancement)
- Cache persona prompts (load once, use many times)
- Efficient Excel operations (openpyxl)

### Reliability

**Target Metrics:**
- **API success rate**: 95%+ (with retries)
- **Fallback coverage**: 100% (every student gets greeting, even if API fails)
- **Excel output success**: 100% (never corrupt output)
- **Data preservation**: 100% (all original data intact)

**Reliability Strategies:**
- Retry logic for transient API failures (3x with backoff)
- Fallback templates when API unavailable
- Validate output before saving
- Atomic file operations (write to temp, then rename)

### Security & Privacy

**Considerations:**
- **API Key Security**: Store in environment variable, never commit to code
- **Student Data Privacy**: Process locally, don't send student names to API (only grades)
- **Content Safety**: Filter generated content for inappropriate language
- **Educational Appropriateness**: All greetings suitable for instructor-student context

**Content Filtering:**
```python
BLOCKED_WORDS = [
    # Profanity, offensive terms, etc.
    # (Actual list would be comprehensive)
]

def is_appropriate(greeting: str) -> bool:
    """Check if greeting is appropriate for educational use"""
    greeting_lower = greeting.lower()

    # Check blocklist
    for word in BLOCKED_WORDS:
        if word in greeting_lower:
            return False

    # Check length (not too short or too long)
    word_count = len(greeting.split())
    if word_count < 10 or word_count > 300:
        return False

    return True
```

### Usability

**CLI Design Principles:**
- Simple default usage (minimal required arguments)
- Clear progress feedback
- Helpful error messages
- Quick execution (<2 min)

**Example Usage:**
```bash
# Simplest usage (all defaults)
greetings-agent generate --input homework_emails_graded.xlsx

# With custom output
greetings-agent generate -i graded.xlsx -o with_feedback.xlsx

# Verbose mode
greetings-agent generate -i graded.xlsx -v
```

**Progress Output:**
```
Personalized Greetings Agent v1.0.0

Loading graded Excel: homework_emails_graded.xlsx
✓ Found 30 students with grades

Generating personalized greetings...
[██████████████████████] 30/30 (100%) - 1:23 elapsed

Persona Distribution:
  Dudi Amsalem (0-50%): 3 students
  Netanyahu (51-70%): 8 students
  Shahar Hasson (71-90%): 12 students
  Trump (91-100%): 7 students

✓ All greetings generated successfully
  API success: 30/30
  Fallbacks used: 0

Saving enhanced Excel...
✓ Output saved to: output/homework_emails_with_greetings.xlsx

Completed in 1 minute 23 seconds
```

### Compatibility

**Operating Systems:**
- Windows 10/11
- macOS 11+
- Linux (Ubuntu 20.04+)

**Python:**
- Python 3.8+
- Python 3.9, 3.10, 3.11 tested

**Dependencies:**
- openpyxl (Excel I/O)
- anthropic (Claude API)
- click (CLI)
- python-dotenv (env variables)

---

## Technical Design

### Architecture

```
┌─────────────────────────────────────────────────────────┐
│              CLI Interface (Click)                      │
│           greetings_agent/cli.py                        │
└────────────────────┬────────────────────────────────────┘
                     │
        ┌────────────▼────────────┐
        │   Main Orchestrator     │
        │   greetings_agent.py    │
        │   - Load Excel          │
        │   - Generate greetings  │
        │   - Save output         │
        └────┬────────────────┬───┘
             │                │
    ┌────────▼─────┐    ┌────▼──────────────┐
    │ Excel        │    │ Greeting          │
    │ Manager      │    │ Generator         │
    │ (openpyxl)   │    │ (Claude API)      │
    └──────────────┘    └────┬──────────────┘
                             │
                    ┌────────▼──────────┐
                    │  Persona Skills   │
                    │  (Prompt Files)   │
                    │  - dudi_amsalem   │
                    │  - netanyahu      │
                    │  - shahar_hasson  │
                    │  - trump          │
                    └───────────────────┘
```

### Data Flow

```
1. INPUT
   homework_emails_graded.xlsx
   (from Repository Analyzer)
   ↓
2. PARSE GRADES
   Extract grade column → categorize into ranges
   ↓
3. GENERATE GREETINGS (for each student)
   ├─ Determine persona (based on grade range)
   ├─ Load persona skill prompt
   ├─ Call Claude API with prompt + grade
   ├─ Validate greeting (length, appropriateness)
   ├─ Retry if failed (3x) or use fallback
   └─ Store greeting
   ↓
4. OUTPUT GENERATION
   Create new Excel with original data + greetings
   ↓
5. SAVE
   homework_emails_with_greetings.xlsx
   (in output/ directory)
```

### Core Modules

#### Module: excel_manager.py
**Purpose:** Read/write Excel files

```python
class ExcelManager:
    def read_graded_excel(self, file_path: str) -> List[Dict]:
        """Read graded Excel from Repository Analyzer"""
        # Open workbook
        # Read "Graded Results" sheet
        # Extract rows with grades
        # Return list of student records

    def write_with_greetings(self,
                            original_data: List[Dict],
                            greetings: List[str],
                            output_path: str):
        """Write Excel with greetings column"""
        # Create new workbook
        # Copy original data
        # Add "Personalized Greeting" column
        # Copy Summary sheet
        # Format and save
```

#### Module: greeting_generator.py
**Purpose:** Generate personalized greetings via Claude API

```python
class GreetingGenerator:
    def __init__(self, api_key: str):
        self.client = anthropic.Anthropic(api_key=api_key)
        self.persona_prompts = self._load_persona_prompts()

    def generate(self, grade: float) -> str:
        """Generate greeting for a grade"""
        # Determine persona
        # Load prompt
        # Call Claude API
        # Validate output
        # Return greeting

    def _determine_persona(self, grade: float) -> str:
        """Determine which persona based on grade"""
        if 0 <= grade <= 50:
            return "dudi_amsalem"
        elif 50 < grade <= 70:
            return "netanyahu"
        elif 70 < grade <= 90:
            return "shahar_hasson"
        elif 90 < grade <= 100:
            return "trump"
        else:
            return "no_grade"

    def _call_api(self, persona_prompt: str, grade: float) -> str:
        """Call Claude API with retry logic"""
        # Inject grade into prompt
        # Call API
        # Retry 3x on failure
        # Fallback if all retries fail
        # Return greeting

    def _validate_greeting(self, greeting: str) -> bool:
        """Validate greeting is appropriate"""
        # Check length
        # Check blocklist
        # Check sentiment (optional)
        # Return True/False
```

#### Module: persona_skills/ (Directory)
**Purpose:** Store persona skill prompts

```
persona_skills/
├── dudi_amsalem.md    # Tough love (0-50%)
├── netanyahu.md       # Diplomatic (51-70%)
├── shahar_hasson.md   # Tech mentor (71-90%)
├── trump.md           # Celebratory (91-100%)
└── fallback.md        # Default templates for API failures
```

Each file contains the system prompt for that persona.

#### Module: cli.py
**Purpose:** Command-line interface

```python
import click
from .greeting_agent import GreetingsAgent

@click.group()
def cli():
    """Personalized Greetings Agent"""
    pass

@cli.command()
@click.option('--input', '-i', required=True, help='Input graded Excel')
@click.option('--output', '-o', help='Output Excel (optional)')
@click.option('--verbose', '-v', is_flag=True, help='Verbose output')
def generate(input, output, verbose):
    """Generate personalized greetings"""
    agent = GreetingsAgent(verbose=verbose)
    agent.run(input_path=input, output_path=output)
```

### Technology Stack

**Language:** Python 3.8+

**Core Libraries:**
- `anthropic>=0.18.0` - Claude API client
- `openpyxl>=3.1.0` - Excel file I/O
- `click>=8.1.0` - CLI framework
- `python-dotenv>=1.0.0` - Environment variables
- `tqdm>=4.66.0` - Progress bars (optional)

**Standard Library:**
- `pathlib` - File path operations
- `os` - Environment variables
- `typing` - Type hints
- `logging` - Error logging
- `time` - Retry backoff

### Project Structure

```
EmailSkillAgents/
├── greetings_agent/              # Main package
│   ├── __init__.py              # Package initialization
│   ├── cli.py                   # CLI interface
│   ├── greeting_agent.py        # Main orchestrator
│   ├── excel_manager.py         # Excel I/O
│   ├── greeting_generator.py   # Claude API integration
│   ├── validators.py            # Content validation
│   └── persona_skills/          # Persona prompts
│       ├── dudi_amsalem.md
│       ├── netanyahu.md
│       ├── shahar_hasson.md
│       ├── trump.md
│       └── fallback.md
├── tests/                        # Test suite
│   ├── test_excel_manager.py
│   ├── test_greeting_generator.py
│   ├── test_validators.py
│   ├── test_integration.py
│   └── fixtures/
│       ├── sample_graded.xlsx
│       └── expected_output.xlsx
├── output/                       # Output directory
│   └── homework_emails_with_greetings.xlsx
├── .env.example                  # Example env file
├── requirements.txt              # Dependencies
├── setup.py                      # Package setup
├── README.md                     # User documentation
└── PRD-PersonalizedGreetingsAgent.md  # This document
```

### Environment Configuration

**.env file:**
```bash
# Claude API Key (required)
ANTHROPIC_API_KEY=sk-ant-xxxxxxxxxxxxx

# Optional configuration
GREETING_MODEL=claude-sonnet-4-5-20250929
GREETING_TEMPERATURE=0.7
GREETING_MAX_TOKENS=200
GREETING_TIMEOUT=30
```

---

## Implementation Plan

### Development Approach: Incremental MVP

**Philosophy:** Build persona prompts first, then integrate with Excel I/O

### Phase 1: Persona Engineering (Week 1)

**Goal:** Create and validate all 4 persona skills

**Tasks:**
- [ ] Research persona communication styles (study speeches, interviews)
- [ ] Write persona skill prompts (dudi_amsalem.md, netanyahu.md, shahar_hasson.md, trump.md)
- [ ] Test prompts manually with Claude API (via Claude.ai or API playground)
- [ ] Iterate prompts until style is consistent and appropriate
- [ ] Create fallback templates for each persona
- [ ] Review with 3 instructors for appropriateness

**Deliverable:**
```bash
# 4 working persona prompts that produce:
- Appropriate tone for grade range
- Consistent style (95%+ match personality)
- Educational and motivational content
- No inappropriate content (100% safe)
```

**Success Criteria:**
- Generate 10 greetings per persona (40 total)
- 95%+ match target personality (manual review)
- 100% appropriate for educational use
- Instructors rate quality 4/5 or higher

**Testing Method:**
```python
# Manual testing script
grades = [10, 25, 40, 50, 55, 60, 70, 75, 85, 90, 95, 100]

for grade in grades:
    persona = determine_persona(grade)
    greeting = generate_greeting(grade, persona)
    print(f"\n{grade}% ({persona}):\n{greeting}\n")

# Review output manually
# Iterate prompts until quality is consistent
```

### Phase 2: Foundation (Week 2)

**Goal:** Basic CLI that generates greetings for sample Excel

**Tasks:**
- [ ] Project setup (structure, dependencies, .gitignore)
- [ ] Excel manager module (read graded Excel)
- [ ] Greeting generator module (Claude API integration)
- [ ] Grade range detection logic
- [ ] Persona prompt loading (from skills/ directory)
- [ ] Simple CLI (generate command)
- [ ] Basic error handling (file not found, API key missing)

**Deliverable:**
```bash
greetings-agent generate --input sample_graded.xlsx
# Successfully generates greetings for 5 test students
# Outputs Excel with Personalized Greeting column
```

**Success Criteria:**
- Reads graded Excel correctly
- Categorizes grades into correct ranges
- Calls Claude API successfully
- Outputs Excel with greeting column
- Handles 1 error type (file not found)

### Phase 3: Robustness (Week 3)

**Goal:** Handle all error cases and edge cases

**Tasks:**
- [ ] API retry logic (3x with exponential backoff)
- [ ] Fallback templates (when API fails)
- [ ] Content validation (blocklist, length, appropriateness)
- [ ] Edge case handling (0%, 100%, no grade, errors)
- [ ] Input validation (check Excel structure)
- [ ] Logging (errors, API calls, generation stats)
- [ ] Progress tracking (console output, progress bar)

**Deliverable:**
- Handles all error scenarios gracefully
- Never crashes (even with API failures)
- Provides clear error messages
- Logs all operations for debugging

**Success Criteria:**
- Processes 30 students with mixed errors without crashing
- Falls back to templates when API unavailable
- 100% of students receive greeting (API or fallback)
- Error messages are clear and actionable

### Phase 4: Polish & UX (Week 4)

**Goal:** Professional user experience

**Tasks:**
- [ ] CLI improvements (help text, examples, version)
- [ ] Progress indicators (real-time status, ETA)
- [ ] Excel formatting (column width, text wrap, alignment)
- [ ] Summary statistics (persona distribution, API success rate)
- [ ] Output directory management (auto-create, custom path)
- [ ] User documentation (README, examples, troubleshooting)
- [ ] Installation guide (pip install, API key setup)

**Deliverable:**
- Professional CLI with excellent UX
- Polished Excel output
- Comprehensive README and documentation

**Success Criteria:**
- First-time users can run successfully without help
- Progress is clear and reassuring
- Output Excel is professional and readable
- Documentation is complete and clear

### Phase 5: Testing & Validation (Week 5)

**Goal:** Production-ready quality

**Tasks:**
- [ ] Unit tests (>80% coverage)
  - Excel manager
  - Greeting generator
  - Validators
  - Persona selection
- [ ] Integration tests (end-to-end)
- [ ] Manual testing (real graded Excel, 30 students)
- [ ] Instructor user testing (5 alpha testers)
- [ ] Performance testing (measure time for 30, 50 students)
- [ ] Content review (sample 50 greetings for appropriateness)
- [ ] Bug fixes and refinements

**Deliverable:**
- Test suite with >80% coverage
- All tests passing
- User testing completed
- Production-ready v1.0.0

**Success Criteria:**
- All functional requirements met
- 30 students in <2 minutes
- 85%+ student satisfaction (pilot test)
- 90%+ instructor satisfaction
- No inappropriate content (100% sample)

### Timeline

| Week | Focus | Deliverable | Milestone |
|------|-------|-------------|-----------|
| 1 | Persona Engineering | 4 validated personas | Prompts produce quality greetings |
| 2 | Foundation | Basic CLI + API | Generates greetings for 5 students |
| 3 | Robustness | Error handling | Handles 30 students with errors |
| 4 | Polish | UX improvements | Professional tool |
| 5 | Testing | Test suite + validation | Production ready |

**Total:** 5 weeks to v1.0.0

---

## Testing Plan

### Unit Tests

**test_excel_manager.py:**
- Read graded Excel with all columns
- Read Excel with missing columns (error)
- Read Excel with no grades (error)
- Write Excel with greetings column
- Preserve original data exactly
- Handle special characters in greetings

**test_greeting_generator.py:**
- Determine persona correctly for all grade ranges
- Load persona prompts from files
- Generate greeting via Claude API
- Retry logic (3x with backoff)
- Fallback to templates on API failure
- Content validation (blocklist, length)

**test_validators.py:**
- Validate appropriate content (pass cases)
- Block inappropriate content (fail cases)
- Validate greeting length (10-300 words)
- Handle edge cases (empty, very long, special chars)

**test_persona_selection.py:**
- Grade 0-50 → dudi_amsalem
- Grade 51-70 → netanyahu
- Grade 71-90 → shahar_hasson
- Grade 91-100 → trump
- Edge cases: 0, 50, 70, 90, 100
- null/None → no_grade

**Coverage Target:** >80%

### Integration Tests

**test_end_to_end.py:**
- Full workflow: Excel → Generate → Output
- Process 10 test students (all persona ranges)
- Verify output Excel correctness
- Verify greeting appropriateness
- Verify all original data preserved

**Test Fixtures:**
```
tests/fixtures/
├── sample_graded.xlsx           # 10 students, all grade ranges
├── sample_graded_with_errors.xlsx  # Mixed: valid + error rows
├── expected_output.xlsx         # Expected results
└── persona_samples/             # Pre-generated greeting samples
    ├── dudi_amsalem_samples.txt
    ├── netanyahu_samples.txt
    ├── shahar_hasson_samples.txt
    └── trump_samples.txt
```

### Manual Testing

**Persona Quality Review:**
1. Generate 10 greetings per persona (40 total)
2. Manual review by instructor panel (3 instructors)
3. Rate each greeting:
   - Matches persona style? (Yes/No)
   - Appropriate for grade range? (Yes/No)
   - Educational and motivational? (Yes/No)
   - Any inappropriate content? (Yes/No)
4. Target: 95%+ "Yes" on all criteria

**Student Feedback Test:**
1. Pilot test with 30 students (real class)
2. Survey after receiving greetings:
   - "The feedback felt personalized" (1-5)
   - "The feedback was motivating" (1-5)
   - "The feedback was helpful" (1-5)
   - "I would prefer this over just a number" (Yes/No)
3. Target: 4.0+ average rating, 85%+ prefer greetings

**Instructor Feedback Test:**
1. 5 instructors use tool for 1 assignment
2. Survey:
   - Ease of use (1-5)
   - Time savings (Yes/No + minutes saved)
   - Greeting quality (1-5)
   - Would use again (Yes/No)
3. Target: 4.0+ average rating, 100% would use again

### Performance Testing

**Benchmark:**
| Students | Sequential | With API Delay | Target |
|----------|------------|----------------|--------|
| 10 | ~30 sec | ~30 sec | <40 sec |
| 30 | ~90 sec | ~90 sec | <2 min |
| 50 | ~150 sec | ~150 sec | <3 min |

**Assumptions:**
- API latency: 2-3 seconds per greeting
- Excel I/O: <5 seconds total
- Sequential processing (no parallelization in v1.0)

**Acceptance Criteria:**
- 30 students in <2 minutes
- No performance degradation with 50 students
- Memory usage <500MB

---

## Launch Plan

### Pre-Launch (Week 5)

**Internal Testing:**
- [ ] Test with 5 instructors (alpha testing)
- [ ] Collect feedback on greeting quality
- [ ] Test with real student classes
- [ ] Fix critical bugs

**Documentation:**
- [ ] README with installation, usage, API key setup
- [ ] Example greetings for each persona
- [ ] Troubleshooting guide
- [ ] FAQ (common questions)

**Preparation:**
- [ ] GitHub repository ready
- [ ] PyPI package prepared (optional)
- [ ] Demo video/screenshots
- [ ] Release notes

### Launch (Week 5, End)

**Distribution:**
- [ ] Merge to main branch (EmailSkillAgents repo)
- [ ] Tag release: v1.0.0
- [ ] Update main README with new agent
- [ ] Announce to instructor community

**Announcement:**
- [ ] Internal announcement (university/institution)
- [ ] Blog post explaining the three-agent workflow
- [ ] Share on teaching communities

### Post-Launch (Week 6-10)

**Monitoring:**
- [ ] Track usage (number of instructors, greetings generated)
- [ ] Monitor feedback (GitHub issues, surveys)
- [ ] Collect student reactions
- [ ] Measure re-submission rates

**Support:**
- [ ] Respond to issues within 48 hours
- [ ] Fix critical bugs within 1 week
- [ ] Document common issues in FAQ

**Iteration:**
- [ ] Gather v1.1 feature requests
- [ ] Prioritize enhancements
- [ ] Plan v1.1 roadmap

---

## Risks & Mitigation

| Risk | Probability | Impact | Mitigation | Owner |
|------|-------------|--------|------------|-------|
| **AI-generated content is inappropriate** | Medium | Critical | Extensive prompt engineering, content validation, manual review sample, blocklist filtering | PM + Dev |
| **Personas feel offensive or stereotypical** | Medium | High | Cultural sensitivity review, instructor panel feedback, focus on educational value not entertainment | PM |
| **Claude API costs too high for instructors** | Low | Medium | Document costs (~$0.01-0.02 per greeting), optimize prompts to reduce tokens, provide cost calculator | PM |
| **API failures prevent greeting generation** | Medium | Medium | Retry logic (3x), fallback templates (100% coverage), cache prompts, document offline mode | Developer |
| **Students find greetings insincere/robotic** | Medium | High | Pilot test with students, iterate prompts, ensure personalization (grade reference), instructor review | PM |
| **Greetings don't match instructor's teaching style** | High | Medium | v1.1: custom personas, tone adjustment, instructor can edit greetings before sending | PM |
| **Legal concerns (using real public figures)** | Low | High | Legal review, disclaimers (parody/educational use), respectful portrayal, avoid political content | Legal |
| **Students compare greetings and find patterns** | Medium | Low | Increase temperature for variety, document that it's AI-assisted (transparency), focus on value | PM |

---

## Dependencies & Assumptions

### Dependencies

**Internal:**
- Repository Analyzer (provides graded Excel input)
- GmailAgent (provides original email data, optional)
- Output directory (write access required)

**External:**
- Claude API (Anthropic) - requires API key and credits
- Internet connection (for API calls)
- Python 3.8+ installed
- openpyxl library

**API Requirements:**
- Anthropic API key (get from https://console.anthropic.com)
- API credits (estimated $0.50-1.00 for 30 students)
- Rate limits: 50 requests/minute (sufficient for sequential processing)

### Assumptions

**User Assumptions:**
- Instructors are comfortable with AI-generated content
- Instructors will review greetings before sending to students (optional but recommended)
- Students understand feedback is AI-assisted (transparency)
- Instructors have API key or can obtain one (simple process)

**Technical Assumptions:**
- Claude API produces consistent, high-quality output
- Persona prompts are robust across different grade values
- API latency is 2-3 seconds per greeting (acceptable)
- Internet connection is stable during generation

**Educational Assumptions:**
- Personalized feedback improves student engagement
- Different motivation styles work for different performance levels
- Instructor time savings justify AI-assisted approach
- Students respond positively to varied communication styles

**Cultural Assumptions:**
- Public figure personas are acceptable in educational context
- Caricatures are understood as educational tools, not mockery
- International students understand cultural references (may need localization in v1.1)

### Constraints

**Budget:**
- Development: $0 (internal tool)
- API costs: ~$0.01-0.02 per greeting (instructor pays or institution)
- Estimated cost per class: $0.30-0.60 (30 students)

**Timeline:** 5 weeks to production

**Resources:**
- 1 developer (full-time, weeks 2-5)
- 1 PM (prompt engineering, week 1)
- 1 QA (testing, week 5)
- 3 instructors (alpha testing, week 5)

**Technical:**
- Claude API only (no other LLMs in v1.0)
- Sequential processing (no parallelization in v1.0)
- Text greetings only (no audio/video)
- English only (no i18n in v1.0)

**Ethical:**
- Must be appropriate for educational use (100% safe)
- Respectful portrayal of public figures
- Transparency about AI-generated content
- Instructor oversight recommended

---

## Open Questions & Decisions

### OPEN: Should instructors review greetings before sending?

**Question:** Should the tool support an "approve before send" workflow?

**Options:**
1. **Auto-send:** Greetings go directly to students (fastest, least oversight)
2. **Review mode:** Instructors review/edit greetings before sending (safer, more time)
3. **Output only:** Tool outputs Excel, instructor decides how to share (current approach)

**Current Decision:** Output only (option 3) for v1.0
- Instructors can review greetings in Excel
- Instructors decide how to share (email, LMS, etc.)
- v1.1 can add email integration with approval workflow

**Owner:** Product Manager
**Status:** Tentative (finalize in Week 1)

### OPEN: API Cost Management

**Question:** How do we handle API costs for instructors?

**Options:**
1. **Instructor pays:** Each instructor gets their own API key
2. **Institution pays:** Shared institutional API key
3. **Freemium:** First 100 greetings free, then pay
4. **Offline mode:** Pre-cache persona outputs, no API needed (lower quality)

**Current Decision:** Instructor pays (option 1) for v1.0
- Simple, no billing infrastructure needed
- API costs are low (~$0.50 per class)
- Document cost in README
- v1.1 can explore institutional licensing

**Owner:** Product Manager
**Status:** Open (finalize in Week 1)

### OPEN: Student Name Personalization

**Question:** Should greetings include student names?

**Options:**
1. **No names:** Generic greetings (current plan)
2. **Names from email:** Extract names from Subject/From (privacy concern)
3. **Manual upload:** Instructor provides name list
4. **LMS integration:** Pull names from LMS (complex)

**Current Decision:** No names for v1.0 (option 1)
- Simplest, no privacy concerns
- Greetings still feel personal via grade-specific content
- v1.1 can add optional name injection

**Owner:** Product Manager
**Status:** Open (validate with instructors in Week 1)

### RESOLVED: Persona Choices

**Question:** Are these 4 personas appropriate and effective?

**Options Considered:**
- Tech industry leaders (Musk, Gates, Jobs) → REJECTED (too corporate)
- Fictional characters (Yoda, Tony Stark) → REJECTED (less relatable)
- Generic styles (Encouraging, Neutral, Strict) → REJECTED (less engaging)
- **Real public figures with distinct styles** → SELECTED

**Decision:** Use Dudi Amsalem, Netanyahu, Shahar Hasson, Trump
- Distinct communication styles
- Recognizable to students (cultural relevance)
- Range from tough to celebratory
- Can be portrayed respectfully
- Educational value (exposure to different communication styles)

**Validation:** Test with 3 instructors in Week 1

**Owner:** Product Manager
**Date:** 2025-11-23

### RESOLVED: Grade Range Thresholds

**Question:** Are 0-50%, 51-70%, 71-90%, 91-100% the right thresholds?

**Decision:** YES, use these thresholds for v1.0
- Aligns with common grading scales (F, D/C, B, A)
- Creates meaningful performance tiers
- Distributes personas evenly
- Can be made configurable in v1.1

**Owner:** Product Manager
**Date:** 2025-11-23

---

## Appendix

### Glossary

- **Persona:** AI communication style based on a public figure
- **Skill:** Prompt/instruction set for a specific persona
- **Greeting:** Personalized feedback message for a student
- **Grade range:** Performance tier that determines persona (0-50%, 51-70%, 71-90%, 91-100%)
- **Fallback template:** Pre-written greeting used when API fails
- **Content validation:** Checking greeting for appropriateness

### Example Greetings by Persona

**Dudi Amsalem (25%):**
```
Listen, 25%? This is not acceptable. You're not even close to where you need to be.
I don't know if you're not trying or not understanding, but either way, this has to
change immediately. You have potential - I wouldn't waste my time otherwise - but
you need to step up now. Get help, put in the work, and show me you're serious.
Time's running out.
```

**Benjamin Netanyahu (65%):**
```
Your achievement of 65% represents a commendable effort and demonstrates fundamental
understanding of the material. However, to reach the higher standards of excellence
that I know you are capable of, further refinement and dedication will be necessary.
I encourage you to analyze areas for improvement and commit to strengthening your
approach. With focused effort, I am confident you can elevate your performance
significantly.
```

**Shahar Hasson (82%):**
```
Nice work - 82% shows you really understand the concepts! Your code structure is
solid, and I can see you're putting thought into organization and clarity. You're
in that zone where you're doing well, but there's still room to polish things up
and hit that top tier. Want to get to 90%+? Look at those couple of larger files
and see if you can break them down even further. You're on the right track - keep
refining!
```

**Donald Trump (97%):**
```
WOW! 97%! This is FANTASTIC work - truly outstanding! You're doing everything right,
and it shows. Your code organization is excellent, really excellent. This is exactly
the kind of high-quality work that leads to big success in the tech industry. You're
a winner, and you should be proud of this achievement. Keep up this TREMENDOUS
performance - you're going places!
```

### CLI Examples

```bash
# Basic usage
greetings-agent generate --input homework_emails_graded.xlsx

# Custom output path
greetings-agent generate -i graded.xlsx -o feedback.xlsx

# Verbose mode
greetings-agent generate -i graded.xlsx -v

# Show help
greetings-agent --help
greetings-agent generate --help

# Version
greetings-agent --version
```

### API Key Setup Guide

**Step 1: Get Claude API Key**
1. Go to https://console.anthropic.com
2. Sign up or log in
3. Navigate to API Keys section
4. Create new API key
5. Copy the key (starts with `sk-ant-`)

**Step 2: Set Environment Variable**

**Windows:**
```cmd
setx ANTHROPIC_API_KEY "sk-ant-your-key-here"
```

**macOS/Linux:**
```bash
echo 'export ANTHROPIC_API_KEY="sk-ant-your-key-here"' >> ~/.bashrc
source ~/.bashrc
```

**Or create .env file:**
```bash
# In project directory
echo "ANTHROPIC_API_KEY=sk-ant-your-key-here" > .env
```

**Step 3: Test**
```bash
greetings-agent generate -i sample.xlsx
```

### Cost Estimator

**Claude API Pricing (Sonnet 4.5):**
- Input: $3 per million tokens
- Output: $15 per million tokens

**Estimated Token Usage per Greeting:**
- Persona prompt: ~300 tokens (input)
- Student grade: ~10 tokens (input)
- Generated greeting: ~100 tokens (output)
- **Total:** ~310 input + 100 output ≈ $0.001 + $0.0015 = **$0.0025 per greeting**

**Cost per Class:**
- 10 students: ~$0.025 (2.5 cents)
- 30 students: ~$0.075 (7.5 cents)
- 50 students: ~$0.125 (12.5 cents)

**Annual Cost (15 assignments, 30 students):**
- 15 × 30 × $0.0025 = **$1.13 per year**

**Conclusion:** API costs are negligible (<$2/year for most instructors).

### Success Story (Hypothetical)

**Instructor: Professor Sarah Chen**
**Class:** Introduction to Programming, 32 students
**Assignment:** Homework 3 - File Organization

**Before Greetings Agent:**
- Grading time: 3 hours (with Repository Analyzer)
- Feedback: Just numerical grades
- Student engagement: 18% re-submitted improved versions
- Student feedback: "I don't know what I did wrong"

**After Greetings Agent:**
- Grading time: 3 hours 2 minutes (2 min to add greetings)
- Feedback: Numerical grades + personalized motivational messages
- Student engagement: 34% re-submitted improved versions (89% increase!)
- Student feedback:
  - "The feedback felt personal and helpful" - 87% agreed
  - "I felt motivated to improve" - 82% agreed
  - "I understood what I needed to work on" - 78% agreed
- Top performer (95%): "The Trump greeting made me laugh and feel proud!"
- Struggling student (38%): "The tough love was what I needed - I got serious and improved to 72%"

**Impact:**
- Time investment: 2 minutes
- Student satisfaction: +45%
- Re-submission rate: +89%
- Average grade improvement: +8% (on re-submissions)

---

## Change Log

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2025-11-23 | Product Strategist | Initial comprehensive PRD:<br>- Defined problem statement and value proposition<br>- Detailed 4 persona specifications with prompts<br>- 15+ user stories across 6 epics<br>- Complete functional requirements (FR-1 through FR-5)<br>- Technical architecture and data flow<br>- 5-week incremental implementation plan<br>- Testing strategy with persona quality review<br>- Cost analysis and API setup guide<br>- Cultural sensitivity considerations<br>- Example greetings for each persona |

---

## Next Steps

1. **Stakeholder Review** (Week 0):
   - [ ] Review PRD with instructor stakeholders
   - [ ] Validate persona choices (appropriate and effective?)
   - [ ] Confirm grade range thresholds
   - [ ] Approve API cost model
   - [ ] Get legal review for public figure usage

2. **Prompt Engineering** (Week 1):
   - [ ] Research each persona's communication style
   - [ ] Draft persona skill prompts
   - [ ] Test prompts manually via Claude API
   - [ ] Iterate until quality is consistent
   - [ ] Create fallback templates
   - [ ] Review with instructor panel (3 instructors)

3. **Development Kickoff** (Week 2):
   - [ ] Set up project structure
   - [ ] Install dependencies (anthropic, openpyxl, click)
   - [ ] Create persona_skills/ directory with prompts
   - [ ] Begin coding (excel_manager.py, greeting_generator.py)

4. **Testing & Validation** (Week 5):
   - [ ] Unit tests (>80% coverage)
   - [ ] Integration tests (end-to-end)
   - [ ] Manual persona quality review (40 greetings)
   - [ ] Instructor alpha testing (5 instructors)
   - [ ] Student feedback pilot (30 students)

---

**Status:** ✅ READY FOR STAKEHOLDER REVIEW
**Confidence:** HIGH (clear value proposition, detailed requirements, realistic timeline)
**Risk Level:** MEDIUM (depends on persona quality and student reception)

---

## Workflow Integration

### Three-Agent Workflow

```
┌─────────────────────────────────────────────────────────────┐
│                    INSTRUCTOR WORKFLOW                      │
└─────────────────────────────────────────────────────────────┘

Step 1: COLLECT HOMEWORK SUBMISSIONS
  ↓
┌─────────────────────┐
│   Agent 1:          │
│   GmailAgent        │
│   - Export emails   │
│   - Extract URLs    │
└──────────┬──────────┘
           ↓
  homework_emails.xlsx
  (ID, Date, Subject, URL)

Step 2: GRADE CODE QUALITY
  ↓
┌─────────────────────┐
│   Agent 2:          │
│   Repository        │
│   Analyzer          │
│   - Clone repos     │
│   - Calculate grade │
└──────────┬──────────┘
           ↓
  homework_emails_graded.xlsx
  (+ Grade, Files, Lines, Status)

Step 3: ADD PERSONALIZED FEEDBACK
  ↓
┌─────────────────────┐
│   Agent 3:          │
│   Greetings Agent   │
│   (NEW)             │
│   - Generate        │
│     motivational    │
│     greetings       │
└──────────┬──────────┘
           ↓
  homework_emails_with_greetings.xlsx
  (+ Personalized Greeting)

Step 4: SHARE FEEDBACK WITH STUDENTS
  ↓
[Instructor reviews and sends via email/LMS]
```

### Time Comparison

**Manual Workflow:**
1. Collect emails: 10 min
2. Clone and grade 30 repos: 2-3 hours
3. Write personalized feedback: 60-90 min
**Total: 3.5-5 hours**

**Automated Workflow:**
1. GmailAgent export: 2 min
2. Repository Analyzer: 20 min (parallel processing)
3. Greetings Agent: 2 min
**Total: 24 minutes (87% time savings!)**

---

*This PRD has been created by the Product Strategy team to ensure the Personalized Greetings Agent delivers educational value, maintains cultural sensitivity, and integrates seamlessly into the existing three-agent homework grading workflow.*
