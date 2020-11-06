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
        

test = sparseMatrix()
test.setItem(0,0,'a')
assert test.numOf('a') == 1
print(test.getItem(0,0))