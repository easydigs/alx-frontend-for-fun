#!/usr/bin/python3
"""
markdown2html.py: A script to check the existence of a Markdown file and
convert it to HTML.

Usage:
    ./markdown2html.py <markdown_file> <output_file>
"""

import sys
import os

def convert_line_to_html(line, in_ulist, in_olist, in_paragraph):
    """
    Converts a single line of Markdown to HTML.
    
    Supports converting Markdown headings (e.g., #, ##, ###), unordered lists 
    (e.g., - item), ordered lists (e.g., * item), and paragraphs to corresponding HTML tags.
    
    :param line: The line of Markdown to convert
    :param in_ulist: A boolean flag to indicate if the current line is inside an unordered list
    :param in_olist: A boolean flag to indicate if the current line is inside an ordered list
    :param in_paragraph: A boolean flag to indicate if the current line is inside a paragraph
    :return: A tuple of the converted HTML line and the updated in_ulist, in_olist, and in_paragraph statuses
    """
    html_line = ""
    stripped_line = line.strip()
    
    # Check for heading syntax
    if stripped_line.startswith("#"):
        heading_level = len(stripped_line.split(' ')[0])
        if heading_level <= 6:
            content = stripped_line[heading_level:].strip()
            html_line = f"<h{heading_level}>{content}</h{heading_level}>\n"
            return html_line, in_ulist, in_olist, in_paragraph

    # Check for unordered list item
    if stripped_line.startswith("- "):
        if in_paragraph:
            html_line += "</p>\n"
            in_paragraph = False
        if in_olist:
            html_line += "</ol>\n"
            in_olist = False
        if not in_ulist:
            html_line += "<ul>\n"
            in_ulist = True
        content = stripped_line[2:].strip()
        html_line += f"    <li>{content}</li>\n"
        return html_line, in_ulist, in_olist, in_paragraph

    # Check for ordered list item
    if stripped_line.startswith("* "):
        if in_paragraph:
            html_line += "</p>\n"
            in_paragraph = False
        if in_ulist:
            html_line += "</ul>\n"
            in_ulist = False
        if not in_olist:
            html_line += "<ol>\n"
            in_olist = True
        content = stripped_line[2:].strip()
        html_line += f"    <li>{content}</li>\n"
        return html_line, in_ulist, in_olist, in_paragraph

    # Handle paragraphs and line breaks
    if stripped_line:
        if not in_paragraph:
            html_line += "<p>\n"
            in_paragraph = True
        else:
            html_line += "    <br />\n"
        html_line += f"    {stripped_line}\n"
        return html_line, in_ulist, in_olist, in_paragraph

    # Close any open paragraphs and lists when encountering a blank line
    if in_paragraph:
        html_line += "</p>\n"
        in_paragraph = False
    if in_ulist:
        html_line += "</ul>\n"
        in_ulist = False
    if in_olist:
        html_line += "</ol>\n"
        in_olist = False

    return html_line, in_ulist, in_olist, in_paragraph

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
    in_paragraph = False  # Flag to track if we're inside a paragraph

    # Open the Markdown file for reading and the output file for writing
    with open(markdown_file, 'r') as md_file, open(output_file, 'w') as html_file:
        for line in md_file:
            # Convert each line from Markdown to HTML
            html_line, in_ulist, in_olist, in_paragraph = convert_line_to_html(line, in_ulist, in_olist, in_paragraph)
            html_file.write(html_line)

        # Close any open paragraphs and lists at the end of the file
        if in_paragraph:
            html_file.write("</p>\n")
        if in_ulist:
            html_file.write("</ul>\n")
        if in_olist:
            html_file.write("</ol>\n")

    # Exit successfully
    sys.exit(0)

if __name__ == "__main__":
    main()
