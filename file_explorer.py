# file_explorer.py  

import os
import argparse
from datetime import datetime

class FileSystemExplorer:
    def __init__(self, path='.', show_hidden=False):
        self.path = path
        self.show_hidden = show_hidden

    def list_files(self):
        """List all files and directories, optionally including hidden files"""
        try:
            files = os.listdir(self.path)
            if not self.show_hidden:
                files = [file for file in files if not file.startswith('.')]
            print(f"Contents of directory: {self.path}\n")
            for file in files:
                print(file)
        except FileNotFoundError:
            print(f"Error: Directory '{self.path}' does not exist.")
        except PermissionError:
            print(f"Error: Permission denied for accessing '{self.path}'.")

    def file_details(self, file_name):
        """Get details of a specific file in the directory"""
        try:
            file_path = os.path.join(self.path, file_name)
            if os.path.isfile(file_path):
                size = os.path.getsize(file_path)
                modification_time = os.path.getmtime(file_path)
                print(f"File: {file_name}")
                print(f"Size: {size} bytes")
                print(f"Last Modified: {datetime.fromtimestamp(modification_time)}")
            else:
                print(f"'{file_name}' is not a file or does not exist.")
        except FileNotFoundError:
            print(f"Error: File '{file_name}' not found.")
        except PermissionError:
            print(f"Error: Permission denied for accessing '{file_name}'.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="File System Explorer Utility")
    parser.add_argument('-p', '--path', type=str, default='.', help="Path to explore")
    parser.add_argument('-f', '--file', type=str, help="Get details of a specific file")
    parser.add_argument('--show-hidden', action='store_true', help="Show hidden files in directory listing")

    args = parser.parse_args()

    explorer = FileSystemExplorer(args.path, args.show_hidden)

    if args.file:
        explorer.file_details(args.file)
    else:
        explorer.list_files()
