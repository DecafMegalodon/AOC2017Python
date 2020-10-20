import fileinput
from day10knothash import *

puzInput = fileinput.input().readline()[:-1:]  # Omit the trailing newline

fullDisk = [0]*128*128

for append in range(0,128):
    section = 0
    knothash = calcKnotHash(puzInput + '-' + str(append))
    for bits8 in knothash:
        for bit in range(7,-1,-1):
            index = append*128 + section*8 + (7-bit)
            print(index)
            fullDisk[index] = bits8&(1<<bit)>0
            #fullDisk[index] = 1
        section += 1
print("SUM", sum(fullDisk))