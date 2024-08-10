#!/usr/bin/python3
"""
markdown2html.py: A script to check the existence of a Markdown file and
convert it to HTML.

Usage:
    ./markdown2html.py <markdown_file> <output_file>
"""

import sys
import os

def convert_line_to_html(line):
    """
    Converts a single line of Markdown to HTML.
    
    Currently supports converting Markdown headings (e.g., #, ##, ###) to
    corresponding HTML tags.
    """
    # Check for heading syntax
    if line.startswith("#"):
        heading_level = len(line.split(' ')[0])
        if heading_level <= 6:
            content = line[heading_level:].strip()
            return f"<h{heading_level}>{content}</h{heading_level}>\n"
    
    # If no heading syntax is found, return the line as is
    return line

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

    # Open the Markdown file for reading and the output file for writing
    with open(markdown_file, 'r') as md_file, open(output_file, 'w') as html_file:
        for line in md_file:
            # Convert each line from Markdown to HTML
            html_line = convert_line_to_html(line)
            html_file.write(html_line)

    # Exit successfully
    sys.exit(0)

if __name__ == "__main__":
    main()
