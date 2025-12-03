# Date Filtering Guide

**Version:** 2.1.0
**Date:** December 2, 2025
**Feature:** Flexible Email Filtering with Date Support

---

## 🎯 Overview

The Email Skill Agents system now supports **flexible filtering** with multiple filter types that can be used **individually or in combination**:

- **Label** - Filter by Gmail label
- **Subject** - Filter by subject text
- **Date Filters** - Filter by date ranges or relative dates (NEW!)

You can use **any combination** of these filters to precisely target the emails you want to process.

---

## 📅 Date Filter Options

### 1. **After Date** (`--after`)
Get emails **after** a specific date.

**Format:** `YYYY-MM-DD` or `YYYY/MM/DD`

**Examples:**
```bash
# Get emails after December 1, 2025
python -m gmailagent export --after "2025-12-01"

# Combined with label
python -m gmailagent export --label "homework" --after "2025-12-01"
```

**Use Cases:**
- Get all emails since the start of a month
- Get emails after a specific assignment was posted
- Filter recent communications

---

### 2. **Before Date** (`--before`)
Get emails **before** a specific date.

**Format:** `YYYY-MM-DD` or `YYYY/MM/DD`

**Examples:**
```bash
# Get emails before December 3, 2025
python -m gmailagent export --before "2025-12-03"

# Combined with subject
python -m gmailagent export --subject "Assignment" --before "2025-11-30"
```

**Use Cases:**
- Get emails from a specific time period
- Exclude recent emails
- Archive old emails

---

### 3. **Newer Than** (`--newer-than`)
Get emails from the **last X days/months/years**.

**Format:**
- `Xd` - X days (e.g., `7d` = last 7 days)
- `Xm` - X months (e.g., `2m` = last 2 months)
- `Xy` - X years (e.g., `1y` = last year)

**Examples:**
```bash
# Get emails from last 7 days
python -m gmailagent export --newer-than "7d"

# Get emails from last 2 months with label
python -m gmailagent export --label "homework" --newer-than "2m"

# Get emails from last 30 days with subject filter
python -m gmailagent export --subject "Lesson" --newer-than "30d"
```

**Use Cases:**
- Quick access to recent emails
- Weekly/monthly reports
- Recent assignments or tasks

---

### 4. **Older Than** (`--older-than`)
Get emails **older than X days/months/years**.

**Format:** Same as `newer-than` (e.g., `7d`, `2m`, `1y`)

**Examples:**
```bash
# Get emails older than 30 days
python -m gmailagent export --older-than "30d"

# Get old homework from more than 6 months ago
python -m gmailagent export --label "homework" --older-than "6m"
```

**Use Cases:**
- Archive old emails
- Clean up mailbox
- Historical data analysis

---

## 🔗 Combining Filters

### Example 1: Label + Subject + Date
```bash
python -m gmailagent export \
  --label "homework" \
  --subject "Lesson 19" \
  --after "2025-12-01"
```
**Result:** Homework emails with "Lesson 19" in subject, sent after Dec 1, 2025

---

### Example 2: Date Range (After + Before)
```bash
python -m gmailagent export \
  --label "assignments" \
  --after "2025-11-01" \
  --before "2025-11-30"
```
**Result:** Assignments from November 2025 only

---

### Example 3: Recent Homework
```bash
python -m gmailagent export \
  --label "homework" \
  --newer-than "7d"
```
**Result:** All homework emails from the last 7 days

---

### Example 4: Subject + Recent
```bash
python -m gmailagent export \
  --subject "Assignment" \
  --newer-than "14d"
```
**Result:** All emails with "Assignment" in subject from last 2 weeks

---

## 🎛️ Using the Orchestrator

The orchestrator now prompts for all filter types:

### Option 1: Run Email Generator

```
Please specify how to filter emails:
You can use any combination of filters below

Filter Options:
  Label:    'homework', 'lesson19', 'assignments'
  Subject:  'Homework 19', 'Assignment', 'Project'
  After:    '2025-12-01' (emails after this date)
  Before:   '2025-12-03' (emails before this date)
  Newer:    '7d' (last 7 days), '2m' (last 2 months)

Enter Gmail label (or press Enter to skip): homework
Enter subject text (or press Enter to skip): Lesson 19
Enter after date YYYY-MM-DD (or press Enter to skip): 2025-12-01
Enter before date YYYY-MM-DD (or press Enter to skip):
Enter newer than (e.g., 7d, 2m) (or press Enter to skip):
```

### Option 5: Run All Agents

```
STEP 1: Email Export Filters

Specify how to filter emails from Gmail:
You can use any combination of filters below

Examples:
  Label:    'homework', 'lesson19', 'assignments'
  Subject:  'Homework 19', 'Assignment', 'Project'
  After:    '2025-12-01' (emails after this date)
  Before:   '2025-12-03' (emails before this date)
  Newer:    '7d' (last 7 days), '2m' (last 2 months)

Enter Gmail label (or press Enter to skip): homework
Enter subject text (or press Enter to skip):
Enter after date YYYY-MM-DD (or press Enter to skip): 2025-12-01
Enter before date YYYY-MM-DD (or press Enter to skip): 2025-12-03
Enter newer than (e.g., 7d, 2m) (or press Enter to skip):

CONFIGURATION SUMMARY
Gmail Label:    homework
Subject Filter: (none)
After Date:     2025-12-01
Before Date:    2025-12-03
Newer Than:     (none)
Recipient:      alona.musiyko@gmail.com
```

---

## 📝 Common Use Cases

