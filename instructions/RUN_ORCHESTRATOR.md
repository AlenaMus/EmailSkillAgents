# How to Run the Orchestrator

## 🚀 Start the Orchestrator

Open your terminal and run:

```bash
cd C:\AIDevelopmentCourse\L-19\EmailSkillAgents
python orchestrator.py
```

You'll see this menu:

```
======================================================================
  EMAIL SKILL AGENTS ORCHESTRATOR
======================================================================

>> Automated Homework Grading Workflow

1. Run Email Generator (GmailAgent)
2. Run Repository Analyzer (on existing input)
3. Run Greetings Agent (on existing output)
4. Create Email Drafts and Send (Evaluation Sender)
5. Run ALL Agents (1 -> 2 -> 3 -> 4)
6. Reset - Clean All Inputs/Outputs
7. Exit

----------------------------------------------------------------------
Select option (1-7):
```

---

## 📋 Option Examples

### Option 1: Run Email Generator

**What it does:** Exports emails from Gmail

**Interaction:**
```
Select option (1-7): 1

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

[INFO] Filter by label: homework
[INFO] Filter by subject: lesson19
[INFO] Running GmailAgent...
Command: gmailagent export --label homework --subject lesson19
...
```

---

### Option 4: Create Email Drafts

**What it does:** Sends email drafts to students

**Interaction:**
```
Select option (1-7): 4

======================================================================
  Agent 4: Evaluation Gmail Sender - Send Feedback
======================================================================

[OK] Input ready: All 30 rows ready

Default recipient: alona.musiyko@gmail.com
Enter a recipient email to send all drafts to that address (for testing)
Or press Enter to use the default email

Recipient email: mytest@example.com
[INFO] Recipient: mytest@example.com

Send email drafts to mytest@example.com? (yes/no): yes

[INFO] Running Evaluation Gmail Sender...
[OK] Email drafts created successfully
[INFO] Drafts saved to: email_drafts/

Press Enter to continue...
```

---

### Option 5: Run ALL Agents

**What it does:** Runs complete workflow (1→2→3→4)

**Interaction:**
```
Select option (1-7): 5

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

Recipient email: test@example.com

======================================================================
CONFIGURATION SUMMARY
======================================================================
Gmail Label:    homework
Subject Filter: Assignment 19
Recipient:      test@example.com
======================================================================

Start processing with this configuration? (yes/no): yes

[Then runs all 4 agents automatically]
```

---

### Option 6: Reset

**What it does:** Cleans all outputs

**Interaction:**
```
Select option (1-7): 6

[WARN] This will delete all outputs. Continue? (yes/no): yes

======================================================================
  Reset - Cleaning All Inputs and Outputs
======================================================================
[OK] Deleted: homework_emails.xlsx
[OK] Deleted: homework_emails_graded.xlsx
[OK] Deleted: homework_emails_with_greetings.xlsx
[OK] Deleted 21 files
[OK] Deleted 0 directories
[INFO] All outputs cleaned. Ready for fresh run.

Press Enter to continue...
```

---

## 💡 Tips

### 1. Test First
Always test with your own email before sending to students:
```
Recipient email: your@email.com
```

### 2. Use Option 5 for Complete Workflow
For production, use Option 5 to run all agents at once.

### 3. Reset Between Runs
Use Option 6 to clean up before starting a new grading cycle.

### 4. Press Enter for Defaults
Most prompts have defaults - just press Enter to use them.

### 5. You Can Cancel Anytime
Type `no` when asked to confirm, and the operation will be cancelled.

---

## 🎯 Quick Workflows

### First-Time Setup
```bash
# 1. Run orchestrator
python orchestrator.py

# 2. Select Option 1 (Email Generator)
# 3. Enter label and subject
# 4. Then select Option 5 (Run All)
# 5. Follow the prompts
```

### Regular Use
```bash
# 1. Run orchestrator
python orchestrator.py

# 2. Select Option 5 (Run All)
# 3. Configure filters and email
# 4. Confirm and wait
```

### Testing
```bash
# 1. Run orchestrator
python orchestrator.py

# 2. Select Option 4 (Evaluation Sender only)
# 3. Enter your test email
# 4. Confirm
```

### Cleanup
```bash
# 1. Run orchestrator
python orchestrator.py

# 2. Select Option 6 (Reset)
# 3. Confirm: yes
```

---

## ❓ Troubleshooting

### "Input file not found"
**Cause:** Previous agent hasn't run yet

**Solution:** Run agents in order (1→2→3→4) or use Option 5

### "Input not ready"
**Cause:** Previous agent didn't complete successfully

**Solution:** Re-run the previous agent

### "gmailagent not found"
**Cause:** Package not installed

**Solution:**
```bash
pip install -e .
```

### Want to start fresh?
**Solution:** Use Option 6 (Reset)

---

## 📞 Need Help?

**Documentation:**
- Main README: `README.md`
- Orchestrator Guide: `orchestrator_docs/instructions/ORCHESTRATOR_README.md`
- Interactive Guide: `orchestrator_docs/instructions/ORCHESTRATOR_INTERACTIVE_GUIDE.md`
- Quick Start: `orchestrator_docs/instructions/ORCHESTRATOR_QUICKSTART.md`

**Test Scripts:**
```bash
# Demo interactive features
python tests/test_interactive_menu.py

# Test reset
python tests/test_reset.py
```

---

## 🎉 Ready to Start!

Just run:
```bash
python orchestrator.py
```

And follow the interactive prompts! The orchestrator will guide you through each step.

---

**Happy grading!** 🚀
