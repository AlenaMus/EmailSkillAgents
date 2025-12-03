# EVALUATION GMAIL SENDER AGENT - PRD

**Version:** 1.0
**Date:** 2025-11-23
**Status:** Ready for Development
**Product Manager:** Product Management Team

---

## Executive Summary

The **Evaluation Gmail Sender Agent** is the fourth and final agent in the automated homework grading workflow. It completes the feedback loop by automatically sending personalized grade reports back to students via Gmail.

**Core Value:** Transform graded assignments into delivered feedback automatically, completing the end-to-end grading workflow.

**Position in Workflow:**
1. Agent 1 (GmailAgent): Exports homework emails to Excel
2. Agent 2 (Repository Analyzer): Analyzes repos and calculates grades
3. Agent 3 (Personalized Greetings): Adds motivational feedback
4. **Agent 4 (Evaluation Gmail Sender - NEW): Sends feedback to students**

**Time Savings:** 30-60 minutes of manual email composition → <1 minute automated

---

## Problem Statement

### User Problem

**Who:** Course instructors who have completed automated grading

**What:** "I've automated my grading with three agents. Now I have an Excel file with grades, personalized greetings, and repository URLs. But I still need to manually compose and send 30+ emails to students, copying grades and feedback into each email. This takes another 30-60 minutes."

**Why it matters:**
- Students need timely feedback (within 24-48 hours)
- Manual email composition is tedious and error-prone
- Feedback loop incomplete without delivery
- Risk of copy-paste errors (wrong grade to wrong student)

---

## Goals & Success Metrics

### North Star Metric

**Time from Homework Submission to Feedback Received:** 24 hours (from 1-2 weeks)

### Success Metrics

- **Email Generation Time:** <1 minute for 30 students
- **Email Accuracy:** 100% correct grade-to-student mapping
- **Student Feedback Timeliness:** 90%+ receive within 24 hours
- **Draft Review Rate:** 60%+ instructors review drafts
- **Email Open Rate:** 85%+ students open feedback

---

## User Stories

### Epic 1: Gmail Draft Creation

**US-1.1: Generate Gmail Drafts from Excel**
**Priority:** Critical | **Effort:** 5 points

**As an** instructor,
**I want to** generate Gmail drafts for all students from the graded Excel file,
**So that** I can review feedback before sending.

**Acceptance Criteria:**
- Read `homework_emails_with_greetings.xlsx`
- Create Gmail draft for each student
- Subject: Original homework submission subject
- Body: Grade + personalized greeting + repo URL
- Apply label "lesson19Agents"
- Show progress: [3/30] Creating draft...
- Summary: "✓ Created 30 drafts in Gmail"

---

### Epic 2: Direct Email Sending

**US-2.1: Send Emails Directly (Optional)**
**Priority:** Medium | **Effort:** 3 points

**As an** instructor,
**I want** to send emails directly without creating drafts,
**So that** I can save time when I trust the process.

**Acceptance Criteria:**
- Option: `--send` flag
- Emails sent directly (not drafts)
- Label "lesson19Agents" applied
- Confirmation prompt before sending
- Summary: "✓ Sent 30 emails"

---

### Epic 3: Email Template & Formatting

**US-3.1: Professional Email Template**
**Priority:** Critical | **Effort:** 3 points

**As an** instructor,
**I want** professionally formatted emails,
**So that** students take feedback seriously.

**Acceptance Criteria:**
- HTML-formatted email
- Grade displayed prominently
- Full personalized greeting
- Clickable repository URL
- Professional signature
- Mobile-responsive
- UTF-8 support (Hebrew characters)

---

### Epic 4: Testing & Safety

**US-4.1: Test Mode (Send to Self)**
**Priority:** High | **Effort:** 2 points

**As an** instructor,
**I want** to send all emails to myself for testing,
**So that** I can verify format before sending to students.

**Acceptance Criteria:**
- Option: `--to myemail-sender@test.com`
- All emails sent to test address
- Subject/body reflect individual student data
- Can verify email format

---

## Functional Requirements

### FR-1: Excel Input Processing

**Read Excel File:**
- Accept file path as CLI argument
- Validate file exists and readable
- Expected columns: ID, Date, Subject, URL, Grade, Personalized Greeting
- Extract: Subject, Grade, Greeting, Repo URL, Student email

**Email Address Detection:**
- Extract from original email metadata (if available)
- Or use separate column in Excel
- Validate email format
- Handle missing emails gracefully

---

### FR-2: Gmail API Integration

**Authentication:**
- OAuth 2.0 (reuse from GmailAgent)
- Scopes: gmail.compose, gmail.send, gmail.labels
- Store token in ~/.gmailagent/

**Draft Creation:**
- API: `users.drafts.create`
- To: Student email
- Subject: Original homework subject
- Body: HTML email template
- Label: "lesson19Agents"

**Email Sending:**
- API: `users.messages.send`
- Same content as draft mode
- Label: "lesson19Agents"

**Label Management:**
- Check if "lesson19Agents" exists
- Create if not exists
- Apply to all drafts/emails

---

### FR-3: Email Template

