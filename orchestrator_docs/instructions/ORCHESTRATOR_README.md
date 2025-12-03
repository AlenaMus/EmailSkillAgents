# Email Skill Agents Orchestrator

**Version:** 1.0.0
**Purpose:** Unified workflow manager for the 4-agent email grading system

---

## Overview

The **Orchestrator** is a command-line menu system that manages the entire email grading workflow, coordinating all 4 agents in the correct sequence with status validation.

### Agent Workflow

```
1. GmailAgent           → Export homework emails to Excel
                        → Sets Status = "ready"
                        ↓
2. Repository Analyzer  → Checks Status = "ready"
                        → Analyzes repos, calculates grades
                        → Sets Status = "ready"
                        ↓
3. Greetings Agent      → Checks Status = "ready"
                        → Adds personalized feedback
                        → Sets Status = "ready"
                        ↓
4. Evaluation Sender    → Checks Status = "ready"
                        → Creates and sends email drafts
```

---

## Features

✅ **Menu-Driven Interface** - Simple numbered options
✅ **Status Validation** - Ensures agents run in correct order
✅ **Individual Agent Execution** - Run any agent independently
✅ **Full Pipeline Execution** - Run all agents synchronously
✅ **Reset Functionality** - Clean all outputs for fresh run
✅ **Error Handling** - Clear error messages with guidance
✅ **Default Email Configuration** - Pre-configured test recipient

---

## Installation

### Prerequisites

Ensure all 4 agents are installed:

```bash
# Install all dependencies
pip install -r requirements.txt

# Verify agents are accessible
python -m gmailagent --help
python -m repo_analyzer.cli --help
python -m greetings_grades_agent.cli --help
python -m evaluationAgent.cli --help
```

### No Installation Needed

The orchestrator is a standalone script. Just run it directly:

```bash
python orchestrator.py
```

---

## Usage

### Starting the Orchestrator

```bash
python orchestrator.py
```

You'll see the main menu:

```
======================================================================
  EMAIL SKILL AGENTS ORCHESTRATOR
======================================================================

📧 Automated Homework Grading Workflow

1. Run Email Generator (GmailAgent)
2. Run Repository Analyzer (on existing input)
3. Run Greetings Agent (on existing output)
4. Create Email Drafts and Send (Evaluation Sender)
5. Run ALL Agents (1 → 2 → 3 → 4)
6. Reset - Clean All Inputs/Outputs
7. Exit

----------------------------------------------------------------------
Select option (1-7):
```

---

## Menu Options

### Option 1: Run Email Generator (GmailAgent)

**Purpose:** Export homework emails from Gmail to Excel

**What it does:**
- Prompts you to run `gmailagent export` manually
- Finds the most recent Excel file in `exports/`
- Copies it to `exports/homework_emails.xlsx`
- Validates Status column is set to "ready"

**When to use:** Start of the workflow, or to update the email export

**Example:**
```bash
Select option (1-7): 1

======================================================================
  Agent 1: GmailAgent - Export Homework Emails
======================================================================

ℹ Running GmailAgent...

GmailAgent will export emails to Excel.
You'll need to specify filters (label, sender, subject, etc.)

Example command:
  gmailagent export --label 'homework' --subject 'lesson19'

Please run the command manually or press Enter to continue...

Press Enter after you've exported emails with GmailAgent...
```

**Output:** `exports/homework_emails.xlsx` with Status = "ready"

---

### Option 2: Run Repository Analyzer

**Purpose:** Analyze GitHub repositories and calculate grades

**What it does:**
- Checks if `exports/homework_emails.xlsx` exists
- Validates Status = "ready" in input file
- Runs repository analyzer
- Creates `output/homework_emails_graded.xlsx`
- Sets Status = "ready" for next agent

**When to use:** After Agent 1 completes

**Requirements:**
- Agent 1 must have run successfully
- Input file must have Status = "ready"

**Example:**
```bash
Select option (1-7): 2

======================================================================
  Agent 2: Repository Analyzer - Analyze Repositories
======================================================================

✓ Input ready: All 30 rows ready
ℹ Running Repository Analyzer...
✓ Repository analysis completed
✓ Output status: All 30 rows ready
```

**Output:** `output/homework_emails_graded.xlsx` with grades and Status = "ready"

---

### Option 3: Run Greetings Agent

**Purpose:** Add personalized motivational feedback based on grades

**What it does:**
- Checks if `output/homework_emails_graded.xlsx` exists
- Validates Status = "ready" in input file
- Runs greetings agent
- Creates `greetings_results/homework_emails_with_greetings.xlsx`
- Sets Status = "ready" for next agent

**When to use:** After Agent 2 completes

**Requirements:**
- Agent 2 must have run successfully
- Input file must have Status = "ready"

**Example:**
```bash
Select option (1-7): 3

======================================================================
  Agent 3: Personalized Greetings Agent - Add Feedback
======================================================================

✓ Input ready: All 30 rows ready
ℹ Running Personalized Greetings Agent...
✓ Greetings generation completed
✓ Output status: All 30 rows ready
```

**Output:** `greetings_results/homework_emails_with_greetings.xlsx` with personalized greetings and Status = "ready"

