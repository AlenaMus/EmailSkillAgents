# Orchestrator Quick Start Guide

**Fast reference for running the Email Skill Agents Orchestrator**

---

## Start Orchestrator

```bash
cd C:\AIDevelopmentCourse\L-19\EmailSkillAgents
python orchestrator.py
```

---

## Quick Reference

### 1️⃣ Run Email Generator
- **Use:** Export homework emails from Gmail
- **Command:** Option 1
- **Output:** `exports/homework_emails.xlsx`
- **Next:** Run Option 2

### 2️⃣ Run Repository Analyzer
- **Use:** Analyze repos and calculate grades
- **Command:** Option 2
- **Input:** `exports/homework_emails.xlsx`
- **Output:** `output/homework_emails_graded.xlsx`
- **Next:** Run Option 3

### 3️⃣ Run Greetings Agent
- **Use:** Add personalized feedback
- **Command:** Option 3
- **Input:** `output/homework_emails_graded.xlsx`
- **Output:** `greetings_results/homework_emails_with_greetings.xlsx`
- **Next:** Run Option 4

### 4️⃣ Create Email Drafts
- **Use:** Generate and send feedback emails
- **Command:** Option 4
- **Input:** `greetings_results/homework_emails_with_greetings.xlsx`
- **Output:** `email_drafts/*.html`
- **Default Email:** alona.musiyko@gmail.com

### 5️⃣ Run ALL Agents
- **Use:** Complete workflow (1→2→3→4)
- **Command:** Option 5
- **Best for:** Production runs
- **Time:** Depends on number of repos

### 6️⃣ Reset
- **Use:** Clean all outputs
- **Command:** Option 6
- **Deletes:** All intermediate files
- **Use before:** Starting fresh run

---

## Typical Workflow

### First Time Setup

```bash
# 1. Export emails with GmailAgent
gmailagent export --label "homework" --subject "lesson19"

# 2. Start orchestrator
python orchestrator.py

# 3. Select Option 5 (Run All)
# 4. Enter email or press Enter for default
# 5. Wait for completion
```

### Subsequent Runs

```bash
# 1. Reset previous run
python orchestrator.py
Select: 6 (Reset)
Confirm: yes

# 2. Run all agents
Select: 5 (Run All)
Enter email: your@email.com

# 3. Done!
```

---

## Common Commands

### Test Run (Send to Yourself)

```bash
python orchestrator.py
Select: 5
Email: your.email@test.com
```

### Run Individual Agent

```bash
python orchestrator.py
Select: 2  # Run Repository Analyzer only
```

### Clean and Restart

```bash
python orchestrator.py
Select: 6  # Reset
Confirm: yes
Select: 5  # Run all
```

---

## Status Indicators

| Symbol | Meaning |
|--------|---------|
| ✓ | Success |
| ✗ | Error |
| ⚠ | Warning |
| ℹ | Info |

---

## Error Quick Fixes

**"Input file not found"**
→ Run previous agent first

**"Input not ready"**
→ Previous agent failed, re-run it

**"No Excel files found"**
→ Run GmailAgent to export emails

**"Agent X failed"**
→ Check error details, verify installation

---

## Default Paths

```
exports/homework_emails.xlsx                      # Agent 1 output
output/homework_emails_graded.xlsx                # Agent 2 output
greetings_results/homework_emails_with_greetings.xlsx  # Agent 3 output
email_drafts/*.html                               # Agent 4 output
```

---

## Tips

✅ Use Option 5 for full workflow
✅ Test with your email first (Option 4)
✅ Reset between grading cycles (Option 6)
✅ Watch status messages for errors

---

For detailed documentation, see `ORCHESTRATOR_README.md`
