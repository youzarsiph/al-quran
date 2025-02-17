# Contribution Guidelines

Thank you for your interest in contributing to the Quran API project! Your contributions are essential to ensuring the project remains robust, efficient, and useful to the community. Please follow these guidelines to make the contribution process smooth and effective.

## Table of Contents

- [Contribution Guidelines](#contribution-guidelines)
  - [Table of Contents](#table-of-contents)
  - [Code of Conduct](#code-of-conduct)
  - [How to Contribute](#how-to-contribute)
  - [Development Setup](#development-setup)
  - [Contributing Code](#contributing-code)
  - [Testing](#testing)
  - [Code Style](#code-style)
  - [Pull Requests](#pull-requests)
  - [Reporting Issues](#reporting-issues)
  - [Code Reviews](#code-reviews)
  - [Commit Message Guidelines](#commit-message-guidelines)

## Code of Conduct

Before making any contributions, please read and adhere to the [Code of Conduct](CODE_OF_CONDUCT.md). This document outlines the expected behavior of contributors in the project community to ensure a positive and respectful environment for everyone.

## How to Contribute

We welcome various types of contributions, including:

- **Code:** Bug fixes, new features, improvements to documentation, and performance enhancements.
- **Documentation:** Improving, correcting, or expanding documentation.
- **Ideas:** Suggestions for new features or improvements.
- **Bug Reports:** Reporting and fixing issues.

## Development Setup

Ensure your local development environment is set up correctly by following these steps:

1. **Fork the Repository:**

   - Navigate to the [Quran API repository](https://github.com/youzarsiph/al-quran) on GitHub.
   - Click on the "Fork" button to create a personal copy of the repository.

2. **Clone Your Fork:**

   ```bash
   git clone https://github.com/<your-username>/al-quran.git
   cd al-quran
   ```

3. **Set Up a Virtual Environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

4. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

## Contributing Code

When contributing code, please keep the following in mind:

- **Branching:** Create a new branch for your feature or bug fix.

  ```bash
  git checkout -b feature/AmazingFeature
  ```

- **Atomic Commits:** Ensure each commit addresses a single issue or adds a single new feature.
- **Code Quality:** Write clean, maintainable, and well-documented code. Follow our [Code Style](#code-style) guidelines.

## Testing

- **Run Tests:** Ensure all tests pass before submitting a pull request.

  ```bash
  python manage.py test
  ```

- **Write Tests:** Add tests for any new functionality or bug fixes.

## Code Style

To maintain consistency, we follow these coding conventions:

- **Formatter:** Use [Black](https://github.com/psf/black) to format your code.

  ```bash
  black .
  ```

- **Linter:** Use [Ruff](https://github.com/astral-sh/ruff) for linting.

  ```bash
  ruff .
  ```

- **Naming Conventions:** Use descriptive names for variables, functions, and classes. Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) guidelines.

## Pull Requests

When submitting a pull request:

- **Title:** Use a clear, concise title that summarizes the changes.
- **Description:** Provide detailed information about the purpose and implementation of the changes.
- **Screenshots:** Include screenshots or videos if the changes affect the user interface.
- **Link Issues:** Reference any related issues in the pull request description.

## Reporting Issues

When reporting an issue:

- **Describe the Problem:** Provide a detailed description of the issue, including steps to reproduce it.
- **Expected Behavior:** Explain what should happen instead.
- **Environment:** Specify your operating system, Python version, and any other relevant details.
- **Screenshots:** Attach screenshots or videos if applicable.

## Code Reviews

All pull requests will undergo a code review process. We encourage constructive feedback and aim to provide timely reviews.

- **Respond to Feedback:** Address any feedback provided by the reviewers.
- **Update Pull Request:** Make necessary changes and update the pull request as needed.

## Commit Message Guidelines

Commit messages should be clear and informative. We follow the [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) standard:

- **Type:** Indicates the kind of change (`feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`).
- **Scope:** (Optional) The scope of the change.
- **Description:** A brief description of the change.

Example:

```bash
git commit -m "fix(api): resolve issue with verse pagination"
```

---

By following these guidelines, you can help maintain the high quality and reliability of the Quran API project. Your contributions are deeply appreciated!
