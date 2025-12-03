# Command: New Program Implementation Requirements

This document outlines the requirements and best practices for developing new programs as packages. These guidelines should be followed by all LLMs and developers to ensure consistency, maintainability, and quality.

## 1. Develop as a Package

All new programs should be structured as a distributable package. This includes:

-   A `pyproject.toml` or `setup.py` file to define package metadata, dependencies, and entry points.
-   A clear directory structure, typically with a source directory (e.g., `src/`).
-   A `README.md` file with instructions on installation, configuration, and usage.
-   A `LICENSE` file.

## 2. Class Size Limitation

To promote modularity and readability, each class should have a maximum of **150 lines** of code. If a class exceeds this limit, it should be refactored into smaller, more focused classes.

## 3. Agent Folder Structure

When new agents are developed, they must be placed in a dedicated folder.

-   The folder should be named after the agent (e.g., `new_agent_name/`).
-   This folder should be located within a general `agents/` directory if applicable.
-   All files related to the agent should be contained within its folder.

## 4. Logging and Retry Mechanisms

-   **Logging:**
    -   Use the `logging` module for all debugging and informational output.
    -   Do not use `print()` for debugging.
    -   Configure log levels (DEBUG, INFO, WARNING, ERROR, CRITICAL) appropriately.
    -   Log messages should be clear and informative.

-   **Retry Mechanism:**
    -   Implement a retry mechanism (e.g., using a decorator with exponential backoff) for operations that may fail intermittently, such as network requests or API calls. This is crucial for building resilient systems.

## 5. Use of `.env` for Configuration

-   All configuration variables, especially secrets and environment-specific settings, must be stored in a `.env` file.
-   The `.env` file should **never** be committed to version control. Add it to `.gitignore`.
-   A `.env.example` file should be provided with placeholder values to guide users on the required configuration.
-   The application should load these variables from the `.env` file at runtime (e.g., using a library like `python-dotenv`).
