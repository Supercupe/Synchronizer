# Directory Synchronization Tool

This project provides a simple command-line tool for synchronizing files and directories between a source and a destination (replica) folder. The tool ensures that the destination folder is an exact copy of the source folder, including all nested directories and files.

## Features

- **One-Way Synchronization**: Makes the destination directory exactly match the source directory.
- **Periodic Updates**: Synchronizes the directories at specified intervals.
- **Logging**: Provides console output for file and directory creation, updates, and deletions.
- **No Third-Party Libraries**: Utilizes only built-in Python libraries for functionality.

## Requirements

- Python 3.x
- Basic knowledge of command-line usage

## Usage
- To run the code You need to run your script and provide path to your source and replica folder. After entenig your paths provide an integer for periodical upadte in seconds. 
- Example: python3 index.py "/path/to/source" /path/to/replica" 10
  
