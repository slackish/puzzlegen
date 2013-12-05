#!/usr/bin/python
"""
I wanted something to quickly move these to a nicely formatted
pdf.  I'm going to add circles in manually
"""

import string
import sys

def preamble():
    print "\\documentclass[]{article}"
    print "\\usepackage{sudoku}"
    print "\\begin{document}"
    print "\\begin{sudoku}"

def main():
    f = sys.argv[-1]
    data = open(f).read().split("\n\n")[2].split("\n")
    trans = string.maketrans(" .", "| ")
    preamble()
    for i in data:
        if i.startswith("----"):
            continue
        i = "".join(i.split("|"))
        i = " ".join(i.split("  "))
        print "%s|." % i.translate(trans)
    postamble()

def postamble():
    print "\\end{sudoku}"
    print "\\end{document}"



if __name__ == "__main__":
    main()
