# https://adventofcode.com/2017/day/3
"""
Dev plan:
Study the problem:
    Our spiral described in OEIS as sequence A141481
    Expands in all four cardinal directions
Write spiral number generator
Search for the answer
"""
import fileinput
import math

class expandGrid:
    def __init__(self):
        self.grid = {}
        
    def read(self, y, x):
        try:
            return self.grid[(y, x)]
        except:
            return 0
            
    def sumNeighbors(self, y, x):
        sum = 0
        for yval in range(y-1, y+2): #  Range is not inclusive of last number
            for xval in range(x-1, y+2):
                sum += self.grid[(y,x)]
        return sum
        
    def countNeighbors(self, y, x):
        neighbors = 0
        for yval in range(y-1, y+2): #  Range is not inclusive of last number
            for xval in range(x-1, y+2):
                sum += self.grid[(y,x)]
        
    def write(self, y, x, value):
        self.grid[(y,x)] = value
        
    def __str__(self):
        return str(self.grid)
        
#  Returns a rotated y,x direction vector. Positive direction indicate clockwise rotation
#  Direction should be in the number of 90 degree increments desired
def rotate(curY, curX, direction):
    rotationList = ["-1,0", "0,1", "1,0", "0,-1"] #  Ascending clockwise
    listPos = rotationList.index('%d,%d' % (curY, curX))
    newRotationStrings = rotationList[((listPos + direction) % 4)].split(',')
    return (int(newRotationStrings[0]), int(newRotationStrings[1]))
        
grid = expandGrid()
grid.write(0,0,1)
lastValue = 1
curY = 0
curX = 0
curIndex = 1
moveY = 0
moveX = 1
puzInput = int(fileinput.input().readline().strip('\n'))

while lastValue < puzInput:
    lastValue = grid.sumNeighbors(curY, curX)
    grid.write(curY, curX, lastValue)
    curY += moveY
    curX += moveX
    #  update current rotation
    
    
