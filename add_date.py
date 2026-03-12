import os
import argparse
from datetime import datetime

def add_date_prefix(directory):
    """
    Adds today's date (YYYY-MM-DD) to the beginning of every filename in the specified folder.
    """
    # Get today's date in YYYY-MM-DD format
    today = datetime.now().strftime("%Y-%m-%d")
    prefix = f"{today}_"
    
    # Check if the provided path is a valid directory
    if not os.path.isdir(directory):
        print(f"Error: '{directory}' is not a valid directory.")
        return

    # List all items in the directory
    try:
        items = os.listdir(directory)
    except Exception as e:
        print(f"Error accessing directory: {e}")
        return

    count = 0
    for filename in items:
        old_path = os.path.join(directory, filename)
        
        # Process only files (skip directories)
        if os.path.isfile(old_path):
            # Skip if the file already has the prefix to avoid double-prefixing
            if filename.startswith(prefix):
                print(f"Skipping '{filename}': Already prefixed.")
                continue
            
            new_filename = f"{prefix}{filename}"
            new_path = os.path.join(directory, new_filename)
            
            try:
                os.rename(old_path, new_path)
                print(f"Renamed: '{filename}' -> '{new_filename}'")
                count += 1
            except Exception as e:
                print(f"Failed to rename '{filename}': {e}")
    
    print(f"\nSuccessfully renamed {count} files.")

def main():
    parser = argparse.ArgumentParser(description="Add today's date prefix (YYYY-MM-DD) to filenames in a folder.")
    parser.add_argument("directory", nargs="?", default=".", help="The folder path to process (default: current directory)")
    
    args = parser.parse_args()
    
    # Confirmation for current directory
    if args.directory == ".":
        confirm = input("Process files in the CURRENT directory? (y/n): ").lower()
        if confirm != 'y':
            print("Operation cancelled.")
            return

    add_date_prefix(args.directory)

if __name__ == "__main__":
    main()
