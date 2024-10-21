#!/usr/bin/python3
""" Markdown to Html"""
import sys
import os
""" sys for args and os to check file"""


if len(sys.argv) < 3:
    """ confirm the args coming in"""
    sys.stderr.write('Usage: ./markdown2html.py README.md README.html\n')
    sys.exit(1)

markdownFile = sys.argv[1]
htmlFile = sys.argv[2]


if not os.path.isfile(markdownFile):
    """check markdown if it is a markdownfile"""
    sys.stderr.write(f'Missing {mardownFile}\n')
    sys.exit(1)

sys.exit(0)
