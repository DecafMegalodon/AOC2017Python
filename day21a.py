#  https://adventofcode.com/2017/day/21
import fileinput


'''
https://stackoverflow.com/questions/8421337/rotating-a-two-dimensional-array-in-python
served as inspiration for this implementation

It takes in a "matrix" and transforms it a few times
E.G. Take the follow matrix:

           \/-Performs a vertical flip
[['..#'] [::-1] ['###'] zip   [#..](As serpate characters)
 ['.#.']  --->  ['.#.'] --->  [##.]
 ['###']        ['..#']  /\   [#.#]
              Mirrors across the x=y axis
              
The vertical flip plus the mirror across the x=y axis is equivalent to a 90 degree rotation
A counterclockwise flip could be achieved by doing the flips in reverse order

Rotates a subimage clockwise (with row major ordering)'''
def rotate(subimg, times=1):
    rotated = subimg
    for i in range(0, times):
        rotated = list(zip(*rotated[::-1]))
    return [''.join(j) for j in rotated]
    

#Returns a shallow-copied vertical flip of the given image
def flipVert(subimg):
    return subimg[::-1]
    
#Returns a slightly less shallow-copied horizonal flip of the given image
def flipHoriz(subimg):
    return [i[::-1] for i in subimg]
    
    
image = ['.#.',
         '..#',
         '###']
     
     
rulesDict = {}

for rule in fileinput.input():
    if rule == '\n':
        break
    splitline = rule.split(" => ")
    rulesDict[splitline[0]] = splitline[1].strip('\n')


for iteration in range(2):
    dim = len(image)
    
    assert dim % 2 == 0 or dim % 3 == 0
    
    divisor = 2 if (dim % 2 == 0) else 3
    
    #  Process the image by chunk
    for width in range(0, dim, divisor):
        for height in range(0, dim, divisor):
            subimage = []
            for subrow in range(divisor):
                subimage.append(image
                        [height+subrow]
                        [width : width + divisor])
            print(subimage)    
        
    