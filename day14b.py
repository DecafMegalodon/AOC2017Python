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
        return disk[y*128 + x] = occupied

for append in range(0,128):
    section = 0
    knothash = calcKnotHash(puzInput + '-' + str(append))
    for bits8 in knothash:
        for bit in range(7,-1,-1):
            thisBit = bits8&(1<<bit)>0
            setDiskOccuptation(disk,append,section*8 + 7 - bit, thisBit)
        section += 1
print("SUM", sum(fullDisk))