---

### Option 4: Create Email Drafts and Send

**Purpose:** Generate email drafts and send to students (or test email)

**What it does:**
- Checks if `greetings_results/homework_emails_with_greetings.xlsx` exists
- Validates Status = "ready" in input file
- Prompts for recipient email (default: `alona.musiyko@gmail.com`)
- Runs evaluation sender
- Creates HTML email drafts in `email_drafts/`

**When to use:** After Agent 3 completes

**Requirements:**
- Agent 3 must have run successfully
- Input file must have Status = "ready"

**Example:**
```bash
Select option (1-7): 4

======================================================================
  Agent 4: Evaluation Gmail Sender - Send Feedback
======================================================================

Default recipient: alona.musiyko@gmail.com
Enter recipient email (or press Enter for default):

✓ Input ready: All 30 rows ready
ℹ Recipient: alona.musiyko@gmail.com
ℹ Running Evaluation Gmail Sender...
✓ Email drafts created successfully
ℹ Drafts saved to: email_drafts/
```

**Output:** HTML email drafts in `email_drafts/` directory

---

### Option 5: Run ALL Agents (Synchronously)

**Purpose:** Run the complete workflow from start to finish

**What it does:**
- Runs Agent 1 (GmailAgent)
- Waits for completion and validates
- Runs Agent 2 (Repository Analyzer)
- Waits for completion and validates
- Runs Agent 3 (Greetings Agent)
- Waits for completion and validates
- Runs Agent 4 (Evaluation Sender)
- Reports final status

**When to use:**
- First-time setup after exporting emails
- Re-running the entire workflow
- After making changes to any agent

**Requirements:**
- Fresh start (or after running Option 6 to reset)
- Gmail authentication already set up

**Example:**
```bash
Select option (1-7): 5

======================================================================
  Running All Agents Synchronously
======================================================================

Default recipient: alona.musiyko@gmail.com
Enter recipient email (or press Enter for default): test@example.com

[Agent 1 runs...]
[Agent 2 runs...]
[Agent 3 runs...]
[Agent 4 runs...]

======================================================================
  All Agents Completed Successfully!
======================================================================
```

**Output:** Complete workflow from emails to sent feedback

---

### Option 6: Reset - Clean All Inputs/Outputs

**Purpose:** Delete all intermediate and output files for fresh start

**What it does:**
- Deletes `exports/homework_emails.xlsx`
- Deletes `output/homework_emails_graded.xlsx`
- Deletes `greetings_results/homework_emails_with_greetings.xlsx`
- Cleans all files in `exports/`, `output/`, `greetings_results/`, `email_drafts/`
- Keeps directory structure intact

**When to use:**
- Before starting a new grading cycle
- After errors that corrupt output files
- When testing the workflow

**Example:**
```bash
Select option (1-7): 6

======================================================================
  Reset - Cleaning All Inputs and Outputs
======================================================================

⚠ This will delete all outputs. Continue? (yes/no): yes

✓ Deleted: homework_emails.xlsx
✓ Deleted: homework_emails_graded.xlsx
✓ Deleted: homework_emails_with_greetings.xlsx
✓ Deleted 45 files
✓ Deleted 0 directories
ℹ All outputs cleaned. Ready for fresh run.
```

---

### Option 7: Exit

**Purpose:** Exit the orchestrator

**What it does:**
- Cleanly exits the program
- Preserves all files and state

---

## Status Validation

The orchestrator enforces proper sequencing using the **Status** column:

### How It Works

1. **Agent 1** sets Status = "ready" when export completes
2. **Agent 2** checks Status = "ready" before running, then sets Status = "ready" after completion
3. **Agent 3** checks Status = "ready" before running, then sets Status = "ready" after completion
4. **Agent 4** checks Status = "ready" before running

### Error Messages

If you try to run an agent out of order:

```
✗ Input not ready: 30/30 rows not ready (Status != 'ready')
ℹ Please run Agent 1 first
```

Or:

```
✗ Cannot process: 15 row(s) have Status != 'ready'.
  Previous agent (Repository Analyzer) must complete successfully before this agent can run.
```

---

## File Locations

### Input/Output Paths

| Agent | Input | Output |
|-------|-------|--------|
| **Agent 1** | Gmail | `exports/homework_emails.xlsx` |
| **Agent 2** | `exports/homework_emails.xlsx` | `output/homework_emails_graded.xlsx` |
| **Agent 3** | `output/homework_emails_graded.xlsx` | `greetings_results/homework_emails_with_greetings.xlsx` |
| **Agent 4** | `greetings_results/homework_emails_with_greetings.xlsx` | `email_drafts/*.html` |

### Directory Structure

```
EmailSkillAgents/
├── orchestrator.py                 # This orchestrator
├── exports/                        # Agent 1 output
│   └── homework_emails.xlsx
├── output/                         # Agent 2 output
│   └── homework_emails_graded.xlsx
├── greetings_results/              # Agent 3 output
│   └── homework_emails_with_greetings.xlsx
└── email_drafts/                   # Agent 4 output
    ├── email_1_grade_100_test_at_example_com.html
    ├── email_2_grade_75_test_at_example_com.html
    └── summary.txt
```

