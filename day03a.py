"""Observations:
Addresses are 1-indexed
A new "ring" starts on n^2 + 1 indices
New "Rings" start near - but not on a corner. 1 away.
We can find the ring number as so: ((math.sqrt(index-1)+1)//2)+1
Ring diameter can be found by ring number*2-1
We can break the current ring into four "quadrants" like so
22221
3$$$1
3$$$1
3$$$1
34444

"""

import fileinput
import math

index = int(fileinput.input()[0])

ring = int(((math.sqrt(index-1)+1)//2)+1)
print(ring)
