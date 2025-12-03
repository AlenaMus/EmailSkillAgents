# Quick Start Guide - Evaluation Gmail Sender Agent

**Version:** 1.0.0
**Time to Start:** < 2 minutes
**No Gmail API Required**

---

## What This Agent Does

Reads graded Excel files (from Agent 3) and creates professional HTML emails with personalized feedback for each student.

---

## Installation (30 seconds)

```bash
# Navigate to project
cd C:\AIDevelopmentCourse\L-19\EmailSkillAgents

# Install dependencies (if not already installed)
pip install openpyxl click
```

Done! No Gmail API setup needed.

---

## Basic Usage (1 minute)

### Step 1: Test Reading Excel File

```bash
python -m evaluationAgent.cli test
```

**Expected Output:**
```
Found 4 students
Valid for email:   3
Skipped (invalid): 1
```

### Step 2: Preview What Will Happen (Dry-Run)

```bash
python -m evaluationAgent.cli create-drafts --dry-run
```

**Expected Output:**
```
[1/3] Student (Grade: 100%) -> Would create draft for test@example.com (DRY RUN)
[2/3] Student (Grade: 75%) -> Would create draft for test@example.com (DRY RUN)
[3/3] Student (Grade: 100%) -> Would create draft for test@example.com (DRY RUN)
```

### Step 3: Create Email Drafts

```bash
python -m evaluationAgent.cli create-drafts
```

**Expected Output:**
```
[1/3] Student (Grade: 100%) -> Saved to email_1_grade_100_test_at_example_com.html
[2/3] Student (Grade: 75%) -> Saved to email_2_grade_75_test_at_example_com.html
[3/3] Student (Grade: 100%) -> Saved to email_3_grade_100_test_at_example_com.html

[OK] Created 3 email drafts successfully!
```

### Step 4: Review Emails

```bash
# Open email_drafts folder
explorer email_drafts

# Open an email in browser
start email_drafts/email_1_grade_100_test_at_example_com.html
```

**What You'll See:**
- Professional HTML email
- Student grade prominently displayed
- Personalized feedback (Trump/Shahar Hasson persona)
- Clickable repository link
- Mobile-responsive design

---

## Common Commands

### Default Usage (Safe Mode)

```bash
# Create HTML emails (no Gmail API needed)
python -m evaluationAgent.cli create-drafts
```

Output: `email_drafts/*.html` files

### Test with Your Email

```bash
# All emails sent to your address (for testing)
python -m evaluationAgent.cli create-drafts --to your@email.com
```

### Custom Instructor Name

```bash
# Professional signature
python -m evaluationAgent.cli create-drafts --instructor-name "Prof. David Chen"
```

### Verbose Mode (Detailed Output)

```bash
# See detailed progress
python -m evaluationAgent.cli create-drafts --verbose
```

### Custom Input File

```bash
# Use different Excel file
python -m evaluationAgent.cli create-drafts --input path/to/your/file.xlsx
```

---

## What You Get

### Email Files

```
email_drafts/
├── email_1_grade_100_test_at_example_com.html
├── email_2_grade_75_test_at_example_com.html
├── email_3_grade_100_test_at_example_com.html
└── summary.txt
```

### Summary Report

```
STATISTICS
------------------------------------------------------------
Total Students:        4
Valid for Email:       3
Emails Created:        3
Skipped:               1
Failed:                0

CREATED EMAILS
------------------------------------------------------------
Output Directory: email_drafts/
Files Created:
  - email_1_grade_100_test_at_example_com.html
  - email_2_grade_75_test_at_example_com.html
  - email_3_grade_100_test_at_example_com.html
```

---

## Email Preview

### Example 1: 100% Grade (Trump Persona)

```
Hi there,

Your grade for this assignment: 100%

Feedback:
EXCELLENT! 100%! This is what I call WINNING! Your work is
outstanding, just outstanding. You're a star performer, the
BEST! Keep up these high standards - you're going places!
AMAZING!

Repository: https://github.com/student/repo

Best regards,
Your Instructor
```

### Example 2: 75% Grade (Shahar Hasson Persona)

```
Hi there,

Your grade for this assignment: 75%

Feedback:
Solid! 75% is really good work. You're clearly understanding
the concepts. With a bit more attention to detail, you could
be hitting 95%+. Keep up the great work!

Repository: https://github.com/student/repo

Best regards,
Your Instructor
```

---

## Workflow Integration

### Complete 4-Agent Workflow

```
1. GmailAgent
   ↓ exports/homework_emails.xlsx

2. Repository Analyzer
   ↓ repo_analysis_results/homework_emails_with_grades.xlsx

3. Personalized Greetings
   ↓ greetings_results/homework_emails_with_greetings.xlsx

4. Evaluation Gmail Sender (THIS AGENT)
   ↓ email_drafts/*.html
```

### Input File Expected

