#  https://adventofcode.com/2017/day/19
import fileinput

path = [line for line in fileinput.input()]
alphabet = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
pathLetters = ""
travelChars = "-|"

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
    try:
        curChar = path[curY][curX]
    except:
        break
    assert curChar != ' '
    if curChar in alphabet:
        pathLetters += curChar
    
    if curChar == '+': #  If we need to turn
        curTravelChar = '-' if curTravelChar == '|' else '|'
        if path[curY+curVelX][curX+curVelY] == curTravelChar:
            curVelY, curVelX = -1 * curVelX, -1 * curVelY
        else:
            curVelY, curVelX = curVelX, curVelY
    curY += curVelY
    curX += curVelX
    print(curChar)
print(pathLetters)