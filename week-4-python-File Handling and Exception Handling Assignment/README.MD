# File Processing Utilities

This repository contains Python scripts to manage, modify, and interact with text files. Each script serves a specific purpose, offering functionality such as reading files, handling errors, modifying content, and appending text to files.

## Files in This Repository

### 1. **file_error.reader_.py**

**Purpose:**
A simple program for reading files with basic error handling. It ensures smooth user interaction when dealing with missing or inaccessible files.

**Key Features:**

- Reads and displays file contents.
- Provides file statistics (number of lines, words, and characters).
- Handles common errors like:
  - File not found.
  - Permission errors.
  - Unexpected exceptions.

**Usage:**
Run the script and provide the file name when prompted. Type `quit` to exit the program.

```bash
python file_error.reader_.py
```

### 2. file_processing.py

**Purpose:**
Allows users to read and modify the content of a file with options for uppercase conversion, lowercase conversion, or reversing the text.

**Key Features:**

- Reads and displays file content.
- Provides three modification options:
  1. Convert to uppercase.
  2. Convert to lowercase.
  3. Reverse the text.
- Saves the modified content to a new file (`modified_<original_filename>`).
- Handles common errors such as:
  - File not found.
  - Permission errors.
  - Invalid user input.

**Usage:**
Run the script and follow the prompts to read a file and apply modifications.

```bash
python file_processing.py
```

### 3. `add-content.in.file.py`

**Purpose:**
Manages text files by allowing users to add custom content or create a new file if it doesn't exist.

**Key Features:**

- Checks if a file exists.
- Provides an option to create a new file if it doesn’t exist.
- Allows adding custom text to an existing or new file.
- Supports reading file content.
- Handles errors such as:
  - File not found.
  - Permission errors.
  - Invalid actions.

**Usage:**
Run the script and follow the prompts to add or read content from a file.

```bash
python add-content.in.file.py
```

## Prerequisites

- Python 3.x
- Basic understanding of file handling in Python.

## Error Handling

Each script incorporates error handling for smoother user experience. Common exceptions like `FileNotFoundError` and `PermissionError` are managed gracefully.

## License

This repository is open-source and available for personal and educational purposes.

---

Feel free to modify these scripts to suit your specific needs or enhance their functionality.
