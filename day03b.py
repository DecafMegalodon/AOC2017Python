"""
Dev plan:
Study the problem:
    Our spiral described in OEIS as sequence A141481
    Expands in all four cardinal directions
Write spiral number generator
Search for the answer
"""
import fileinput

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
                sum += self.read(yval, xval)
        return sum
        
    def write(self, y, x, value):
        self.grid[(y,x)] = value
        
    def __str__(self):
        return str(self.grid)
        
grid = expandGrid()
grid.write(0,0,1)
grid.write(1,1,2)
grid.write(2,2,1000000000)
print(grid.sumNeighbors(0,0))
