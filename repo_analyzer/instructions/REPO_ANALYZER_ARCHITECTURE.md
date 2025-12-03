# Repository Analyzer Agent - Architecture

## Overview

The Repository Analyzer Agent follows a **layered architecture** with clear separation of concerns:

1. **CLI Layer** - User interaction (Click framework)
2. **Orchestrator Layer** - Workflow coordination
3. **Business Logic Layer** - Core functionality (Excel, Git, Metrics)
4. **Configuration Layer** - Constants and exceptions

## System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     USER INTERACTION                        │
│                                                             │
│  python -m repo_analyzer.cli analyze --input hw.xlsx       │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│                    CLI LAYER (cli.py)                       │
│  ┌───────────────────────────────────────────────────┐     │
│  │ - Parse command-line arguments                    │     │
│  │ - Validate input file path                        │     │
│  │ - Create RepositoryAnalyzer instance              │     │
│  │ - Handle exceptions and display errors            │     │
│  └───────────────────────────────────────────────────┘     │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│              ORCHESTRATOR LAYER (analyzer.py)               │
│  ┌───────────────────────────────────────────────────┐     │
│  │ RepositoryAnalyzer                                │     │
│  │ ────────────────────                              │     │
│  │ - Coordinate all components                       │     │
│  │ - Manage workflow                                 │     │
│  │ - Display progress                                │     │
│  │ - Generate summary                                │     │
│  └───────────────────────────────────────────────────┘     │
└──┬────────────────┬────────────────┬────────────────────────┘
   │                │                │
   │                │                │
   ▼                ▼                ▼
┌───────────────┐  ┌───────────────┐  ┌─────────────────┐
│ EXCEL MANAGER │  │  REPO MANAGER │  │ METRICS         │
│               │  │               │  │ CALCULATOR      │
│ excel_        │  │ repo_         │  │ metrics_        │
│ manager.py    │  │ manager.py    │  │ calculator.py   │
│               │  │               │  │                 │
│ ┌───────────┐ │  │ ┌───────────┐ │  │ ┌─────────────┐ │
│ │ Read      │ │  │ │ Clone     │ │  │ │ Traverse    │ │
│ │ Excel     │ │  │ │ Repository│ │  │ │ Directory   │ │
│ │           │ │  │ │           │ │  │ │             │ │
│ │ Validate  │ │  │ │ Validate  │ │  │ │ Identify    │ │
│ │ Columns   │ │  │ │ URL       │ │  │ │ Code Files  │ │
│ │           │ │  │ │           │ │  │ │             │ │
│ │ Extract   │ │  │ │ Handle    │ │  │ │ Count Lines │ │
│ │ URLs      │ │  │ │ Errors    │ │  │ │             │ │
│ │           │ │  │ │           │ │  │ │ Calculate   │ │
│ │ Write     │ │  │ │ Cleanup   │ │  │ │ Grade       │ │
│ │ Results   │ │  │ │           │ │  │ │             │ │
│ │           │ │  │ │           │ │  │ │             │ │
│ │ Create    │ │  │ │           │ │  │ │             │ │
│ │ Summary   │ │  │ │           │ │  │ │             │ │
│ └───────────┘ │  │ └───────────┘ │  │ └─────────────┘ │
└───────┬───────┘  └───────┬───────┘  └────────┬────────┘
        │                  │                   │
        │                  │                   │
        ▼                  ▼                   ▼
┌─────────────────────────────────────────────────────┐
│              CONFIGURATION & ERRORS                 │
│                                                     │
│  ┌────────────────┐         ┌──────────────────┐   │
│  │  config.py     │         │    errors.py     │   │
│  │  ────────────  │         │    ──────────    │   │
│  │  Constants:    │         │    Exceptions:   │   │
│  │  - Extensions  │         │    - ExcelError  │   │
│  │  - Exclusions  │         │    - RepoError   │   │
│  │  - Line Limit  │         │    - MetricError │   │
│  │  - Retry Count │         │    - NetworkErr  │   │
│  └────────────────┘         └──────────────────┘   │
└─────────────────────────────────────────────────────┘
```

## Data Flow

```
INPUT                  PROCESSING                       OUTPUT
─────                  ──────────                       ──────

homework_             1. Read Excel                    homework_
emails.xlsx          ───────────────►                  emails_
                                                       graded.xlsx
  │                   ExcelManager
  │                   - Validate
  │                   - Extract URLs                    │
  │                                                     │
  ▼                   2. Clone Repos                    │
                     ───────────────►                   │
[URL 1]               RepositoryManager                 │
[URL 2]               - Shallow clone                   │
[URL 3]               - Error handling                  │
[URL 4]               - Temp directory                  │
                                                        │
  │                   3. Calculate Metrics              │
  │                  ───────────────►                   │
  ▼                   MetricsCalculator                 │
                      - Count lines                     │
