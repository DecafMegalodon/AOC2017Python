#  https://adventofcode.com/2017/day/1
import fileinput


#  Return the integer representation of the pos-th digit,
#  wrapping around to the start on an overflow
def getDigit(string, pos):
    return int(string[pos % len(string)])

#  input from AOC day 1 will always be on a single line, including a \n
puzInput = fileinput.input().readline().strip()

runningSum = 0
halfLength = len(puzInput) // 2

for i in range(0, len(puzInput)):
    if(getDigit(puzInput, i) == getDigit(puzInput, i + halfLength)):
        runningSum += getDigit(puzInput, i)

print(runningSum)
