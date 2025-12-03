# GmailAgent - Exports Folder Structure

## Overview
All exported Excel files are automatically saved to the `./exports/` directory with intelligent filenames based on the filters used.

## Folder Structure

```
EmailSkillAgents/
├── exports/                              ← Auto-created folder for all Excel exports
│   ├── 22.11.2024_143022_mails_by_tag_Important.xlsx
│   ├── 22.11.2024_143530_mails_from_folder_Work.xlsx
│   ├── 22.11.2024_144015_mails_by_subject_invoice.xlsx
│   ├── 22.11.2024_145033_mails_by_tag_clients.xlsx
│   ├── 22.11.2024_145522_mails_by_label_Important_from_sender_client@example.com.xlsx
│   └── ... (more exports)
├── PRD-GmailAgent.md                     ← Product Requirements Document
├── EXPORTS_FOLDER_STRUCTURE.md           ← This file
└── ... (other project files)
```

## Filename Convention

### Format
```
DD.MM.YYYY_HHMMSS_mails_<filter_description>.xlsx
```

### Components

1. **Date**: `DD.MM.YYYY` (e.g., `22.11.2024`)
2. **Time**: `HHMMSS` in 24-hour format (e.g., `143022` = 2:30:22 PM)
3. **Prefix**: Always `mails_`
4. **Filter Description**: Describes which filters were used

### Filter Description Patterns

| Filter Type | Filename Pattern | Example |
|-------------|------------------|---------|
| By Tag | `by_tag_<tagname>` | `by_tag_Important` |
| By Folder | `from_folder_<foldername>` | `from_folder_Work` |
| By Label | `by_label_<labelname>` | `by_label_Clients` |
| By Sender | `from_sender_<email>` | `from_sender_boss@company.com` |
| By Recipient | `to_recipient_<email>` | `to_recipient_john@example.com` |
| By Subject | `by_subject_<text>` | `by_subject_invoice` |
| Multiple Filters | Combined with `_` | `by_tag_Work_from_sender_john@example.com` |

## Example Filenames

### Single Filter Examples

```bash
# Export by tag "Important"
$ gmailagent export --tag "Important"
→ exports/22.11.2024_143022_mails_by_tag_Important.xlsx

# Export from folder "Work"
$ gmailagent export --folder "Work"
→ exports/22.11.2024_143530_mails_from_folder_Work.xlsx

# Export from sender
$ gmailagent export --from "boss@company.com"
→ exports/22.11.2024_144015_mails_from_sender_boss@company.com.xlsx

# Export by subject
$ gmailagent export --subject "invoice"
→ exports/22.11.2024_144522_mails_by_subject_invoice.xlsx
```

### Multiple Filter Examples

```bash
# Export by tag AND sender
$ gmailagent export --tag "Work" --from "client@example.com"
→ exports/22.11.2024_145033_mails_by_tag_Work_from_sender_client@example.com.xlsx

# Export by folder AND subject
$ gmailagent export --folder "Important" --subject "meeting"
→ exports/22.11.2024_145522_mails_from_folder_Important_by_subject_meeting.xlsx

# Export by label, sender, and subject
$ gmailagent export --label "Sales" --from "lead@company.com" --subject "proposal"
→ exports/22.11.2024_150033_mails_by_label_Sales_from_sender_lead@company.com_by_subject_proposal.xlsx
```

## Filename Sanitization

Special characters are automatically handled:

| Original | Sanitized | Example |
|----------|-----------|---------|
| `@` | `@` (kept) | `boss@company.com` |
| Spaces | `_` | `My Tag` → `My_Tag` |
| `/` | `_` | `Work/Projects` → `Work_Projects` |
| `<>:"\|?*` | `_` | Removed or replaced |

**Max length**: Each filter value is limited to 50 characters to keep filenames reasonable.

## Excel File Structure

Each exported Excel file contains:

### Columns

