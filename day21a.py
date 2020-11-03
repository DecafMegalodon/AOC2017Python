#  https://adventofcode.com/2017/day/21
import fileinput
import math


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
    
#Takes a subimage and flips it horizonally or vertically as needed
#Flipdescriptor format: 0bXY
#X = hoirzontal flip, Y = vertical flip
def processFlip(subimage, flipDescriptor):
    horizFlip = flipDescriptor % 2
    vertFlip = flipDescriptor - horizFlip
    newImage = subimage
    if horizFlip:
        newImage = flipHoriz(newImage)
    if vertFlip:
        newImage = flipVert(newImage)
    return newImage
    
#  Image MUST be built left to right
def imprintImage(image, rule, startY):
    print(image,rule,startY)
    for y in range(len(rule)):
        image[startY + y] += rule[y]
    print("built image:", image)
    
image = ['.#.',
         '..#',
         '###']
     
rulesDict = {}

for rule in fileinput.input():
    if rule == '\n':
        break
    splitline = rule.split(" => ")
    rulesDict[splitline[0]] = splitline[1].strip('\n')


for iteration in range(5):
    dim = len(image)
    
    assert dim % 2 == 0 or dim % 3 == 0
    
    divisor = 2 if (dim % 2 == 0) else 3
    newChunkSize = 3 if divisor == 2 else 4

    provisionalImage = [''] * (dim // divisor * newChunkSize)
    print("Blank image:", provisionalImage)
    
    #  Process the image by chunk
    for width in range(0, dim, divisor):
        for height in range(0, dim, divisor):
            subimage = []
            
            #  Fetch subimage
            for subrow in range(divisor):
                subimage.append(image
                        [height+subrow]
                        [width : width + divisor])
                        
            rotation = 0
            flips = 0 #See processFlip for documentation
            foundRule = False

            
            while not foundRule:
                if flips == 4: #We've tried all combinations for flips for this rotation
                    rotation += 1
                    flips = 0
                assert rotation != 4 #  This indicates a failed search for a rule
                
                newImage = rotate(subimage, rotation)
                newImage = processFlip(newImage, flips)
                print(newImage)
                if '/'.join(newImage) in rulesDict:
                    print("FOUND RULE!", height, width)
                    replacement = rulesDict['/'.join(newImage)]
                    print("Replacement:", replacement)
                    imprintImage(provisionalImage,
                                    replacement.split('/'),
                                    height // divisor * newChunkSize)
                    foundRule = True
                else:    
                    flips += 1
                    
    image = provisionalImage

onSum = 0

for row in image:
    onSum += row.count('#')
print(onSum)