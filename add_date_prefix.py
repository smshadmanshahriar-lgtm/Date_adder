import os
import argparse
from datetime import datetime

def add_date_prefix(directory):
    today = datetime.now().strftime("%Y-%m-%d")
    prefix = f"{today}_"
    
    if not os.path.isdir(directory):
        print(f"Error: {directory} is not a valid directory.")
        return

    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    
    for filename in files:
        if filename.startswith(prefix):
            print(f"Skipping {filename}: Already prefixed.")
            continue
            
        old_path = os.path.join(directory, filename)
        new_path = os.path.join(directory, f"{prefix}{filename}")
        
        try:
            os.rename(old_path, new_path)
            print(f"Renamed: {filename} -> {prefix}{filename}")
        except Exception as e:
            print(f"Failed to rename {filename}: {e}")

def main():
    parser = argparse.ArgumentParser(description="Add today's date prefix (YYYY-MM-DD) to filenames in a folder.")
    parser.add_argument("directory", nargs="?", default=".", help="The folder path (default: current directory)")
    
    args = parser.parse_args()
    add_date_prefix(args.directory)

if __name__ == "__main__":
    main()
