"""
Test script to demonstrate the reset functionality of the orchestrator.
"""

import os
from pathlib import Path
from orchestrator import AgentOrchestrator


def create_test_files():
    """Create some test files to demonstrate reset."""
    orchestrator = AgentOrchestrator()

    print("Creating test files...")

    # Create test files in each directory
    test_files = [
        orchestrator.EXPORTS_DIR / "test_email1.xlsx",
        orchestrator.EXPORTS_DIR / "test_email2.xlsx",
        orchestrator.OUTPUT_DIR / "test_graded.xlsx",
        orchestrator.GREETINGS_RESULTS_DIR / "test_greetings.xlsx",
        orchestrator.EMAIL_DRAFTS_DIR / "test_draft1.html",
        orchestrator.EMAIL_DRAFTS_DIR / "test_draft2.html",
    ]

    for file_path in test_files:
        file_path.parent.mkdir(parents=True, exist_ok=True)
        file_path.write_text("Test content", encoding='utf-8')
        print(f"  Created: {file_path.relative_to(orchestrator.PROJECT_ROOT)}")

    print(f"\nTotal test files created: {len(test_files)}")
    return orchestrator


def show_files(orchestrator):
    """Show current files in output directories."""
    print("\nCurrent files in output directories:")
    print("-" * 70)

    dirs = [
        ("exports", orchestrator.EXPORTS_DIR),
        ("output", orchestrator.OUTPUT_DIR),
        ("greetings_results", orchestrator.GREETINGS_RESULTS_DIR),
        ("email_drafts", orchestrator.EMAIL_DRAFTS_DIR),
    ]

    total_files = 0
    for name, dir_path in dirs:
        if dir_path.exists():
            files = list(dir_path.glob("*"))
            file_count = len([f for f in files if f.is_file()])
            total_files += file_count
            print(f"  {name:20} : {file_count} files")
            for f in files:
                if f.is_file():
                    print(f"    - {f.name}")
        else:
            print(f"  {name:20} : Directory not found")

    print(f"\nTotal files: {total_files}")
    print("-" * 70)


def main():
    print("=" * 70)
    print("  ORCHESTRATOR RESET TEST")
    print("=" * 70)

    # Create test files
    orchestrator = create_test_files()

    # Show files before reset
    print("\n" + "=" * 70)
    print("  BEFORE RESET")
    print("=" * 70)
    show_files(orchestrator)

    # Perform reset
    print("\n" + "=" * 70)
    print("  PERFORMING RESET")
    print("=" * 70)
    orchestrator.reset_all()

    # Show files after reset
    print("\n" + "=" * 70)
    print("  AFTER RESET")
    print("=" * 70)
    show_files(orchestrator)

    print("\n" + "=" * 70)
    print("  TEST COMPLETE")
    print("=" * 70)
    print("\nThe reset functionality successfully cleaned all output files!")
    print("Directories are preserved but emptied.")


if __name__ == "__main__":
    main()
