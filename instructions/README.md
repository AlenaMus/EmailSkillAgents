# Email Skill Agents - Automated Homework Grading System

**Version:** 2.0.0
**Course:** AI Development Course - Lesson 19
**Purpose:** Automated end-to-end email-based homework grading workflow

---

## 📋 Overview

This project implements a complete automated grading workflow using 4 specialized agents that work together to grade student homework submissions via email.

### Workflow

```
Gmail → Export Emails → Analyze Repos → Add Feedback → Send Results
  ↓           ↓              ↓              ↓             ↓
Agent 1    Agent 2        Agent 3        Agent 4    Complete!
```

---

## 🚀 Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the Orchestrator
```bash
python orchestrator.py
```

### 3. Follow Interactive Prompts
The orchestrator will guide you through:
- Email filtering options
- Recipient configuration
- Agent execution
- Status monitoring

---

## 📁 Project Structure

```
EmailSkillAgents/
│
├── orchestrator.py                    # Main orchestrator program
│
├── gmailagent/                        # Agent 1: Gmail Email Exporter
│   ├── instructions/                  # Documentation
│   │   ├── PRD-GmailAgent.md         # Product requirements
│   │   └── README.md → ../README.md  # Agent documentation
│   ├── auth.py
│   ├── gmail_client.py
│   ├── url_extractor.py
│   ├── excel_exporter.py
│   └── cli.py
│
├── repo_analyzer/                     # Agent 2: Repository Analyzer
│   ├── instructions/                  # Documentation
│   │   ├── PRD-RepositoryAnalyzer.md
│   │   ├── REPO_ANALYZER_ARCHITECTURE.md
│   │   ├── REPO_ANALYZER_SUMMARY.md
│   │   ├── REPO_ANALYZER_IMPLEMENTATION_REPORT.md
│   │   ├── QUICKSTART_REPO_ANALYZER.md
│   │   └── README.md → ../README.md
│   ├── analyzer.py
│   ├── metrics_calculator.py
│   ├── excel_manager.py
│   ├── repo_manager.py
│   └── cli.py
│
├── greetings_grades_agent/            # Agent 3: Personalized Greetings
│   ├── instructions/                  # Documentation
│   │   ├── PRD-PersonalizedGreetingsAgent.md
│   │   ├── GREETINGS_AGENT_SUMMARY.md
│   │   ├── GREETINGS_IMPLEMENTATION_REPORT.md
│   │   ├── QUICKSTART_GREETINGS.md
│   │   └── README.md → ../README.md
│   ├── skills/                        # Persona implementations
│   │   ├── donald_trump.py
│   │   ├── dudi_amsalem.py
│   │   ├── shahar_hasson.py
│   │   └── benjamin_netanyahu.py
│   ├── greeting_generator.py
│   ├── persona_manager.py
│   ├── excel_manager.py
│   └── cli.py
│
├── evaluationAgent/                   # Agent 4: Email Sender
│   ├── instructions/                  # Documentation
│   │   ├── PRD-EvaluationGmailSender.md
│   │   ├── EVALUATION_AGENT_SUMMARY.md
│   │   ├── EVALUATION_AGENT_IMPLEMENTATION_REPORT.md
│   │   ├── QUICKSTART_EVALUATION_SENDER.md
│   │   └── README.md → ../README.md
│   ├── email_sender.py
│   ├── excel_reader.py
│   ├── gmail_client.py
│   ├── email_template.py
│   └── cli.py
│
├── orchestrator_docs/                 # Orchestrator Documentation
│   └── instructions/
│       ├── ORCHESTRATOR_README.md
│       ├── ORCHESTRATOR_QUICKSTART.md
│       ├── ORCHESTRATOR_INTERACTIVE_GUIDE.md
│       ├── ORCHESTRATOR_CHANGELOG.md
│       ├── HOW_TO_RUN_ORCHESTRATOR.md
│       └── UPDATES_SUMMARY.md
│
├── docs/                              # General Project Documentation
│   ├── PROJECT_SUMMARY.md
│   ├── PROJECT_STRUCTURE.md
│   ├── INSTALLATION.md
│   ├── QUICKSTART.md
│   ├── IMPLEMENTATION_CHECKLIST.md
│   ├── IMPLEMENTATION_REPORT.md
│   ├── GMAIL_CREDENTIALS_GUIDE.md
│   ├── HOW_TO_DOWNLOAD_CREDENTIALS.md
│   ├── FIX_REDIRECT_URI.md
│   ├── RUN_FROM_WINDOWS.md
│   ├── WINDOWS_SETUP_COMPLETE.md
│   └── EXPORTS_FOLDER_STRUCTURE.md
│
├── tests/                             # Test Scripts
│   ├── test_reset.py
│   ├── test_interactive_menu.py
│   ├── test_greetings_agent.py
│   ├── test_grading_formula.py
│   ├── verify_greetings.py
│   ├── demo_full_greetings.py
│   └── check_output.py
│
├── exports/                           # Agent 1 Output
├── output/                            # Agent 2 Output
├── greetings_results/                 # Agent 3 Output
└── email_drafts/                      # Agent 4 Output
```