/tmp/repo_1/          - Count files                     │
/tmp/repo_2/          - Calculate grade                 │
/tmp/repo_3/                                            │
/tmp/repo_4/          4. Aggregate Results              │
                     ───────────────►                   │
  │                   Analyzer                          │
  │                   - Collect all results             │
  │                   - Calculate summary               │
  │                   - Generate statistics             │
  │                                                     │
  ▼                   5. Write Output                   ▼
                     ───────────────►
Cleanup               ExcelManager                    [Sheet 1]
                      - Format data                   Graded
                      - Create sheets                 Results
                      - Write statistics
                                                      [Sheet 2]
                                                      Summary
```

## Processing Sequence (Per Repository)

```
STEP 1: CLONE
──────────────
User Input → CLI → Analyzer → RepoManager.clone(url)
                                    │
                                    ├─ Validate URL format
                                    ├─ Create temp directory
                                    ├─ Execute git clone --depth 1
                                    ├─ Handle errors (404, 403, network)
                                    └─ Return local_path or error
                                         │
                                         ▼
                                    local_path

STEP 2: ANALYZE
───────────────
local_path → MetricsCalculator.calculate(local_path)
                    │
                    ├─ Traverse directory tree
                    ├─ Filter code files (by extension)
                    ├─ Exclude directories (node_modules, .git, etc)
                    ├─ For each code file:
                    │   ├─ Read file (UTF-8, fallback latin-1)
                    │   ├─ Count non-empty lines
                    │   └─ Track if < 130 lines
                    ├─ Sum totals
                    └─ Calculate grade: (files_<130 / total_files) * 100
                         │
                         ▼
                    {total_lines, total_files, files_under_130, grade}

STEP 3: RECORD
──────────────
Metrics → Analyzer → results.append()
                         │
                         └─ Store for Excel output
```

## Workflow State Machine

```
┌───────────┐
│   START   │
└─────┬─────┘
      │
      ▼
┌───────────────┐
│  Read Excel   │───── Error ────► [Exit with error]
└──────┬────────┘
       │ Success
       ▼
┌───────────────┐
│ For each URL  │◄──────────┐
└──────┬────────┘           │
       │                    │
       ▼                    │
┌───────────────┐           │
│  Clone Repo   │           │
└──────┬────────┘           │
       │                    │
       ├─ Success           │
       │    │               │
       │    ▼               │
       │ ┌──────────────┐  │
       │ │ Calculate    │  │
       │ │ Metrics      │  │
       │ └──────┬───────┘  │
       │        │          │
       │        ▼          │
       │    [Record]       │
       │                   │
       ├─ Error            │
       │    │               │
       │    ▼               │
       │ [Record Error]    │
       │                   │
       └──► More URLs? ────┘
              │ No
              ▼
       ┌──────────────┐
       │ Write Excel  │
       └──────┬───────┘
              │
              ▼
       ┌──────────────┐
       │   Cleanup    │
       └──────┬───────┘
              │
              ▼
       ┌──────────────┐
       │  Show Summary│
       └──────┬───────┘
              │
              ▼
          [END]
```

## Component Interactions

### Analyzer → ExcelManager

```python
# Read input
data = excel_manager.read_input("homework_emails.xlsx")
# Returns: [{'url': '...', 'id': '...', 'date': '...', 'subject': '...'}, ...]

# Write output
excel_manager.write_output(
    output_path="output/graded.xlsx",
    original_data=data,
    results=results,
    processing_time=28.5
)
```

### Analyzer → RepositoryManager

```python
# Initialize
repo_manager = RepositoryManager()

# Clone repository
local_path, success, error = repo_manager.clone(url)

if success:
    # Process the repository
    process(local_path)
else:
    # Handle error
    record_error(error)

# Cleanup at end
repo_manager.cleanup()
```

### Analyzer → MetricsCalculator

```python
# Initialize
calculator = MetricsCalculator()