**HTML Template:**
```html
<!DOCTYPE html>
<html>
<body style="font-family: Arial, sans-serif;">
    <p>Hi {student_name},</p>

    <p style="font-size: 20px; font-weight: bold; color: #2c5aa0;">
        Your grade: {grade}%
    </p>

    <div style="background: #f5f5f5; padding: 15px; border-left: 4px solid #2c5aa0;">
        <strong>Feedback:</strong><br>
        {personalized_greeting}
    </div>

    <p><strong>Repository:</strong>
       <a href="{repo_url}">{repo_url}</a>
    </p>

    <p>Best regards,<br>{instructor_name}</p>
</body>
</html>
```

**Variables:**
- `{student_name}`: From email or "there"
- `{grade}`: Numeric grade
- `{personalized_greeting}`: Full greeting text
- `{repo_url}`: Repository URL
- `{instructor_name}`: Configurable (default: "Your Instructor")

---

### FR-4: CLI Interface

**Commands:**

```bash
# Authenticate
python -m evaluation_gmail_sender.cli auth

# Create drafts (default, safe)
python -m evaluation_gmail_sender.cli create-drafts \
    --input greetings_results/homework_emails_with_greetings.xlsx

# Send emails directly
python -m evaluation_gmail_sender.cli send-emails \
    --input greetings_results/homework_emails_with_greetings.xlsx

# Test mode (send to self)
python -m evaluation_gmail_sender.cli send-emails \
    --input file.xlsx \
    --to myemail-sender@test.com

# Dry run (preview only)
python -m evaluation_gmail_sender.cli create-drafts \
    --input file.xlsx \
    --dry-run
```

**Options:**
- `--input`: Excel file path (required)
- `--to`: Override recipient (for testing)
- `--dry-run`: Don't actually send
- `--verbose`: Detailed output
- `--yes`: Skip confirmation

---

### FR-5: Error Handling

**Error Types:**
| Error | Handling | Message |
|-------|----------|---------|
| File not found | Abort | "Excel file not found" |
| No email address | Skip, log | "Skipped: No email" |
| Gmail API error | Retry 3x | "Failed after 3 attempts" |
| Network timeout | Retry with backoff | "Retrying..." |

**Summary Report:**
```
Summary
=======
Total Students: 30
Drafts Created: 28
Skipped: 2 (no email)
Failed: 0
```

---

## Technical Architecture

**Module Structure:**
```
evaluation_gmail_sender/
├── __init__.py
├── cli.py              # CLI interface
├── email_sender.py     # Main orchestrator
├── excel_reader.py     # Read Excel
├── gmail_client.py     # Gmail API wrapper
├── email_template.py   # Template generation
├── config.py           # Configuration
└── errors.py           # Custom exceptions
```

**Technology Stack:**
- Python 3.8+
- openpyxl (Excel I/O)
- google-api-python-client (Gmail API)
- google-auth-oauthlib (OAuth 2.0)
- click (CLI)
- Jinja2 (Email templates)

---

## Implementation Plan

### Phase 1: Foundation (Week 1-2)
- Gmail API setup and authentication
- Excel reader implementation
- Email template (HTML)
- Draft creation (basic)

### Phase 2: Robustness (Week 3)
- Error handling (missing emails, API errors)
- Retry logic
- Summary reports
- Logging

### Phase 3: Advanced Features (Week 4)
- Send emails directly (--send)
- Test mode (--to override)
- Dry-run mode
- Label management

### Phase 4: Testing & Docs (Week 5)
- Unit tests (>80% coverage)
- Integration tests
- Manual testing
- Documentation (README, QUICKSTART)

---

## Success Metrics

**Primary:**
- Email generation: <1 min for 30 students
- Accuracy: 100% correct mapping
- Adoption: 80%+ instructors use it

**Secondary:**
- Email open rate: 85%+
- Student engagement: 30%+ reply
- Instructor satisfaction: 4.5/5

---

## Risk Analysis

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Wrong grade to wrong student | Medium | Critical | Draft mode default, testing |
| Gmail API quota | Low | High | Monitor usage, batch ops |
| Spam filtering | Medium | Medium | Use instructor Gmail, plain text |
| Token expiration | Medium | Medium | Auto-refresh, clear re-auth |

---

## Future Enhancements

**v1.1:**
- Customizable templates
- Email tracking (opens, clicks)
- BCC to instructor
- Scheduled sending

**v1.2:**
- Attachments (PDF reports)
- Reply handling
- Email threads

**v2.0:**
- LMS integration (Canvas, Moodle)
- Multi-channel (Slack, SMS)
- AI reply summarization

---

## Appendix

### Email Template Examples

**High Grade (Trump):**
```
Subject: Homework 17 - t-SNE

Hi Student,

Your grade: 95%

Feedback:
TREMENDOUS work! 95%! This is WINNING! You're FANTASTIC!

Repository: https://github.com/student/repo

Best regards,
Prof. Chen
```

**Low Grade (Dudi):**
```
Subject: Homework 5

Hi Student,

Your grade: 45%

Feedback:
Listen, 45%? Not good enough. Time to stop excuses and
make real progress. You can do better.

Repository: https://github.com/student/repo

Best regards,
Prof. Chen
```

---

## Summary

The Evaluation Gmail Sender Agent completes the automated grading workflow by sending personalized feedback to students. It saves 30-60 minutes per assignment and ensures timely, professional feedback delivery.

**Ready for development** with clear requirements, architecture, and implementation plan.

---

**File Path:** C:\AIDevelopmentCourse\L-19\EmailSkillAgents\PRD-EvaluationGmailSender.md

**END OF PRD**
