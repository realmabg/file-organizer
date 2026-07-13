# File Organizer CLI

A command-line Python tool that organizes files in a folder based on file type, modification date, or filename keyword.

## Features

- Organize files by file extension (PDF, TXT, PNG, etc.)
- Organize files by last modified date (YYYY-MM)
- Organize files containing a specific keyword
- Error handling for:
  - Missing folders
  - Invalid paths
  - Empty folders
  - Duplicate files
  - Unsupported file types
  - No keyword matches
- Automated unit tests using pytest
- Continuous Integration with GitHub Actions
- Automatic code formatting with Black

---

## Project Structure

```
.
├── organizer.py
├── tests/
│   └── test_code.py
├── DESIGN.md
├── Flow.md
├── README.md
└── .github/
    └── workflows/
        └── python-tests.yml
```

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd file-organizer
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it.

macOS/Linux:

```bash
source .venv/bin/activate
```

Windows:

```powershell
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install pytest black
```

---

## Running the Program

Run:

```bash
python organizer.py
```

Choose one of the options:

```
1. Organize by file type
2. Organize by date
3. Organize by keyword
```

Then enter the folder path.

---

## Example

Before:

```
Downloads/
├── report.pdf
├── notes.txt
├── photo.jpg
```

Choose:

```
1
```

After:

```
Downloads/
├── pdf/
│   └── report.pdf
├── txt/
│   └── notes.txt
├── jpg/
│   └── photo.jpg
```

---

## Running Tests

Run all tests:

```bash
python -m pytest
```

---

## Formatting

Check formatting:

```bash
black --check .
```

Automatically format code:

```bash
black .
```

---

## GitHub Actions

GitHub Actions automatically:

- installs Python
- installs project dependencies
- checks formatting with Black
- runs all pytest unit tests

on every push and pull request.

---

## Design Notes

The application is organized into separate functions for each organization method:

- `organize_by_type()`
- `organize_by_date()`
- `organize_by_keyword()`

The `main()` function provides the command-line interface and calls the appropriate function based on the user's selection.

The project separates application logic from the CLI, making the functions easy to test independently with pytest.

Additional design details are documented in `DESIGN.md`, and the workflow is illustrated in `Flow.md`.