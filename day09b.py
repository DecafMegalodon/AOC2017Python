#https://adventofcode.com/2017/day/9
import fileinput

streamData = fileinput.input().readline()
skipping = False
isGarbage = False
depth = 0
score = 0

for char in streamData:
    if char == '\n':
        break
    if skipping:
        skipping = False
        continue
    if isGarbage:
        if char == '!':
            skipping = True
            continue
        if char == '>': #Garbage over
            isGarbage = False
            continue
        score += 1
        continue
    if char == '<':
        isGarbage = True
        continue
print(score)
