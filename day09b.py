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
        if char == '>': #Garbage over
            isGarbage = False
        continue
    if char == '<':
        isGarbage = True
        continue
    if char == '{':
        depth += 1
    if char == '}':
        score += depth
        depth -= 1
    assert depth >= 0
print(score)
