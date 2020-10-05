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
Distance from the origin depends only on where we are in a particular quadrant for a given ring - not which one we're in.
    Being in index 1 of quadrant 1 is equally far from the origin as index 1 of quadrant 2, 3, and 4
We can find the end of a ring by knowing what ring we're in. (Ring*2-1) ** 2
We can find the start or a ring by adding one to the end of the previous ring (save for ring one, which does not have a previous ring!)
"""

import fileinput
import math

index = int(fileinput.input()[0])

ring = int(((math.sqrt(index-1)+1)//2)+1)
print("Ring: ", ring)

