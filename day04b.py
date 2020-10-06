#Advent of code day 04b
import fileinput

validPasswords = 0

for line in fileinput.input():
    if(line == "\n"):
        break
    splitWords = line.split()
    if len(splitWords) == len(set(splitWords)):
        validPasswords += 1
        
print(validPasswords)