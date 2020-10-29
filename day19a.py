#  https://adventofcode.com/2017/day/19
import fileinput

def getChar(path, y, x):
    try:
        return path[y][x]
    except:
        return ' '

path = [line for line in fileinput.input()]
alphabet = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
pathLetters = ""
travelChars = "-|"

#  Find the start of the path on the top row
curX = path[0].index("|")
curY = 0
curVelY = 1
curVelX = 0
curTravelChar = "|"
totalTraveled = 0

while True:

    curChar = getChar(path, curY, curX)
    if curChar == ' ': #  We can't leave the path!
        break

    if curChar in alphabet:
        pathLetters += curChar
    
    if curChar == '+': #  If we need to turn
        curTravelChar = '-' if curTravelChar == '|' else '|'
        if curTravelChar == '-': #  Horizontal travel
            curVelY = 0
            if getChar(path, curY,curX + 1) != ' ':
                curVelX = 1
            else:
                curVelX = -1
        else: #Traveling vertically
            curVelX = 0
            if getChar(path, curY + 1, curX) != ' ':
                curVelY = 1
            else:
                curVelY = -1
    curY += curVelY
    curX += curVelX
    totalTraveled += 1
print(pathLetters)
#print(totalTraveled)