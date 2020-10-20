import fileinput
from day10knothash import *

BITSINHASH = 128
fullDisk = [0]*128*128
puzInput = fileinput.input().readline()[:-1:]  # Omit the trailing newline


def getDiskOccupation(disk, y, x):
    if x > 127 or y > 127 or x < 0 or y < 0:
        return 0
    else:
        return disk[y*128 + x]
        
def setDiskOccuptation(disk, y, x, occupied):
    if x > 127 or y > 127 or x < 0 or y < 0:
        raise "NotOnDiskError y%d x%d" % (y, x)
    else:
        disk[y*128 + x] = occupied
        
"""Destructively finds the area of a contiguous block of data"""
def recurseAreaFind(disk, y, x):
    if getDiskOccupation(disk, y, x) == 0:
        return 0

    area = 1
    setDiskOccuptation(disk, y, x, 0)
    for yoff in [-1, 1]:
        for xoff in [-1, 1]:
            area += recurseAreaFind(disk, y+yoff, x+xoff)

    return area

#Build disk bitmap
for append in range(0,128):
    section = 0
    knothash = calcKnotHash(puzInput + '-' + str(append))
    for bits8 in knothash:
        for bit in range(7,-1,-1):
            thisBit = bits8&(1<<bit)>0  # True == 1
            setDiskOccuptation(fullDisk,append,section*8 + 7 - bit, thisBit)
        section += 1


numRegions = 0

for y in range(0,128):
    for x in range(0,128):
        if recurseAreaFind(fullDisk, y, x) > 0:
            numRegions += 1
            
print(numRegions)
#print(fullDisk)