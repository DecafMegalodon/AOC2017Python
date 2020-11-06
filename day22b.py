#https://adventofcode.com/2017/day/22
import fileinput

#  Returns a rotated y,x direction vector. Positive direction indicate clockwise rotation
#  Direction should be in the number of 90 degree increments desired
def rotate(curY, curX, direction):
    rotationList = ["-1,0", "0,1", "1,0", "0,-1"] #  Ascending clockwise
    listPos = rotationList.index('%d,%d' % (curY, curX))
    newRotationStrings = rotationList[((listPos + direction) % 4)].split(',')
    return (int(newRotationStrings[0]), int(newRotationStrings[1]))

    
class sparseGrid:
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
            return '.'
        
    def setItem(self, y, x, item):
        keyname = '%d,%d' % (y,x)
        self.matrix[keyname] = item
        
    def __len__(self):
        return len(self.matrix)
        

grid = sparseGrid()
origGridWidth = -1
origGridHeight = 0
infectProg = ".W#F" #Infection progress. Clean, weakened, infected, flagged
#infectRotate = [-1,0,1,2]

for line in fileinput.input():
    origGridHeight += 1
    for charPos in range(len(line)):
        if line[charPos] == '\n':
            continue
        grid.setItem(origGridHeight - 1, charPos, line[charPos])
        
origGridWidth = len(grid) // origGridHeight

curY = origGridWidth // 2
curX = origGridHeight // 2 #  Start in the middle of the original grid
curDirVert = -1
curDirHoriz = 0
numBursts = 0

for iteration in range(10000000):
    curSpot = grid.getItem(curY, curX)
    infectionIndex = infectProg.index(curSpot)
    #Rotate the "carrier"
    #Infected = rotate clockwise, uninfected = ccw
    rotationAmount = infectionIndex - 1
    curDirVert, curDirHoriz = rotate(curDirVert, curDirHoriz, rotationAmount)
    
    #  Flip infection status of current node. 
    numBursts += (curSpot == 'W') #  Uptick the infection counter if it's an weakened node
    grid.setItem(curY, curX, infectProg[(infectionIndex + 1) % 4])
    
    #  Move forward
    curY += curDirVert
    curX += curDirHoriz
    
print(numBursts)
