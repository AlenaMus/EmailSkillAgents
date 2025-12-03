# How to Run the Orchestrator

## Quick Start

### 1. Open Terminal/Command Prompt

```bash
cd C:\AIDevelopmentCourse\L-19\EmailSkillAgents
```

### 2. Run the Orchestrator

```bash
python orchestrator.py
```

You'll see the menu:

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

### 3. Select an Option

Type a number (1-7) and press Enter.

---

## Testing the Reset Function

### Method 1: Using the Menu

```bash
python orchestrator.py
```

Then:
1. Type `6` and press Enter
2. Type `yes` to confirm
3. All outputs will be deleted

### Method 2: Using the Test Script

```bash
python test_reset.py
```

This will:
- Create test files in all output directories
- Show files before reset (21 files)
- Perform the reset
- Show files after reset (0 files)

---

## Example Session

### Reset All Files

```
$ python orchestrator.py

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

## What Gets Deleted?

When you run **Option 6 (Reset)**, the orchestrator deletes:

### Files
- `exports/homework_emails.xlsx` (Agent 1 output)
- `output/homework_emails_graded.xlsx` (Agent 2 output)
- `greetings_results/homework_emails_with_greetings.xlsx` (Agent 3 output)
- All files in `exports/` directory
- All files in `output/` directory
- All files in `greetings_results/` directory
- All files in `email_drafts/` directory

### What's Preserved
- Directory structure (all folders remain)
- Source code and agent implementations
- Configuration files
- Credentials (token.json, credentials.json)

---

## Running Individual Agents

### Option 1: Email Generator
```
Select option (1-7): 1
```
Guides you through exporting emails with GmailAgent.

### Option 2: Repository Analyzer
```
Select option (1-7): 2
```
Analyzes repos from the exported emails.

**Requirement:** Agent 1 must have run successfully.

### Option 3: Greetings Agent
```
Select option (1-7): 3
```
Adds personalized feedback based on grades.

**Requirement:** Agent 2 must have run successfully.

### Option 4: Evaluation Sender
```
Select option (1-7): 4

Default recipient: alona.musiyko@gmail.com
Enter recipient email (or press Enter for default): your@email.com
```
Creates email drafts and sends to specified email.

**Requirement:** Agent 3 must have run successfully.

---

## Running All Agents at Once

```
Select option (1-7): 5

Default recipient: alona.musiyko@gmail.com
Enter recipient email (or press Enter for default): test@example.com
```

This runs all 4 agents in sequence:
1. Email Generator (manual step)
2. Repository Analyzer (automatic)
3. Greetings Agent (automatic)
4. Evaluation Sender (automatic)

---

## Status Messages

The orchestrator uses these status indicators:

- `[OK]` - Operation successful
- `[ERROR]` - Operation failed
- `[INFO]` - Informational message
- `[WARN]` - Warning message

---

## Exiting the Orchestrator

```
Select option (1-7): 7

[INFO] Exiting orchestrator. Goodbye!
```

Or press `Ctrl+C` at any time to exit.

---

## Troubleshooting

### "Input file not found"
**Solution:** Run the previous agent first (agents must run in order: 1→2→3→4)

### "Input not ready: X rows not ready"
**Solution:** Previous agent didn't complete successfully. Re-run that agent.

### "Agent X failed"
**Solution:** Check the error details. Verify the agent is properly installed.

### Want to start fresh?
**Solution:** Use Option 6 (Reset) to clean all outputs, then start from Option 1 or 5.

---

## Tips

1. **Always test first**: Use your own email when testing Option 4 or 5
2. **Reset between runs**: Use Option 6 before starting a new grading cycle
3. **Watch the status messages**: They guide you through the process
4. **Run sequentially**: Agents must run in order (1→2→3→4)

---

For more details, see `ORCHESTRATOR_README.md` or `ORCHESTRATOR_QUICKSTART.md`
