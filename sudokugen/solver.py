#!/usr/bin/python
"""
A way to generate some letter-based sudoku puzzles
and make sure that the passphrase is in a puzzle

Probably a smarter way to do it, but this took about an hour to write.

python solver.py "inputtexthere"
"""


import random
import string
import sys
import subprocess
import traceback

QQWING = "/home/amcphall/projects/2012/christmas/sudoku/qqwing-1.0.3/qqwing"
ARGS = [QQWING, "--generate", "--solution", "--difficulty", "intermediate"]
LETTERS = "ETAOINSHRDLCUMWFGYPBVKJXQZ"

def validate(text):
    """ Make sure that text will actually work """
    order = list("".join(text.split()))
    uniq = []
    for i in order:
        if i not in uniq:
            uniq.append(i)
    if len(uniq) > 9:
        print "too many letters"
        sys.exit(1)
    if len(uniq) > 9:
        print "too many letters"
        sys.exit(1)
    uniq = fill_letters(uniq)
    return order, uniq


def fill_letters(uniq):
    """ append extra letters, if need be """
    while len(uniq) != 9:
        for i in LETTERS:
            if i in uniq:
                continue
            else:
                uniq.append(i)
                break
    return uniq
    

def gen_board():
    """ lets grab a board """
    try:
        p = subprocess.Popen(ARGS, stdout=subprocess.PIPE)
        (stdout, stderr) = p.communicate()
        return stdout.strip().split('\n\n',1)
    except:
        traceback.print_exc()
        print ARGS
        sys.exit(2)
        
def parse_board(board):
    """ figure out how the board works """
    parsed = []
    oneline = []
    rcount = 0
    for r in board.split('\n'):
        if r.startswith("----"):
            continue
        parsed.append([])
        for c in r.split():
            if c in "123456789.":
                parsed[rcount].append(c)
                oneline.append(c)
        rcount += 1
    # validate everything
    if rcount != 9:
        print "not right amount of rows", rcount
        sys.exit(3)
    for i in parsed:
        if len(i) != 9:
            print "not right amount of rows"
            sys.exit(4)
    return "".join(oneline)


def trial(order, uniq):
    """ bulk of work, figure out if things will fit """
    boards = gen_board()
    solution = parse_board(boards[1])
    numbers = [str(x) for x in range(1, 10)]
    order = str(order)

    #for i in xrange(1,10):
    #    i = str(i)
    #    if i not in boards[0]:
    #        return

    trials = 0
    notsolved = True

    while notsolved and trials < 30:
        random.shuffle(uniq)
        random.shuffle(numbers)
        trans = string.maketrans("".join(uniq), "".join(numbers))
        test = order.translate(trans)
        notsolved = x_in_y(test, solution)

    if notsolved:
        return
    else:
        trans = string.maketrans("".join(numbers), "".join(uniq))
        print "Success!"
        print "Input"
        print "".join(order)
        print ""
        print "Translation:"
        print "".join(uniq)
        print "".join(numbers)
        print ""
        print "", boards[0].translate(trans)
        print ""
        print boards[1].translate(trans)
        sys.exit(0)

def x_in_y(x, y):
    xcount = 0
    xlen = len(x)
    for i in y:
        if i == x[xcount]:
            xcount += 1
            if xcount == xlen:
                return True
    return False



def main():
    text = sys.argv[-1].strip().upper()
    order, uniq = validate(text)
    print order, uniq
    for i in xrange(50):
        trial(order, uniq)
    print "failed"
    sys.exit(6)
        

if __name__ == "__main__":
    main()

