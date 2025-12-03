# Quick Start: Personalized Greetings Agent

Get personalized feedback for your students in under 2 minutes!

## Prerequisites

You must have already run:
1. **GmailAgent** - To export homework emails
2. **Repository Analyzer** - To grade the repositories

This creates: `output/homework_emails_graded.xlsx`

## 5-Minute Quick Start

### Step 1: Navigate to Project Directory

```bash
cd C:\AIDevelopmentCourse\L-19\EmailSkillAgents
```

### Step 2: Run Greetings Agent

```bash
python -m greetings_grades_agent.cli greet --input output/homework_emails_graded.xlsx
```

### Step 3: Check Output

The agent creates: `greetings_results/homework_emails_with_greetings.xlsx`

Open it in Excel to see:
- All original columns (ID, Date, Subject, URL, Grade, etc.)
- **NEW: Personalized Greeting** - Motivational message
- **NEW: Greeting Persona** - Which persona was used

## Example Output

```
==================================================
Personalized Greetings Agent v1.0
==================================================

Reading input: output\homework_emails_graded.xlsx
Found 30 students with grades

Generating personalized greetings...

[1/30] Grade: 45%    -> Persona: Dudi Amsalem
[2/30] Grade: 100%   -> Persona: Donald Trump
[3/30] Grade: 75%    -> Persona: Shahar Hasson
...
[30/30] Grade: 92%   -> Persona: Donald Trump

Writing output to: greetings_results\homework_emails_with_greetings.xlsx

==================================================
Summary
==================================================
Total Students: 30
Greetings Generated: 28
Skipped (no grade): 2

Personas Used:
  - Dudi Amsalem (0-50%): 4
  - Netanyahu (51-70%): 9
  - Shahar Hasson (71-90%): 11
  - Donald Trump (91-100%): 4

Output: greetings_results\homework_emails_with_greetings.xlsx

[OK] Greetings complete!
```

## Sample Greetings

### Low Grade (0-50%) - Dudi Amsalem

> "Listen, 35%? We need to talk. This isn't good enough. Time to stop making excuses and start making real progress. You can do better - I know it. Now get to work!"

**Tone:** Direct, tough love, motivating

### Average Grade (51-70%) - Benjamin Netanyahu

> "Your performance at 65% demonstrates potential, though there is clear room for advancement. With focused effort and strategic improvement, you can achieve excellence."

**Tone:** Diplomatic, formal, constructive

### Good Grade (71-90%) - Shahar Hasson

> "Nice work! 82% shows you've got strong fundamentals. Keep pushing - you're close to mastering this. A few refinements and you'll be at the top!"

**Tone:** Warm, tech mentor, encouraging

### Excellent Grade (91-100%) - Donald Trump

> "TREMENDOUS work! 97%! This is what I call WINNING! You're doing an absolutely FANTASTIC job - the best! AMAZING achievement!"

**Tone:** Enthusiastic, celebratory, superlatives

## Advanced Usage

### Custom Output Path

```bash
python -m greetings_grades_agent.cli greet \
  --input output/homework_emails_graded.xlsx \
  --output my_custom_greetings.xlsx
```

### Verbose Mode

```bash
python -m greetings_grades_agent.cli greet \
  --input output/homework_emails_graded.xlsx \
  --verbose
```

## Complete Workflow (All 3 Agents)

```bash
# Agent 1: Export emails from Gmail
python -m gmailagent.cli export-emails --query "homework submission"

# Agent 2: Grade repositories
python -m repo_analyzer.cli grade-all --input output/homework_emails.xlsx

# Agent 3: Add personalized greetings
python -m greetings_grades_agent.cli greet --input output/homework_emails_graded.xlsx

# Final output: greetings_results/homework_emails_with_greetings.xlsx
```

## What Happens Next?

After running the agent, you have an Excel file with:
- All original data (grades, file counts, etc.)
- Personalized motivational greetings for each student
- Persona used for each greeting

**Next steps:**
1. Review the greetings in Excel
2. (Optional) Edit any greetings you want to customize
3. Send feedback to students via:
   - Email (copy/paste greetings)
   - LMS (Canvas, Blackboard, etc.)
   - Direct message
   - In-class feedback

## Testing

Test the agent with the included test suite:

```bash
python test_greetings_agent.py
```

This validates:
- Persona selection logic (all grade ranges)
- Greeting generation (all 4 personas)
- Greeting variety (multiple templates)
- Excel validation
- Edge cases (0%, 100%, missing grades)

## Troubleshooting

### "Excel file not found"

**Problem:** Input file doesn't exist

**Solution:** Run Repository Analyzer first to create `homework_emails_graded.xlsx`

```bash
python -m repo_analyzer.cli grade-all --input output/homework_emails.xlsx
```

### "Missing 'Grade' column"

**Problem:** Input Excel has wrong format

**Solution:** Ensure you're using output from Repository Analyzer, not GmailAgent

### No greetings for some students

**Problem:** Some students have repository errors (no grade)

**Expected:** Agent skips students without grades, shows "N/A" in greeting column

## Performance

- **30 students**: ~2 seconds
- **50 students**: ~3 seconds
- **100 students**: ~5 seconds

Template-based approach is instant (no API calls needed).

## What's Next?

- Read full documentation: `greetings_grades_agent/README.md`
- Review the PRD: `PRD-PersonalizedGreetingsAgent.md`
- Explore persona templates: `greetings_grades_agent/skills/`
- Customize greetings for your teaching style

## Support

For detailed documentation:
- **README**: `greetings_grades_agent/README.md`
- **PRD**: `PRD-PersonalizedGreetingsAgent.md`
- **Code**: `greetings_grades_agent/` directory

---

**Time Saved:** 60-90 minutes → 2 seconds
**Engagement Boost:** Cold numbers → Personalized motivation
**Quality:** Consistent, appropriate, educational feedback