---

## 🤖 The Four Agents

### Agent 1: GmailAgent
**Purpose:** Export homework emails from Gmail to Excel

**Documentation:**
- 📄 `gmailagent/instructions/PRD-GmailAgent.md`
- 📘 `gmailagent/README.md`

**Quick Start:**
```bash
# Interactive mode (via orchestrator)
python orchestrator.py
Select: 1

# Manual mode
gmailagent export --label "homework" --subject "lesson19"
```

**Output:** `exports/homework_emails.xlsx` with Status = "ready"

---

### Agent 2: Repository Analyzer
**Purpose:** Analyze GitHub repositories and calculate grades

**Documentation:**
- 📄 `repo_analyzer/instructions/PRD-RepositoryAnalyzer.md`
- 📘 `repo_analyzer/instructions/README.md`
- 📊 `repo_analyzer/instructions/REPO_ANALYZER_ARCHITECTURE.md`
- 🚀 `repo_analyzer/instructions/QUICKSTART_REPO_ANALYZER.md`

**Quick Start:**
```bash
# Interactive mode (via orchestrator)
python orchestrator.py
Select: 2

# Manual mode
python -m repo_analyzer.cli analyze --input exports/homework_emails.xlsx
```

**Output:** `output/homework_emails_graded.xlsx` with grades and Status = "ready"

---

### Agent 3: Personalized Greetings Agent
**Purpose:** Add motivational feedback based on grades

**Documentation:**
- 📄 `greetings_grades_agent/instructions/PRD-PersonalizedGreetingsAgent.md`
- 📘 `greetings_grades_agent/instructions/README.md`
- 🚀 `greetings_grades_agent/instructions/QUICKSTART_GREETINGS.md`

**Features:**
- 4 Personas: Trump, Dudi, Shahar, Netanyahu
- Grade-based feedback selection
- Hebrew and English support

**Quick Start:**
```bash
# Interactive mode (via orchestrator)
python orchestrator.py
Select: 3

# Manual mode
python -m greetings_grades_agent.cli generate-greetings \
  --input output/homework_emails_graded.xlsx
```

**Output:** `greetings_results/homework_emails_with_greetings.xlsx` with Status = "ready"

---

### Agent 4: Evaluation Gmail Sender
**Purpose:** Send personalized feedback emails to students

**Documentation:**
- 📄 `evaluationAgent/instructions/PRD-EvaluationGmailSender.md`
- 📘 `evaluationAgent/instructions/README.md`
- 🚀 `evaluationAgent/instructions/QUICKSTART_EVALUATION_SENDER.md`

**Quick Start:**
```bash
# Interactive mode (via orchestrator)
python orchestrator.py
Select: 4

# Manual mode
python -m evaluationAgent.cli create-drafts \
  --input greetings_results/homework_emails_with_greetings.xlsx \
  --to test@example.com
```

**Output:** HTML email drafts in `email_drafts/`

