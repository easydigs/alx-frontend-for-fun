#!/usr/bin/python3
"""
markdown2html.py: A script to check the existence of a Markdown file and
convert it to HTML.

Usage:
    ./markdown2html.py <markdown_file> <output_file>
"""

import sys
import os

def convert_line_to_html(line, in_list):
    """
    Converts a single line of Markdown to HTML.
    
    Supports converting Markdown headings (e.g., #, ##, ###) and unordered
    lists (e.g., - item) to corresponding HTML tags.
    
    :param line: The line of Markdown to convert
    :param in_list: A boolean flag to indicate if the current line is inside a list
    :return: A tuple of the converted HTML line and the updated in_list status
    """
    html_line = ""
    
    # Check for heading syntax
    if line.startswith("#"):
        heading_level = len(line.split(' ')[0])
        if heading_level <= 6:
            content = line[heading_level:].strip()
            html_line = f"<h{heading_level}>{content}</h{heading_level}>\n"
            return html_line, in_list

    # Check for unordered list item
    if line.startswith("- "):
        if not in_list:
            html_line += "<ul>\n"
            in_list = True
        content = line[2:].strip()
        html_line += f"    <li>{content}</li>\n"
    else:
        if in_list:
            html_line += "</ul>\n"
            in_list = False
        html_line += line  # Preserve other content

    return html_line, in_list

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

    in_list = False  # Flag to track if we're inside a list

    # Open the Markdown file for reading and the output file for writing
    with open(markdown_file, 'r') as md_file, open(output_file, 'w') as html_file:
        for line in md_file:
            # Convert each line from Markdown to HTML
            html_line, in_list = convert_line_to_html(line, in_list)
            html_file.write(html_line)

        # Close any open list at the end of the file
        if in_list:
            html_file.write("</ul>\n")

    # Exit successfully
    sys.exit(0)

if __name__ == "__main__":
    main()
