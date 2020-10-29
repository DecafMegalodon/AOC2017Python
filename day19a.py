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
    nextChar = path[curY+curVelY][curX+curVelX]
    if nextChar in alphabet:
        pathLetters += nextChar
    
    if nextChar != '+': #  If we don't need to turn yet
        curY += curVelY
        curX += curVelX
        
    if nextChar == ' ':
        break
    print(nextChar)
print(pathLetters)