### Use Case 1: Process This Week's Homework
```bash
python orchestrator.py
# Select Option 1
# Label: homework
# Newer than: 7d
```

### Use Case 2: Process Specific Lesson from December
```bash
python orchestrator.py
# Select Option 5
# Label: homework
# Subject: Lesson 19
# After: 2025-12-01
# Before: 2025-12-31
```

### Use Case 3: Process All Recent Assignments
```bash
python -m gmailagent export \
  --subject "Assignment" \
  --newer-than "30d"
```

### Use Case 4: Archive Old Homework (older than 6 months)
```bash
python -m gmailagent export \
  --label "homework" \
  --older-than "6m"
```

---

## ✨ Filter Combinations Matrix

| Label | Subject | Date | Result |
|-------|---------|------|--------|
| ✓ | - | - | All emails with that label |
| - | ✓ | - | All emails with that subject |
| - | - | ✓ | All emails in that date range |
| ✓ | ✓ | - | Label + Subject match |
| ✓ | - | ✓ | Label + Date match |
| - | ✓ | ✓ | Subject + Date match |
| ✓ | ✓ | ✓ | All three must match (most specific) |

**Note:** You can skip any filter by pressing Enter

---

## 🔍 Gmail Query Syntax

The system converts your filters to Gmail's query syntax:

| Filter | Gmail Query |
|--------|-------------|
| `--label homework` | `label:homework` |
| `--subject "Lesson 19"` | `subject:Lesson 19` |
| `--after "2025-12-01"` | `after:2025/12/01` |
| `--before "2025-12-03"` | `before:2025/12/03` |
| `--newer-than "7d"` | `newer_than:7d` |
| `--older-than "30d"` | `older_than:30d` |

**Combined Example:**
```
--label homework --subject "Lesson" --after "2025-12-01"
→ label:homework subject:Lesson after:2025/12/01
```

---

## 💡 Tips & Best Practices

### Tip 1: Use Relative Dates for Regular Tasks
Instead of calculating dates manually, use relative filters:
```bash
# Weekly homework review
--newer-than "7d"

# Monthly report
--newer-than "30d"
```

### Tip 2: Combine Label + Date for Precision
```bash
# Get homework from this month
--label "homework" --after "2025-12-01"
```

### Tip 3: Use Date Ranges for Specific Periods
```bash
# Get emails from November only
--after "2025-11-01" --before "2025-11-30"
```

### Tip 4: Test Filters First
Use Option 1 to test your filters before running the full workflow (Option 5):
```bash
python orchestrator.py
# Select Option 1 to test filters
# If results look good, run Option 5
```

### Tip 5: Skip Unnecessary Filters
You don't need to fill in all filters - just press Enter to skip:
```bash
Enter Gmail label: homework
Enter subject: [just press Enter]
Enter after date: 2025-12-01
Enter before date: [just press Enter]
Enter newer than: [just press Enter]
```

---

## 🧪 Testing Examples

### Test 1: Basic Date Filter
```bash
python -m gmailagent export --after "2025-12-01"
```

### Test 2: Recent Homework
```bash
python -m gmailagent export --label "homework" --newer-than "7d"
```

### Test 3: Complete Workflow with Dates
```bash
python orchestrator.py
# Select Option 5
# Label: homework
# Subject: (skip)
# After: 2025-12-01
# Recipient: [default]
# Confirm: yes
```

---

## 📊 Summary of Changes

### New Options Added
1. `--after DATE` - Filter emails after date
2. `--before DATE` - Filter emails before date
3. `--newer-than PERIOD` - Filter recent emails
4. `--older-than PERIOD` - Filter old emails

### Files Modified
1. `gmailagent/cli.py` - Added date options to export command
2. `gmailagent/gmail_client.py` - Added date support to query builder
3. `orchestrator.py` - Added date prompts to interactive menu

### Backward Compatibility
✅ **Fully backward compatible** - existing scripts using only label/subject will continue to work

---

## ❓ Frequently Asked Questions

**Q: Can I use both --after and --newer-than together?**
A: Yes, but usually you only need one. --newer-than is simpler for relative dates.

**Q: What date format should I use?**
A: Use YYYY-MM-DD (e.g., 2025-12-01). YYYY/MM/DD also works.

**Q: How do I filter emails from exactly one day?**
A: Use --after and --before with the same date:
```bash
--after "2025-12-01" --before "2025-12-01"
```

**Q: Can I filter by time (hours/minutes)?**
A: No, Gmail only supports date-level filtering, not time-level.

**Q: What happens if I don't enter any filters?**
A: You'll be prompted to confirm exporting ALL emails (up to the limit).

---

## 🚀 Quick Reference

**Command Line:**
```bash
# Recent homework
python -m gmailagent export --label "homework" --newer-than "7d"

# Specific date range
python -m gmailagent export --after "2025-12-01" --before "2025-12-31"

# Combined filters
python -m gmailagent export --label "homework" --subject "Lesson" --after "2025-12-01"
```

**Orchestrator (Interactive):**
```bash
python orchestrator.py
# Option 1: Single agent with prompts
# Option 5: Full workflow with prompts
```

---

## 📖 Related Documentation

- `README.md` - Project overview
- `FINAL_STATUS.md` - Complete project status
- `RUN_ORCHESTRATOR.md` - How to run orchestrator
- `docs/LATEST_FIXES.md` - Recent updates

---

**Version:** 2.1.0
**Feature:** Date Filtering Support
**Status:** ✅ Production Ready

All date filtering features are fully tested and ready to use! 🎉