**Location:** `greetings_results/homework_emails_with_greetings.xlsx`

**Required Columns:**
- ID, Subject, URL, Grade, Status, Personalized Greeting

**Valid Student Criteria:**
- Status = "Success"
- Grade > 0
- Personalized Greeting not empty
- URL starts with http:// or https://

---

## Troubleshooting

### Issue: No emails created

**Symptom:**
```
Emails Created: 0
```

**Solution:**
```bash
# Diagnose the issue
python -m evaluationAgent.cli test

# Check for:
# - Students with Status != "Success"
# - Students with Grade = 0
# - Missing personalized greetings
```

### Issue: File not found

**Symptom:**
```
✗ Input file not found
```

**Solution:**
```bash
# Verify file exists
dir greetings_results\homework_emails_with_greetings.xlsx

# Or specify custom path
python -m evaluationAgent.cli create-drafts --input path\to\file.xlsx
```

### Issue: Hebrew characters broken

**Solution:**
Open HTML files in a modern browser (Chrome, Firefox, Edge). UTF-8 encoding is automatic.

---

## Advanced Usage

### Dry-Run Mode

Preview without creating files:

```bash
python -m evaluationAgent.cli create-drafts --dry-run
```

### Test Mode

Send all to one recipient:

```bash
python -m evaluationAgent.cli create-drafts --to instructor@school.edu
```

### Combine Options

```bash
python -m evaluationAgent.cli create-drafts \
  --input custom.xlsx \
  --to test@email.com \
  --instructor-name "Prof. Smith" \
  --verbose
```

### Gmail API Mode (Optional)

Create drafts in Gmail instead of files:

```bash
# First time: Authenticate
python -m evaluationAgent.cli auth

# Create drafts in Gmail
python -m evaluationAgent.cli create-drafts --use-gmail
```

**Note:** Gmail API requires additional setup (credentials.json). Default HTML file mode works without any setup.

---

## Getting Help

```bash
# Main help
python -m evaluationAgent.cli --help

# Command help
python -m evaluationAgent.cli create-drafts --help

# Test command help
python -m evaluationAgent.cli test --help
```

---

## Best Practices

### 1. Always Test First

```bash
# Step 1: Test Excel reading
python -m evaluationAgent.cli test

# Step 2: Dry-run preview
python -m evaluationAgent.cli create-drafts --dry-run

# Step 3: Create drafts
python -m evaluationAgent.cli create-drafts
```

### 2. Review Before Sending

```bash
# Create HTML files
python -m evaluationAgent.cli create-drafts

# Open in browser
start email_drafts/email_1_grade_100_test_at_example_com.html

# Verify:
# - Grade correct
# - Feedback appropriate
# - Repository URL correct
# - Formatting good
```

### 3. Use Test Mode

```bash
# Send all to yourself first
python -m evaluationAgent.cli create-drafts --to your@email.com

# Review in your inbox
# Then send to students
```

### 4. Check Summary

```bash
# Review summary report
type email_drafts\summary.txt

# Verify:
# - All expected students processed
# - Skip reasons make sense
# - No unexpected failures
```

---

## FAQ

**Q: Do I need Gmail API?**
A: No! Default mode saves HTML files. Gmail API is optional.

**Q: How do I preview emails?**
A: Run without `--use-gmail`. Open HTML files in browser.

**Q: Can I customize the template?**
A: Yes! Edit `evaluationAgent/email_template.py`.

**Q: How do I change instructor name?**
A: Use `--instructor-name "Your Name"` flag.

**Q: What if a student has 0% grade?**
A: They are automatically skipped (no email sent).

**Q: Can I send to one email for testing?**
A: Yes! Use `--to your@email.com` flag.

---

## Time Savings

**Manual Process:**
- Compose 30 emails: 30-60 minutes
- Risk of errors: High
- Consistency: Low

**Automated Process:**
- Generate 30 emails: < 1 minute
- Risk of errors: Zero
- Consistency: 100%

**Result:** 97%+ time savings

---

## Next Steps

1. **Review Emails:**
   - Open `email_drafts/` folder
   - Open HTML files in browser
   - Verify formatting and content

2. **Test with Your Email:**
   ```bash
   python -m evaluationAgent.cli create-drafts --to your@email.com
   ```

3. **Customize Instructor Name:**
   ```bash
   python -m evaluationAgent.cli create-drafts --instructor-name "Prof. Smith"
   ```

4. **Optional: Set Up Gmail API**
   - See `evaluationAgent/README.md`
   - Only needed for `--use-gmail` mode

---

## Summary

**What:** Professional email generator for student feedback
**Input:** Excel file with grades and personalized greetings
**Output:** HTML email files (or Gmail drafts)
**Time:** < 1 minute for 30 students
**Setup:** None required (HTML mode)

**Ready to use immediately!**

---

**Evaluation Gmail Sender Agent v1.0.0** - Completing the grading workflow!
