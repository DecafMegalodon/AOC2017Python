"""Observations:
Addresses are 1-indexed
A new "ring" starts on n^2 + 1 indices
New "Rings" start near - but not on a corner. 1 away.
The diameter of the current ring is ceiling(sqrt(index))
"""

import fileinput

input = int(fileinput.input()[0])
print(input)