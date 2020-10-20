import fileinput
from day10knothash import *

puzInput = fileinput.input().readline()[:-1:]  # Omit the trailing newline

fullDisk = []

for append in range(0,128):
    knothash = calcKnotHash(puzInput + '-' + str(append))
    for bits8 in knothash:
        utilized += sum([bits8&(1<<loc)>0 for loc in range(8)])
    #print(printableHash(knothash))