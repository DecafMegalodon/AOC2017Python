#  https://adventofcode.com/2017/day/2
import fileinput

rollingChecksum = 0

for line in fileinput.input():
    if(line == "\n"):
        break
    splitNumbers = line.split()
    splitNumbers = [int(''.join(chars)) for chars in splitNumbers]
    rollingChecksum += max(splitNumbers) - min(splitNumbers)

print(rollingChecksum)