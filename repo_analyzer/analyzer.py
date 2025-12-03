"""
Main orchestrator for Repository Analyzer Agent.
Coordinates Excel reading, repository cloning, metrics calculation, and output generation.
"""

import time
from typing import List, Dict
from pathlib import Path

from .excel_manager import ExcelManager
from .repo_manager import RepositoryManager
from .metrics_calculator import MetricsCalculator
from .config import STATUS_SUCCESS, STATUS_ERROR, VERSION
from .errors import (
    ExcelError,
    RepositoryError,
    NoCodeFilesError,
    MetricsCalculationError
)


class RepositoryAnalyzer:
    """Main analyzer orchestrator."""

    def __init__(self, verbose: bool = False):
        """
        Initialize analyzer.

        Args:
            verbose: Enable verbose output
        """
        self.verbose = verbose
        self.excel_manager = ExcelManager()
        self.repo_manager = None  # Created when needed
        self.metrics_calculator = MetricsCalculator()

    def analyze(self, input_path: str, output_path: str = None) -> Dict:
        """
        Analyze repositories from Excel file.

        Args:
            input_path: Path to input Excel file
            output_path: Path to output Excel file (optional, auto-generated if None)

        Returns:
            Dict with summary statistics

        Raises:
            ExcelError: If Excel operations fail
        """
        print(f"Repository Analyzer v{VERSION}")
        print("=" * 50)
        print()

        start_time = time.time()

        try:
            # Step 1: Read input Excel
            print(f"Reading input: {input_path}")
            original_data = self.excel_manager.read_input(input_path)
            print(f"Found {len(original_data)} repository URLs")
            print()

            # Step 2: Process repositories (SEQUENTIAL for Phase 1)
            print("Processing repositories...")
            results = self._process_repositories_sequential(original_data)

            # Step 3: Write output Excel
            if output_path is None:
                output_path = self.excel_manager.generate_output_path(input_path)

            processing_time = time.time() - start_time

            print()
            print("Writing output...")
            self.excel_manager.write_output(
                output_path,
                original_data,
                results,
                processing_time
            )

            # Step 4: Display summary
            summary = self._generate_summary(results, processing_time)
            self._display_summary(summary, output_path)

            return summary

        finally:
            # Cleanup temporary files
            if self.repo_manager:
                print()
                self.repo_manager.cleanup()

    def _process_repositories_sequential(self, data: List[Dict]) -> List[Dict]:
        """
        Process repositories sequentially (Phase 1 MVP).

        Args:
            data: List of repository data from Excel

        Returns:
            List of results for each repository
        """
        # Initialize repository manager
        self.repo_manager = RepositoryManager()

        print(f"Temporary directory: {self.repo_manager.get_temp_dir()}")
        print()

        results = []
        total = len(data)

        for idx, repo_data in enumerate(data, start=1):
            url = repo_data['url']
            print(f"[{idx}/{total}] Analyzing {url}...")

            result = self._process_single_repository(url)
            results.append(result)

            # Display result
            if result['status'] == STATUS_SUCCESS:
                grade = result['grade']
                print(f"  Grade: {grade:.2f}%")
            else:
                error = result['error']
                print(f"  Error: {error}")

            print()

        return results

    def _process_single_repository(self, url: str) -> Dict:
        """
        Process a single repository: clone, calculate metrics, grade.

        Args:
            url: Repository URL

        Returns:
            Dict with keys: url, grade, total_files, files_under_130,
                           total_lines, status, error
        """
        result = {
            'url': url,
            'grade': 0.0,
            'total_files': 0,
            'files_under_130': 0,
            'total_lines': 0,
            'status': STATUS_ERROR,
            'error': ''
        }

        try:
            # Step 1: Clone repository
            local_path, success, error = self.repo_manager.clone(url)

            if not success:
                result['error'] = error
                result['status'] = self._determine_status_from_error(error)
                return result

            # Step 2: Calculate metrics
            metrics = self.metrics_calculator.calculate(local_path)

            # Step 3: Check for edge case (no code files)
            if metrics['total_files'] == 0:
                result['error'] = 'No code files found in repository'
                result['status'] = 'No Code Files'
                return result

            # Step 4: Populate results
            result['grade'] = metrics['grade']
            result['total_files'] = metrics['total_files']
            result['files_under_130'] = metrics['files_under_130']
            result['total_lines'] = metrics['total_lines']
            result['status'] = STATUS_SUCCESS

            return result

        except MetricsCalculationError as e:
            result['error'] = f"Metrics calculation failed: {str(e)}"
            result['status'] = STATUS_ERROR
            return result

        except Exception as e:
            result['error'] = f"Unexpected error: {str(e)}"
            result['status'] = STATUS_ERROR
            return result

    def _determine_status_from_error(self, error: str) -> str:
        """
        Determine status code from error message.

        Args:
            error: Error message

        Returns:
            Status string
        """
        error_lower = error.lower()

        if 'not found' in error_lower or '404' in error_lower:
            return 'Not Found'
        elif 'timeout' in error_lower:
            return 'Timeout'
        elif 'access denied' in error_lower or 'forbidden' in error_lower:
            return 'Access Denied'
        elif 'network' in error_lower or 'connection' in error_lower:
            return 'Network Error'
        elif 'invalid' in error_lower:
            return 'Invalid URL'
        else:
            return STATUS_ERROR

    def _generate_summary(self, results: List[Dict], processing_time: float) -> Dict:
        """
        Generate summary statistics.

        Args:
            results: Processing results
            processing_time: Total processing time in seconds

        Returns:
            Summary dict
        """
        total_repos = len(results)
        successful = sum(1 for r in results if r['status'] == STATUS_SUCCESS)
        failed = total_repos - successful

        # Calculate average grade (only for successful repos)
        grades = [r['grade'] for r in results if r['status'] == STATUS_SUCCESS]
        avg_grade = sum(grades) / len(grades) if grades else 0.0

        return {
            'total_repos': total_repos,
            'successful': successful,
            'failed': failed,
            'avg_grade': avg_grade,
            'processing_time': processing_time
        }

    def _display_summary(self, summary: Dict, output_path: str):
        """
        Display summary to console.

        Args:
            summary: Summary statistics
            output_path: Path to output file
        """
        print()
        print("Summary")
        print("=" * 50)
        print(f"Successfully Analyzed: {summary['successful']}/{summary['total_repos']}")

        if summary['failed'] > 0:
            print(f"Failed: {summary['failed']}/{summary['total_repos']}")

        if summary['successful'] > 0:
            print(f"Average Grade: {summary['avg_grade']:.2f}%")

        minutes = int(summary['processing_time'] // 60)
        seconds = int(summary['processing_time'] % 60)
        print(f"Processing Time: {minutes}m {seconds}s")
        print()
        print(f"Output: {output_path}")
        print()
        print("Analysis complete!")
