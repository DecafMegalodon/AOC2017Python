# https://adventofcode.com/2017/day/10
import fileinput
from day10knothash import *

"""
Our input is a list of lengths
Our "state" is 256 elements long, circular, and 0 indexed
Lengths larger than the size of the list are invalid.


Reverse the order of that length of elements in the list
    starting with the element at the current position.
Move the current position forward by that length plus the skip size.
Increase the skip size by one.
"""

indata = fileinput.input().readline()[:-1:]  # Omit the trailing newline
knothash = calcKnotHash(indata)
print(printableHash(knothash))
