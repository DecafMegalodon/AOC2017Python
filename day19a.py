#  https://adventofcode.com/2017/day/19
import fileinput

path = [line for line in fileinput.input()]
alphabet = [chr(i) for i in range(ord('a'), ord('z') + 1)]
pathLetters = ""

#Todo list:

#Build pathfinder
    #Default direction is stright ahead, unless we encounter a +

#  Find the start of the path on the top row
curX = path[0].index("|")
curY = 0
curVelY = 1
curVelX = 0
curTravelChar = "|"
totalTraveled = 0

while True:
    curChar = path[curY][curX]
    if curChar in alphabet:
        pathLetters += curChar
    
    if nextChar == '+': #  If we need to turn
        pass
        
    curY += curVelY
    curX += curVelX
    print(curChar)
print(pathLetters)