#!/usr/bin/python3
"""
markdown2html.py: A script to check the existence of a Markdown file and
convert it to HTML.

Usage:
    ./markdown2html.py <markdown_file> <output_file>
"""

import sys
import os

def main():
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

if __name__ == "__main__":
    main()
