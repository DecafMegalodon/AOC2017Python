#https://adventofcode.com/2017/day/11
import fileinput
from collections import Counter

"""
Equivalences:
NW+S = SW, SW+N = NW
NE+S = SE, SE+N = NE
SE+SW = S, NE+NW = N
N+S = 0, NE+SW = 0, NW+SE = 0

Observations:
It should be possible to make a two-dimensional coordinate plane with a nw-se (or ne/sw) axis
    and a n/s axis
Combined with the equivalences up above, it may be possible to quickly reduce the counts to distances
"""
path = fileinput.input().readline()[:-1:].split(',') #Trim out newline at the end and split up!
pathCounts = Counter(path)
dist1 = pathCounts['nw'] - pathCounts['se']
dist2 = pathCounts['ne'] - pathCounts['sw']
dist3 = pathCounts['n'] - pathCounts['s']
equivPath = {'nw': dist1 if dist1 > 0 else 0,
    'se': abs(dist1), 
    'n': 0, 
    's': 0, 
    'ne':0, 
    'sw':0}
if(dist1 > 0):
    equivPath['nw'] = dist1
else:
    equivPath['se'] = abs(dist1)
print(dist1, dist2, dist3)
print(dist1 + dist2 + dist3)

