"""
Demo script to run Option 5 with Studies/AIDevelopmentCourse label
"""
import sys
from pathlib import Path
from orchestrator import AgentOrchestrator

def main():
    print("=" * 70)
    print("DEMO: Running All Agents (Option 5)")
    print("=" * 70)
    print()

    # Create orchestrator
    orch = AgentOrchestrator()

    # Configuration
    label = "Studies/AIDevelopmentCourse"
    subject = ""  # Optional - leave empty for all
    after = ""    # Optional - leave empty for all dates
    before = ""   # Optional
    newer_than = ""  # Optional
    recipient_email = "alona.musiyko@gmail.com"  # Default recipient

    print("CONFIGURATION:")
    print(f"  Gmail Label:    {label}")
    print(f"  Subject Filter: {subject if subject else '(all)'}")
    print(f"  After Date:     {after if after else '(all)'}")
    print(f"  Before Date:    {before if before else '(all)'}")
    print(f"  Newer Than:     {newer_than if newer_than else '(all)'}")
    print(f"  Recipient:      {recipient_email}")
    print("=" * 70)
    print()

    confirm = input("Run all agents with this configuration? (yes/no): ").strip().lower()
    if confirm not in ["yes", "y"]:
        print("\n[INFO] Cancelled by user")
        return 0

    print()

    # Run Agent 1: GmailAgent
    print("=" * 70)
    print("STEP 1/4: Running GmailAgent")
    print("=" * 70)
    if not orch.run_agent_1_gmail(
        label=label,
        subject=subject if subject else None,
        after=after if after else None,
        before=before if before else None,
        newer_than=newer_than if newer_than else None
    ):
        print("\n[ERROR] Agent 1 failed. Stopping workflow.")
        return 1

    print()

    # Run Agent 2: Repository Analyzer
    print("=" * 70)
    print("STEP 2/4: Running Repository Analyzer")
    print("=" * 70)
    if not orch.run_agent_2_repo_analyzer():
        print("\n[ERROR] Agent 2 failed. Stopping workflow.")
        return 1

    print()

    # Run Agent 3: Greetings Agent
    print("=" * 70)
    print("STEP 3/4: Running Greetings Agent")
    print("=" * 70)
    if not orch.run_agent_3_greetings():
        print("\n[ERROR] Agent 3 failed. Stopping workflow.")
        return 1

    print()

    # Run Agent 4: Evaluation Sender
    print("=" * 70)
    print("STEP 4/4: Running Evaluation Sender")
    print("=" * 70)

    # Directly call the evaluation agent without confirmation prompt
    # We'll bypass the orchestrator's confirmation since user already confirmed
    print(f"[INFO] Sending email drafts to: {recipient_email}")

    # Import and run agent 4 directly
    import subprocess
    try:
        cmd = [
            sys.executable,
            "-m", "evaluationAgent.cli",
            "create-drafts",
            "--input", str(orch.GREETINGS_OUTPUT),
            "--to", recipient_email,
            "--verbose"
        ]

        print(f"[INFO] Running command: {' '.join(cmd)}")
        result = subprocess.run(cmd, capture_output=True, text=True)

        if result.returncode == 0:
            print("[OK] Email drafts created successfully!")
            print(f"[OK] Drafts saved to: {orch.EMAIL_DRAFTS_DIR}")
            if result.stdout:
                print("\nOutput:")
                print(result.stdout)
        else:
            print(f"[ERROR] Agent 4 failed")
            if result.stderr:
                print(f"Error: {result.stderr}")
            if result.stdout:
                print(f"Output: {result.stdout}")
            return 1

    except Exception as e:
        print(f"[ERROR] Failed to run Agent 4: {e}")
        import traceback
        traceback.print_exc()
        return 1

    print()
    print("=" * 70)
    print("[OK] ALL AGENTS COMPLETED SUCCESSFULLY!")
    print("=" * 70)
    print()
    print("Results:")
    print(f"  - Exported emails: {orch.EXPORTS_DIR}")
    print(f"  - Analyzed repos:  {orch.OUTPUT_DIR}")
    print(f"  - With greetings:  {orch.GREETINGS_RESULTS_DIR}")
    print(f"  - Email drafts:    {orch.EMAIL_DRAFTS_DIR}")
    print()

    return 0

if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        print("\n\n[INFO] Interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n\n[ERROR] Unexpected error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
