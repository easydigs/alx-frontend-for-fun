#!/usr/bin/python3
"""
markdown2html.py: A script to check the existence of a Markdown file and
convert it to HTML.

Usage:
    ./markdown2html.py <markdown_file> <output_file>
"""

import sys
import os

def convert_line_to_html(line, in_ulist, in_olist):
    """
    Converts a single line of Markdown to HTML.
    
    Supports converting Markdown headings (e.g., #, ##, ###), unordered lists 
    (e.g., - item), and ordered lists (e.g., * item) to corresponding HTML tags.
    
    :param line: The line of Markdown to convert
    :param in_ulist: A boolean flag to indicate if the current line is inside an unordered list
    :param in_olist: A boolean flag to indicate if the current line is inside an ordered list
    :return: A tuple of the converted HTML line and the updated in_ulist and in_olist statuses
    """
    html_line = ""
    
    # Check for heading syntax
    if line.startswith("#"):
        heading_level = len(line.split(' ')[0])
        if heading_level <= 6:
            content = line[heading_level:].strip()
            html_line = f"<h{heading_level}>{content}</h{heading_level}>\n"
            return html_line, in_ulist, in_olist

    # Check for unordered list item
    if line.startswith("- "):
        if in_olist:
            html_line += "</ol>\n"
            in_olist = False
        if not in_ulist:
            html_line += "<ul>\n"
            in_ulist = True
        content = line[2:].strip()
        html_line += f"    <li>{content}</li>\n"
        return html_line, in_ulist, in_olist

    # Check for ordered list item
    if line.startswith("* "):
        if in_ulist:
            html_line += "</ul>\n"
            in_ulist = False
        if not in_olist:
            html_line += "<ol>\n"
            in_olist = True
        content = line[2:].strip()
        html_line += f"    <li>{content}</li>\n"
        return html_line, in_ulist, in_olist

    # Close any open lists if the line doesn't match list syntax
    if in_ulist:
        html_line += "</ul>\n"
        in_ulist = False
    if in_olist:
        html_line += "</ol>\n"
        in_olist = False

    html_line += line  # Preserve other content
    return html_line, in_ulist, in_olist

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

    in_ulist = False  # Flag to track if we're inside an unordered list
    in_olist = False  # Flag to track if we're inside an ordered list

    # Open the Markdown file for reading and the output file for writing
    with open(markdown_file, 'r') as md_file, open(output_file, 'w') as html_file:
        for line in md_file:
            # Convert each line from Markdown to HTML
            html_line, in_ulist, in_olist = convert_line_to_html(line, in_ulist, in_olist)
            html_file.write(html_line)

        # Close any open lists at the end of the file
        if in_ulist:
            html_file.write("</ul>\n")
        if in_olist:
            html_file.write("</ol>\n")

    # Exit successfully
    sys.exit(0)

if __name__ == "__main__":
    main()