| Column | Description | Example |
|--------|-------------|---------|
| **ID** | Unique UUID for each email | `a1b2c3d4-e5f6-7890-abcd-ef1234567890` |
| **Date** | Email timestamp | `2024-11-21 09:30:00` |
| **Subject** | Email subject line | `Meeting Invitation - Q4 Planning` |
| **URL** | Extracted URLs (comma-separated) | `https://zoom.us/j/123456` |

### Example Content

```
| ID | Date | Subject | URL |
|----|------|---------|-----|
| uuid-1234 | 2024-11-21 09:30:00 | Meeting Invitation | https://zoom.us/j/123456 |
| uuid-5678 | 2024-11-21 08:15:00 | Invoice #1234 | https://example.com/invoice |
| uuid-9012 | 2024-11-20 16:45:00 | Project Update | https://docs.google.com/doc123, https://github.com/project |
| uuid-3456 | 2024-11-20 14:30:00 | Quick question | |
```

## Custom Output Override

You can override the automatic naming with `--output` flag:

```bash
# Custom filename (not in exports folder)
$ gmailagent export --tag "Work" --output "my_custom_export.xlsx"
→ my_custom_export.xlsx

# Custom path including folder
$ gmailagent export --tag "Work" --output "reports/monthly_emails.xlsx"
→ reports/monthly_emails.xlsx
```

## Benefits of Smart Naming

✅ **Self-Documenting**: Filename shows exactly what filters were used
✅ **Chronological**: Easy to find recent exports (sorted by date/time)
✅ **No Overwrites**: Timestamp ensures unique filenames
✅ **Organized**: All exports in one folder
✅ **Searchable**: Easy to find specific exports by filter name
✅ **Traceable**: Know when and how each export was generated

## Use Cases

### 1. Daily Email Tracking
Export emails daily and track by date:
```
exports/
├── 21.11.2024_090000_mails_by_tag_Important.xlsx
├── 22.11.2024_090000_mails_by_tag_Important.xlsx
├── 23.11.2024_090000_mails_by_tag_Important.xlsx
```

### 2. Client-Specific Reports
Track emails by client:
```
exports/
├── 22.11.2024_100000_mails_from_sender_clientA@company.com.xlsx
├── 22.11.2024_110000_mails_from_sender_clientB@company.com.xlsx
├── 22.11.2024_120000_mails_from_sender_clientC@company.com.xlsx
```

### 3. Topic-Based Analysis
Export emails by subject matter:
```
exports/
├── 22.11.2024_140000_mails_by_subject_invoice.xlsx
├── 22.11.2024_141000_mails_by_subject_meeting.xlsx
├── 22.11.2024_142000_mails_by_subject_proposal.xlsx
```

### 4. Multi-Filter Segmentation
Combine filters for precise targeting:
```
exports/
├── 22.11.2024_150000_mails_by_tag_Sales_from_sender_lead@company.com.xlsx
├── 22.11.2024_151000_mails_by_tag_Support_by_subject_urgent.xlsx
├── 22.11.2024_152000_mails_from_folder_Clients_by_subject_contract.xlsx
```

## Technical Implementation

The filename generation is handled by:

```python
def generate_filename(filters):
    """Generate smart filename based on active filters"""
    now = datetime.now()
    date_str = now.strftime("%d.%m.%Y")  # DD.MM.YYYY
    time_str = now.strftime("%H%M%S")    # HHMMSS

    filter_parts = []
    # Build filter description from active filters
    # ... (see PRD for full implementation)

    filter_desc = "_".join(filter_parts)
    filename = f"{date_str}_{time_str}_mails_{filter_desc}.xlsx"

    return filename
```

## Folder Management

The `./exports/` folder is:
- ✅ Auto-created on first export if it doesn't exist
- ✅ Persistent across runs
- ✅ Can be cleaned up manually by user
- ✅ Not version controlled (add to `.gitignore`)

### Recommended .gitignore

```gitignore
# GmailAgent exports
exports/
*.xlsx

# Credentials
.gmailagent/
credentials.json
```

---

**Last Updated**: November 21, 2024
**Version**: 1.0
