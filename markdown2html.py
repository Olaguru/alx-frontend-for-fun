#!/usr/bin/python3
"""
Markdown to HTML conversion script.
A script markdown2html.py that takes 2 arguments:
1. The name of the Markdown file
2. The output HTML file name
"""
import sys
import os

# Check if the number of arguments is exactly 3
if len(sys.argv) != 3:
    # Print usage to STDERR and exit with code 1
    sys.stderr.write('Usage: ./markdown2html.py README.md README.html\n')
    sys.exit(1)

# Assign arguments to variables
markdownFile = sys.argv[1]
htmlFile = sys.argv[2]

# Check if the Markdown file exists
if not os.path.isfile(markdownFile):
    # Print an error message if the file is missing and exit with code 1
    sys.stderr.write(f'Missing {markdownFile}\n')
    sys.exit(1)

# If the script runs without any issue, exit with success code 0
sys.exit(0)
