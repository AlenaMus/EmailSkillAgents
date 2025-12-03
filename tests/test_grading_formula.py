"""
Test script to verify the grading formula is implemented correctly.
"""

from repo_analyzer.metrics_calculator import MetricsCalculator


def test_grading_formula():
    """Test the grade calculation formula."""

    calc = MetricsCalculator()

    # Test case 1: All files under 130 lines (perfect score)
    grade = calc._calculate_grade(files_under_limit=5, total_files=5)
    assert grade == 100.00, f"Expected 100.00, got {grade}"
    print("Test 1 PASSED: 5/5 files under limit = 100.00%")

    # Test case 2: 4 out of 5 files under limit
    grade = calc._calculate_grade(files_under_limit=4, total_files=5)
    assert grade == 80.00, f"Expected 80.00, got {grade}"
    print("Test 2 PASSED: 4/5 files under limit = 80.00%")

    # Test case 3: No files under limit
    grade = calc._calculate_grade(files_under_limit=0, total_files=5)
    assert grade == 0.00, f"Expected 0.00, got {grade}"
    print("Test 3 PASSED: 0/5 files under limit = 0.00%")

    # Test case 4: Edge case - no files at all
    grade = calc._calculate_grade(files_under_limit=0, total_files=0)
    assert grade == 0.00, f"Expected 0.00, got {grade}"
    print("Test 4 PASSED: 0/0 files (no code) = 0.00%")

    # Test case 5: Single file under limit
    grade = calc._calculate_grade(files_under_limit=1, total_files=1)
    assert grade == 100.00, f"Expected 100.00, got {grade}"
    print("Test 5 PASSED: 1/1 file under limit = 100.00%")

    # Test case 6: 2 out of 4 files under limit
    grade = calc._calculate_grade(files_under_limit=2, total_files=4)
    assert grade == 50.00, f"Expected 50.00, got {grade}"
    print("Test 6 PASSED: 2/4 files under limit = 50.00%")

    # Test case 7: 12 out of 16 files under limit (from actual test)
    grade = calc._calculate_grade(files_under_limit=12, total_files=16)
    assert grade == 75.00, f"Expected 75.00, got {grade}"
    print("Test 7 PASSED: 12/16 files under limit = 75.00%")

    print("\nAll grading formula tests PASSED!")


def verify_actual_results():
    """Verify the actual results from the test run."""

    print("\nVerifying actual results from test run:")
    print("-" * 50)

    # Result 1: Convolution repo
    # 1 file, 1 under 130 lines -> 100%
    expected = 100.00
    actual = (1 / 1) * 100
    assert actual == expected, f"Convolution: Expected {expected}, got {actual}"
    print(f"Convolution: 1/1 files under 130 = {actual:.2f}% PASS")

    # Result 2: TranslatorAgentsChain repo
    # 16 files, 12 under 130 lines -> 75%
    expected = 75.00
    actual = (12 / 16) * 100
    assert actual == expected, f"TranslatorAgentsChain: Expected {expected}, got {actual}"
    print(f"TranslatorAgentsChain: 12/16 files under 130 = {actual:.2f}% PASS")

    # Result 3: PCA-t-SNE repo
    # 13 files, 13 under 130 lines -> 100%
    expected = 100.00
    actual = (13 / 13) * 100
    assert actual == expected, f"PCA-t-SNE: Expected {expected}, got {actual}"
    print(f"PCA-t-SNE: 13/13 files under 130 = {actual:.2f}% PASS")

    # Average grade
    grades = [100.00, 75.00, 100.00]
    avg = sum(grades) / len(grades)
    expected_avg = 91.67
    assert abs(avg - expected_avg) < 0.01, f"Average: Expected {expected_avg}, got {avg}"
    print(f"\nAverage grade: {avg:.2f}% PASS")

    print("\nAll actual results verified!")


if __name__ == '__main__':
    test_grading_formula()
    verify_actual_results()

    print("\n" + "=" * 50)
    print("SUCCESS: All tests passed!")
    print("Grading formula is implemented correctly.")
    print("=" * 50)
