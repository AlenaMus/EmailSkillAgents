# Orchestrator Interactive Menu Guide

**Version:** 2.0.0 (with Interactive Prompts)

---

## What's New

The orchestrator now features **interactive prompts** that ask for inputs before running agents. No more guessing what parameters to use!

---

## Interactive Features

### Option 1: Email Generator

When you select Option 1, the orchestrator will ask:

```
======================================================================
  Agent 1: GmailAgent - Export Homework Emails
======================================================================

Please specify how to filter emails:
You can use label, subject, or both

Examples:
  Label: 'homework', 'lesson19', 'assignments'
  Subject: 'Homework 19', 'Assignment', 'Project'

Enter Gmail label (or press Enter to skip): homework
Enter subject text (or press Enter to skip): lesson19
```

**Features:**
- Prompts for Gmail label
- Prompts for subject text
- Both are optional (can press Enter to skip)
- Warns if no filters specified
- Shows the command being executed

---

### Option 4: Evaluation Sender

When you select Option 4, the orchestrator will ask:

```
======================================================================
  Agent 4: Evaluation Gmail Sender - Send Feedback
======================================================================

[OK] Input ready: All 30 rows ready

Default recipient: alona.musiyko@gmail.com
Enter a recipient email to send all drafts to that address (for testing)
Or press Enter to use the default email

Recipient email: test@example.com
[INFO] Recipient: test@example.com

Send email drafts to test@example.com? (yes/no): yes
```

**Features:**
- Shows default email (alona.musiyko@gmail.com)
- Prompts for recipient email
- Can press Enter to use default
- Asks for confirmation before sending
- Can cancel by typing 'no'

---

### Option 5: Run All Agents (NEW!)

When you select Option 5, the orchestrator gathers ALL configuration BEFORE starting:

```
======================================================================
  Running All Agents Synchronously
======================================================================

Before starting, we need to gather some information:

======================================================================
STEP 1: Email Export Filters
======================================================================

Specify how to filter emails from Gmail:
Examples:
  Label: 'homework', 'lesson19', 'assignments'
  Subject: 'Homework 19', 'Assignment', 'Project'

Enter Gmail label (or press Enter to skip): homework
Enter subject text (or press Enter to skip): Assignment 19

======================================================================
STEP 2: Email Recipient Configuration
======================================================================

Default recipient: alona.musiyko@gmail.com
Enter a recipient email to send all drafts to that address (for testing)
Or press Enter to use the default email

Recipient email: mytest@example.com

======================================================================
CONFIGURATION SUMMARY
======================================================================
Gmail Label:    homework
Subject Filter: Assignment 19
Recipient:      mytest@example.com
======================================================================

Start processing with this configuration? (yes/no): yes

[INFO] Running GmailAgent...
[OK] GmailAgent export completed
[OK] Found Excel file: 23.11.2025_071823_mails_by_label_homework.xlsx
...
```

**Features:**
- **STEP 1:** Gathers email filters (label, subject)
- **STEP 2:** Gathers recipient email
- **Configuration Summary:** Shows what will happen
- **Confirmation:** Asks to confirm before starting
- Can cancel at any point
- Runs all 4 agents automatically once confirmed

---

## Benefits

### Before (Old Version)
```bash
# You had to remember command syntax
python orchestrator.py
Select: 4
Enter recipient email: (what do I enter here?)
```

### After (New Version)
```bash
# Interactive prompts guide you
python orchestrator.py
Select: 4

Default recipient: alona.musiyko@gmail.com
Enter a recipient email to send all drafts to that address (for testing)
Or press Enter to use the default email

Recipient email: [Just press Enter or type your email]
```

---

## Key Improvements

### 1. No Need to Remember Arguments
- Old: You had to know `--label`, `--subject`, `--to`
- New: Interactive prompts ask you

### 2. Examples Provided
- Shows examples for each input
- Clear descriptions of what to enter

### 3. Default Values
- Press Enter to use defaults
- No typing required for common cases

### 4. Confirmation Steps
- Asks before performing critical actions
- Shows configuration summary
- Can cancel at any time

### 5. Better Error Prevention
- Validates inputs before running
- Warns about missing filters
- Confirms before sending emails

---

## Quick Start Examples

### Example 1: Export Homework Emails

```bash
python orchestrator.py
```

Select: `1`

```
Enter Gmail label (or press Enter to skip): homework
Enter subject text (or press Enter to skip): Lesson 19
```

Result: Exports all emails with label "homework" and subject containing "Lesson 19"

---

### Example 2: Send Email Drafts to Test Address

```bash
python orchestrator.py
```

Select: `4`

```
Recipient email: myemail@test.com
Send email drafts to myemail@test.com? (yes/no): yes
```

Result: Sends all email drafts to your test address

---

### Example 3: Run Complete Workflow

```bash
python orchestrator.py
```

Select: `5`

```
STEP 1: Email Export Filters
Enter Gmail label (or press Enter to skip): homework
Enter subject text (or press Enter to skip): Assignment

STEP 2: Email Recipient Configuration
Recipient email: [Press Enter for default]

Start processing with this configuration? (yes/no): yes
```

Result: Runs all 4 agents with your configuration

---

## Tips

### 1. Press Enter for Defaults
Most prompts have sensible defaults. Just press Enter to accept them.

### 2. Test First
Always test with your own email before sending to students:
```
Recipient email: your@email.com
```

### 3. Read the Configuration Summary
Option 5 shows a summary before starting. Review it carefully!

### 4. Cancel Anytime
Type `no` when asked to confirm. No changes will be made.

### 5. Use Descriptive Filters
Be specific with labels and subjects to avoid exporting wrong emails.

---

## Troubleshooting

### "No filters specified"
**Solution:** Enter at least a label or subject, or type `yes` to export all emails

### "Cancelled by user"
**Solution:** This is normal. You typed `no` to cancel the operation.

### "gmailagent not found"
**Solution:** Install the package: `pip install -e .`

### Want to change configuration?
**Solution:** Cancel (type `no`) and restart. The orchestrator will ask again.

---

## Comparison Table

| Feature | Old Version | New Version |
|---------|-------------|-------------|
| **Input Method** | Manual parameters | Interactive prompts |
| **Examples** | None | Provided for each input |
| **Defaults** | Had to specify | Press Enter to use |
| **Confirmation** | None | Asked before critical actions |
| **Configuration Review** | No | Shows summary before starting |
| **Error Prevention** | Limited | Validates before running |
| **User Guidance** | Minimal | Step-by-step with examples |

---

## Run the Orchestrator

```bash
cd C:\AIDevelopmentCourse\L-19\EmailSkillAgents
python orchestrator.py
```

Follow the interactive prompts and enjoy the streamlined workflow!

---

For more details, see:
- `ORCHESTRATOR_README.md` - Full documentation
- `ORCHESTRATOR_QUICKSTART.md` - Quick reference
- `HOW_TO_RUN_ORCHESTRATOR.md` - Step-by-step guide
