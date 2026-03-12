# Date Adder Utility

A collection of Python scripts for date-related file operations.

## Current Scripts

### 1. `add_date.py`
This script adds today's date (YYYY-MM-DD) as a prefix to every file in a specified directory.

#### Usage
```bash
python add_date.py [folder_path]
```
- If no `folder_path` is provided, it defaults to the current directory (with a confirmation prompt).
- It skips files that already have the today's date prefix to avoid duplication.

## Project Structure
- `MD_files/`: A sample directory containing markdown files prefixed with dates.
- `Gemini.md`: Contains the original AI prompt used to generate the scripts.
- `add_date.py`: The main file renaming utility.

## Testing
To test the renaming script, you can create a test folder with dummy files and run:
```bash
python add_date.py test_folder
```
