#https://adventofcode.com/2017/day/22
import fileinput

class sparseMatrix:
    def __init__(self):
        self.matrix = dict()
    
    def numOf(self, target):
        num = 0
        for key in self.matrix:
            num += (self.matrix[key] == target)
        return num
        
    def getItem(self, y, x):
        keyname = '%d,%d' % (y,x)
        try:
            return self.matrix[keyname]
        except KeyError:
            return 0
        
    def setItem(self, y, x, item):
        keyname = '%d,%d' % (y,x)
        self.matrix[keyname] = item
        
    def __len__(self):
        return len(self.matrix)
        

grid = sparseMatrix()
origGridWidth = -1
origGridHeight = 0

for line in fileinput.input():
    origGridHeight += 1
    for charPos in range(len(line)):
        if line[charPos] == '\n':
            continue
        grid.setItem(origGridHeight - 1, charPos, line[charPos])
        
origGridWidth = len(grid) // origGridHeight

curY = origGridWidth // 2
curX = origGridHeight // 2 #  Start in the middle of the original grid

print(curY, curX)