# Calculate metrics
metrics = calculator.calculate(local_path)
# Returns: {
#     'total_lines': 1646,
#     'total_files': 16,
#     'files_under_130': 12,
#     'grade': 75.00
# }
```

## Design Patterns Used

### 1. Facade Pattern
**Where:** `RepositoryAnalyzer` class
**Why:** Provides a simplified interface to the complex subsystem (Excel, Git, Metrics)

### 2. Strategy Pattern
**Where:** `MetricsCalculator` for different file types
**Why:** Different handling for different programming languages

### 3. Template Method Pattern
**Where:** `_process_single_repository()` in Analyzer
**Why:** Defines the skeleton of the algorithm (clone → analyze → record)

### 4. Dependency Injection
**Where:** All components are injected into Analyzer
**Why:** Loose coupling, easy testing, flexibility

### 5. Exception Hierarchy
**Where:** Custom exceptions in `errors.py`
**Why:** Fine-grained error handling, clear error types

## Module Dependencies

```
cli.py
  └── analyzer.py (RepositoryAnalyzer)
        ├── excel_manager.py (ExcelManager)
        │     ├── config.py (constants)
        │     └── errors.py (ExcelError, ExcelNotFoundError, etc.)
        │
        ├── repo_manager.py (RepositoryManager)
        │     ├── config.py (CLONE_TIMEOUT, RETRY_ATTEMPTS, etc.)
        │     ├── errors.py (RepositoryError, etc.)
        │     └── git (GitPython library)
        │
        └── metrics_calculator.py (MetricsCalculator)
              ├── config.py (CODE_EXTENSIONS, EXCLUDE_DIRS, LINE_LIMIT)
              └── errors.py (MetricsCalculationError)
```

## Threading Model (Future - Phase 2)

```
┌────────────────────────────────────────────────────┐
│              Main Thread (Orchestrator)            │
│                                                    │
│  ┌──────────────────────────────────────────┐    │
│  │ ThreadPoolExecutor (5-10 workers)        │    │
│  │                                          │    │
│  │  Worker 1  Worker 2  Worker 3  ...      │    │
│  │     │         │         │                │    │
│  │     ▼         ▼         ▼                │    │
│  │   Clone    Clone    Clone                │    │
│  │     │         │         │                │    │
│  │     ▼         ▼         ▼                │    │
│  │  Analyze   Analyze   Analyze             │    │
│  │     │         │         │                │    │
│  │     └─────────┴─────────┘                │    │
│  │              │                           │    │
│  │              ▼                           │    │
│  │      Thread-Safe Queue                   │    │
│  └──────────────────────────────────────────┘    │
│                  │                               │
│                  ▼                               │
│         Collect Results                          │
│                  │                               │
│                  ▼                               │
│          Write to Excel                          │
└────────────────────────────────────────────────────┘
```

**Note:** Phase 1 uses sequential processing. Multithreading will be added in Phase 2.

## Error Handling Flow

```
┌─────────────┐
│ Try Clone   │
└──────┬──────┘
       │
       ├─ Success ────────────────────┐
       │                              │
       ├─ 404 Not Found ──────────►   │
       │   Status: "Not Found"        │
       │   Continue Processing        │
       │                              │
       ├─ 403 Forbidden ──────────►   │
       │   Status: "Access Denied"    │
       │   Continue Processing        ├──► Record Result
       │                              │    & Continue
       ├─ Invalid URL ───────────►    │
       │   Status: "Invalid URL"      │
       │   Continue Processing        │
       │                              │
       ├─ Network Error ─────────►    │
       │   Status: "Network Error"    │
       │   Continue Processing        │
       │                              │
       └─ Unexpected Error ──────►    │
           Status: "Error"            │
           Continue Processing    ────┘
```

## Performance Considerations

### Current (Sequential)
- **Bottleneck:** Network I/O (Git clone)
- **CPU Usage:** Low (waiting for I/O)
- **Processing Time:** ~7 seconds per repo
- **Scalability:** Linear (30 repos = 3.5 minutes)

### Future (Multithreaded - Phase 2)
- **Parallelism:** 5-10 concurrent clones
- **Expected Speedup:** 4-8x
- **Target:** 30 repos in <25 minutes
- **Thread Safety:** Queue for result collection

## Security Considerations

1. **Sandboxed Execution**
   - Clones to temporary directory
   - Read-only access to repositories
   - No code execution
   - Automatic cleanup

2. **Input Validation**
   - URL format validation
   - Excel structure validation
   - File path validation

3. **Error Isolation**
   - Per-repository error handling
   - No cascading failures
   - Continue on error

4. **No Credentials**
   - Public repositories only (Phase 1)
   - No authentication required
   - No sensitive data storage

## Extensibility Points

### Adding New Language Support
**File:** `config.py`
```python
CODE_EXTENSIONS = [
    '.py', '.java', '.js',  # Existing
    '.go', '.rust', '.kt'   # Add new extensions here
]
```

### Custom Grading Formula (Future)
**File:** `metrics_calculator.py`
```python
def _calculate_grade(self, metrics, formula='default'):
    if formula == 'default':
        return (metrics['files_under_130'] / metrics['total_files']) * 100
    elif formula == 'custom':
        # Custom formula implementation
        pass
```

### Additional Metrics (Future)
**File:** `metrics_calculator.py`
```python
def calculate_advanced_metrics(self, repo_path):
    # Cyclomatic complexity
    # Maintainability index
    # Code coverage
    pass
```

---

**Architecture Version:** 1.0.0
**Status:** Production
**Last Updated:** 2025-11-23

