# Email Skill Agents

**Version:** 2.1.0
**Status:** ✅ Production Ready
**Date:** December 3, 2025

Automated homework grading workflow with 4 specialized agents that process Gmail emails, analyze repositories, generate personalized feedback, and send evaluation emails.

---

## 🚀 Quick Start

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Authenticate with Gmail
python -m gmailagent auth

# 3. Run orchestrator
python orchestrator.py

# 4. Select Option 5 (Run All Agents)
```

---

## 📋 Agents

1. **GmailAgent** - Export emails from Gmail with URL extraction
2. **Repository Analyzer** - Clone and analyze Git repositories, calculate grades
3. **Greetings Agent** - Add personalized, persona-based greetings
4. **Evaluation Sender** - Create and send HTML email drafts via Gmail

---

## 📖 Complete Documentation

All documentation is available in the **`instructions/`** folder:

### Getting Started
- **[instructions/README.md](instructions/README.md)** - Complete project overview (START HERE)
- **[instructions/QUICKSTART.md](instructions/QUICKSTART.md)** - Quick reference guide
- **[instructions/RUN_ORCHESTRATOR.md](instructions/RUN_ORCHESTRATOR.md)** - How to run the orchestrator

### Status & Updates
- **[instructions/QUICK_STATUS.md](instructions/QUICK_STATUS.md)** - Current status summary
- **[instructions/FINAL_STATUS.md](instructions/FINAL_STATUS.md)** - Comprehensive status report
- **[instructions/CHANGELOG.md](instructions/CHANGELOG.md)** - Version history

### Technical Details
- **[instructions/OPTION_5_FIX.md](instructions/OPTION_5_FIX.md)** - Option 5 fixes and improvements
- **[instructions/FOLDER_STRUCTURE.md](instructions/FOLDER_STRUCTURE.md)** - Complete folder structure
- **[instructions/REORGANIZATION_COMPLETE.md](instructions/REORGANIZATION_COMPLETE.md)** - Reorganization details

### Feature Guides
- **[docs/DATE_FILTERING_GUIDE.md](docs/DATE_FILTERING_GUIDE.md)** - Date filtering feature guide
- **[docs/LATEST_FIXES.md](docs/LATEST_FIXES.md)** - Latest fixes and updates

---

## ✨ Key Features

- ✅ Gmail integration with OAuth 2.0
- ✅ Automatic repository cloning and analysis
- ✅ Grade calculation based on code metrics
- ✅ Personalized greetings based on performance
- ✅ HTML email generation with professional templates
- ✅ Status column coordination between agents
- ✅ Interactive orchestrator menu
- ✅ Date filtering support (after, before, newer-than)
- ✅ Flexible filter combinations (label + subject + date)

---

## 🎯 Latest Updates (v2.1.0)

### New Features
- ✨ **Date Filtering** - Filter emails by date ranges or relative dates
- ✨ **Flexible Combinations** - Combine label, subject, and date filters

### Recent Fixes
- ✅ Fixed Unicode encoding issues on Windows
- ✅ Fixed "no emails found" detection
- ✅ Fixed Status column handling for multiple Status columns
- ✅ All 4 agents working perfectly in sequence

---

## 📁 Project Structure

```
EmailSkillAgents/
├── instructions/              # 📖 Complete documentation
├── docs/                      # Additional guides
├── gmailagent/               # Agent 1: Email export
├── repo_analyzer/            # Agent 2: Repository grading
├── greetings_grades_agent/   # Agent 3: Personalized greetings
├── evaluationAgent/          # Agent 4: Email sending
├── orchestrator.py           # Main orchestrator
├── tests/                    # Test scripts
└── requirements.txt          # Python dependencies
```

---

## 🔧 Requirements

- Python 3.8+
- Gmail account with API access
- Internet connection
- Required packages (see requirements.txt)

---

## 💡 Usage Examples

### Filter by Label
```bash
python orchestrator.py
# Select Option 1
# Label: Studies/AIDevelopmentCourse
```

### Filter by Date Range
```bash
python -m gmailagent export --label "homework" --after "2025-12-01"
```

### Run Complete Workflow
```bash
python orchestrator.py
# Select Option 5
# Follow prompts for label, subject, date, recipient
```

---

## 🆘 Support

For detailed information, see the documentation in the **`instructions/`** folder.

**Quick Links:**
- Getting Started: `instructions/QUICKSTART.md`
- Troubleshooting: `instructions/FINAL_STATUS.md`
- Feature Guide: `docs/DATE_FILTERING_GUIDE.md`

---

## 📊 Test Results

- ✅ 7/7 tests passing
- ✅ All agents working correctly
- ✅ Date filtering verified
- ✅ Gmail integration tested
- ✅ Complete workflow validated

---

**Version:** 2.1.0
**Last Updated:** December 3, 2025
**Status:** Production Ready ✅

For complete documentation, see **`instructions/README.md`**