---

## Configuration

### Default Email

The default recipient email is configured in `orchestrator.py`:

```python
DEFAULT_EMAIL = "alona.musiyko@gmail.com"
```

To change the default:

1. Edit `orchestrator.py`
2. Update line: `DEFAULT_EMAIL = "your.email@example.com"`
3. Save and restart orchestrator

Or specify a different email when running Agent 4 or Option 5.

---

## Troubleshooting

### Issue: "Input file not found"

**Cause:** Previous agent hasn't run yet

**Solution:** Run agents in order (1 → 2 → 3 → 4) or use Option 5

---

### Issue: "Input not ready: X rows not ready"

**Cause:** Previous agent didn't complete successfully

**Solution:**
1. Check previous agent's output file
2. Verify Status column exists and = "ready"
3. Re-run previous agent if needed
4. Use Option 6 to reset and start fresh

---

### Issue: "Agent X failed"

**Cause:** Agent encountered an error during execution

**Solution:**
1. Check error details in the output
2. Verify agent is properly installed
3. Check log files for specific errors
4. Run agent manually to diagnose:
   ```bash
   python -m repo_analyzer.cli analyze --input exports/homework_emails.xlsx
   ```

---

### Issue: "No Excel files found in exports directory"

**Cause:** Agent 1 (GmailAgent) hasn't exported any files

**Solution:**
1. Run `gmailagent export` manually with proper filters
2. Verify files are created in `exports/` directory
3. Press Enter in orchestrator to detect files

---

## Best Practices

### 1. Always Use Option 5 for Full Workflow

For production runs, use Option 5 to run all agents synchronously. This ensures:
- Proper sequencing
- Status validation at each step
- Complete workflow execution

### 2. Test with Option 4 First

Before sending to all students:
1. Use your own email as recipient
2. Review generated HTML drafts
3. Verify formatting and content
4. Then run for real students

### 3. Reset Between Grading Cycles

Use Option 6 to clean up between different homework assignments:
```bash
# After grading Homework 17
Select option: 6  # Reset

# Start fresh for Homework 18
Select option: 5  # Run all
```

### 4. Monitor Status Messages

Watch for:
- ✓ Success messages (all good)
- ⚠ Warnings (potential issues)
- ✗ Errors (requires action)
- ℹ Info messages (helpful context)

---

## Advanced Usage

### Running Individual Agents Manually

If you need more control, run agents directly:

```bash
# Agent 2: Repository Analyzer
python -m repo_analyzer.cli analyze \
  --input exports/homework_emails.xlsx \
  --output output/homework_emails_graded.xlsx

# Agent 3: Greetings Agent
python -m greetings_grades_agent.cli generate-greetings \
  --input output/homework_emails_graded.xlsx \
  --output greetings_results/homework_emails_with_greetings.xlsx

# Agent 4: Evaluation Sender
python -m evaluationAgent.cli create-drafts \
  --input greetings_results/homework_emails_with_greetings.xlsx \
  --to test@example.com
```

### Custom Email for Testing

When running Option 4 or 5, you can specify any email:

```bash
Select option (1-7): 4

Default recipient: alona.musiyko@gmail.com
Enter recipient email (or press Enter for default): john.doe@test.com
```

All emails will be sent to `john.doe@test.com` instead of actual students.

---

## Error Codes

| Code | Meaning | Solution |
|------|---------|----------|
| File not found | Input file missing | Run previous agent |
| Status not ready | Previous agent incomplete | Re-run previous agent |
| Agent failed | Execution error | Check error details, verify installation |
| No Excel files | GmailAgent not run | Export emails with GmailAgent |

---

## FAQ

### Q: Can I skip agents?

**A:** No. Agents must run in sequence (1 → 2 → 3 → 4) because each depends on the previous agent's output with Status = "ready".

### Q: What if I need to re-run Agent 2 only?

**A:** You can run individual agents (Options 2-4) as long as their input is ready. The orchestrator validates Status before running.

### Q: How do I change the default email?

**A:** Edit `orchestrator.py` and change `DEFAULT_EMAIL = "your.email@example.com"`, or specify a different email when prompted.

### Q: What does Option 6 (Reset) delete?

**A:** All files in `exports/`, `output/`, `greetings_results/`, and `email_drafts/`. Directories are kept but emptied.

### Q: Can I run the orchestrator multiple times?

**A:** Yes! Each run is independent. Use Option 6 to reset between runs.

---

## Support

For issues or questions:

1. Check error messages in orchestrator output
2. Review individual agent READMEs:
   - `README.md` (GmailAgent)
   - `repo_analyzer/README.md`
   - `greetings_grades_agent/README.md`
   - `evaluationAgent/README.md`
3. Run agents manually to diagnose issues
4. Check log files for detailed errors

---

## Version History

### v1.0.0 (2024-12-02)

- Initial release
- Menu-driven interface with 7 options
- Status validation for agent coordination
- Individual and synchronous execution modes
- Reset functionality
- Default email configuration
- Error handling and validation

---

**Orchestrator v1.0.0** - Unified workflow management for email grading automation