---

## 🎮 Orchestrator

The **orchestrator** is a menu-driven system that coordinates all 4 agents.

**Documentation:**
- 📘 `orchestrator_docs/instructions/ORCHESTRATOR_README.md` - Complete guide
- 🚀 `orchestrator_docs/instructions/ORCHESTRATOR_QUICKSTART.md` - Quick reference
- 💡 `orchestrator_docs/instructions/ORCHESTRATOR_INTERACTIVE_GUIDE.md` - Interactive features
- 📋 `orchestrator_docs/instructions/ORCHESTRATOR_CHANGELOG.md` - What's new

### Menu Options

```
1. Run Email Generator (GmailAgent)
2. Run Repository Analyzer
3. Run Greetings Agent
4. Create Email Drafts and Send
5. Run ALL Agents (1 → 2 → 3 → 4)
6. Reset - Clean All Inputs/Outputs
7. Exit
```

### Run Orchestrator
```bash
python orchestrator.py
```

### Interactive Features
- **Option 1:** Asks for email filters (label, subject)
- **Option 4:** Asks for recipient email with confirmation
- **Option 5:** Gathers all configuration before starting
- **Option 6:** Cleans all outputs for fresh run

---

## 🔄 Status Column Coordination

All agents coordinate using a **Status** column to ensure proper sequencing:

| Agent | Checks Status | Sets Status |
|-------|---------------|-------------|
| **Agent 1** | - | ✓ "ready" |
| **Agent 2** | ✓ "ready" | ✓ "ready" |
| **Agent 3** | ✓ "ready" | ✓ "ready" |
| **Agent 4** | ✓ "ready" | - |

**Benefits:**
- Prevents running agents out of order
- Ensures data is ready before processing
- Clear error messages if prerequisites not met

---

## 📚 Documentation Index

### Getting Started
- 📘 `docs/QUICKSTART.md` - Fast setup guide
- 📄 `docs/INSTALLATION.md` - Detailed installation
- 🪟 `docs/RUN_FROM_WINDOWS.md` - Windows-specific setup

### Agent Documentation
Each agent has its own `instructions/` folder with:
- **PRD** - Product Requirements Document
- **README** - Usage guide
- **QUICKSTART** - Fast reference
- **ARCHITECTURE** - Technical details (where applicable)
- **IMPLEMENTATION REPORT** - Development notes (where applicable)

### Orchestrator Documentation
- 📘 `orchestrator_docs/instructions/ORCHESTRATOR_README.md`
- 🚀 `orchestrator_docs/instructions/ORCHESTRATOR_QUICKSTART.md`
- 💡 `orchestrator_docs/instructions/ORCHESTRATOR_INTERACTIVE_GUIDE.md`
- 📝 `orchestrator_docs/instructions/HOW_TO_RUN_ORCHESTRATOR.md`
- 📋 `orchestrator_docs/instructions/ORCHESTRATOR_CHANGELOG.md`
- ✅ `orchestrator_docs/instructions/UPDATES_SUMMARY.md`

### Setup Guides
- 🔑 `docs/GMAIL_CREDENTIALS_GUIDE.md` - Get Gmail API credentials
- 📥 `docs/HOW_TO_DOWNLOAD_CREDENTIALS.md` - Download credentials
- 🔧 `docs/FIX_REDIRECT_URI.md` - Fix redirect URI issues

### Project Documentation
- 📊 `docs/PROJECT_SUMMARY.md` - Project overview
- 📁 `docs/PROJECT_STRUCTURE.md` - Code structure
- ✅ `docs/IMPLEMENTATION_CHECKLIST.md` - Development checklist
- 📈 `docs/IMPLEMENTATION_REPORT.md` - Implementation details

---

## 🧪 Testing

Test scripts are organized in the `tests/` folder:

```bash
# Test reset functionality
python tests/test_reset.py

# Demo interactive menu
python tests/test_interactive_menu.py

# Test greetings agent
python tests/test_greetings_agent.py

# Test grading formula
python tests/test_grading_formula.py
```

