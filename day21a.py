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

Rotates a subimage clockwise (with row major ordering)'''
def rotate(subimg, times=1):
    rotated = subimg
    for i in range(times):
        rotated = list(zip(*subimg[::-1]))
    return [''.join(j) for j in rotated]
    

test = ['###','...','...']
for i in range(4):
    test = rotate(test)
    print(test, '\n')