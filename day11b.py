#https://adventofcode.com/2017/day/11
import fileinput
from collections import Counter

"""
Equivalences:
NW+S = SW, SE+N = NE
NE+S = SE, SW+N = NW
SE+SW = S, NE+NW = N
N+S = 0, NE+SW = 0, NW+SE = 0

Observations:
It should be possible to make a two-dimensional coordinate plane with a nw-se (or ne/sw) axis
    and a n/s axis
Combined with the equivalences up above, it may be possible to quickly reduce the counts to distances
"""

path = fileinput.input().readline()[:-1:].split(',') #Trim out newline at the end and split up!
pathCounts = Counter(path)

changed = True


#N+S -> 0, NE+SW -> 0, NW+SE -> 0
dist1 = pathCounts['nw'] - pathCounts['se']
dist2 = pathCounts['ne'] - pathCounts['sw']
dist3 = pathCounts['n'] - pathCounts['s']

if (dist1 * dist3) < 0: #If they're opposite signs and both non-zero. Check for NW/SE + S/N -> SW/NW indentity
    delta = min(abs(dist1),abs(dist3))
    if dist1 > dist3: #NW+S -> SW
        dist2 -= delta
        dist1 -= delta
        dist3 += delta
    else: #SE+N -> NE
        dist2 += delta
        dist1 += delta
        dist3 -= delta

#Copy paste code BAD.        
if dist2 * dist3 < 0: #NE/SW + S/N -> SE/NW
    delta = min(abs(dist2), abs(dist3))
    if dist2 > dist3: #NE + S -> SE
        dist2 -= delta
        dist1 -= delta
        dist3 += delta
    else: #SW+N -> NW
        dist2 += delta
        dist1 += delta
        dist3 -= delta
        
if dist1 * dist2 > 0: #SE+SW = S, NE+NW = N
    delta = min(abs(dist1), abs(dist2))
    if dist1 > 0: #NE+NW = N
        dist2 -= delta
        dist1 -= delta
        dist3 += delta
    else: #SE+SW = S
        dist2 += delta
        dist1 += delta
        dist3 -= delta
    
print(abs(dist1) + abs(dist2) + abs(dist3))

