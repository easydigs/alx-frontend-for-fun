#!/usr/bin/python3
import sys
import os

# Check if the number of arguments is less than 2
if len(sys.argv) < 3:
    print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
    sys.exit(1)

# Extract the filenames from the arguments
markdown_file = sys.argv[1]
output_file = sys.argv[2]

# Check if the Markdown file exists
if not os.path.isfile(markdown_file):
    print(f"Missing {markdown_file}", file=sys.stderr)
    sys.exit(1)

# If all checks are passed, print nothing and exit with status 0
sys.exit(0)