---

## ⚙️ Configuration

### Default Settings

**Default Email:** `alona.musiyko@gmail.com`

Change in `orchestrator.py`:
```python
DEFAULT_EMAIL = "your.email@example.com"
```

### Grading Formula

Configured in `repo_analyzer/config.py`:
```python
GRADE_WEIGHTS = {
    'files': 0.3,      # 30%
    'lines': 0.2,      # 20%
    'comments': 0.5,   # 50%
}
```

### Persona Configuration

Edit personas in `greetings_grades_agent/skills/`:
- `donald_trump.py`
- `dudi_amsalem.py`
- `shahar_hasson.py`
- `benjamin_netanyahu.py`

---

## 🛠️ Requirements

- Python 3.8+
- Gmail API credentials
- Internet connection
- Git (for repository analysis)

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Required Packages
- openpyxl
- google-api-python-client
- google-auth-oauthlib
- click
- gitpython
- beautifulsoup4

---

## 🚦 Common Workflows

### Workflow 1: Complete Grading Cycle
```bash
python orchestrator.py
Select: 5

# Follow prompts:
# - Enter Gmail label: homework
# - Enter subject: Lesson 19
# - Enter recipient: your@email.com
# - Confirm: yes

# Wait for completion...
```

### Workflow 2: Re-run from Repository Analysis
```bash
python orchestrator.py
Select: 2  # Repository Analyzer
Select: 3  # Greetings Agent
Select: 4  # Evaluation Sender
```

### Workflow 3: Reset and Start Fresh
```bash
python orchestrator.py
Select: 6  # Reset
Confirm: yes

Select: 5  # Run all agents
```

---

## ❓ Troubleshooting

### "Input file not found"
**Solution:** Run the previous agent first. Agents must run in order (1→2→3→4).

### "Input not ready: Status != 'ready'"
**Solution:** Previous agent didn't complete successfully. Re-run that agent.

### "gmailagent not found"
**Solution:** Install package: `pip install -e .`

### "Gmail authentication failed"
**Solution:**
1. Check credentials at `~/.gmailagent/credentials.json`
2. Re-authenticate: `gmailagent auth`

### More Help
- Check agent-specific documentation in `instructions/` folders
- Run `python orchestrator.py` and use Option 7 for help
- Review error messages for specific guidance

---

## 📖 Learn More

### For Each Agent
Navigate to the agent's `instructions/` folder and read:
1. **PRD** - Understand requirements
2. **README** - Learn usage
3. **QUICKSTART** - Fast reference

### For the Orchestrator
Navigate to `orchestrator_docs/instructions/` and read:
1. **ORCHESTRATOR_README.md** - Complete documentation
2. **ORCHESTRATOR_INTERACTIVE_GUIDE.md** - Interactive features
3. **ORCHESTRATOR_QUICKSTART.md** - Quick reference

---

## 🎯 Key Features

✅ **Automated Workflow** - 4 agents working together
✅ **Interactive Prompts** - Guided configuration
✅ **Status Validation** - Ensures proper sequencing
✅ **Gmail Integration** - Direct email handling
✅ **Repository Analysis** - Automatic code grading
✅ **Personalized Feedback** - 4 unique personas
✅ **Email Drafts** - HTML formatted feedback
✅ **Reset Function** - Clean slate for new runs
✅ **Comprehensive Docs** - Organized by agent
✅ **Test Scripts** - Verify functionality

---

## 📞 Support

For issues, questions, or contributions:
1. Check relevant documentation in `instructions/` folders
2. Review error messages for guidance
3. Run test scripts in `tests/` folder
4. Check `docs/` for setup guides

---

## 📜 License

AI Development Course - Lesson 19
For educational purposes

---

## 🏆 Credits

**Course:** AI Development Course
**Lesson:** 19 - Email Skill Agents
**Components:** 4 Specialized Agents + Orchestrator
**Version:** 2.0.0 (with Interactive Prompts)

---

**Ready to start?** Run `python orchestrator.py` and follow the prompts! 🚀
