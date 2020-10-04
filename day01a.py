import fileinput

def getDigit(string, pos):
    return int(string[pos % len(string)])

input = fileinput.input()[0][:-1:] #input from AOC will always be on a single line, including a \n

runningSum = 0

for i in range(0, len(input)):
    if(getDigit(input,i) == getDigit(input,i+1)):
        runningSum += getDigit(input,i)
        
print(runningSum)

