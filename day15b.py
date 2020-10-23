#https://adventofcode.com/2017/day/15
import fileinput

# Puzzle input format: Generator X starts with NUM
stdin = fileinput.input()
genA = int(stdin.readline().split()[4])
genB = int(stdin.readline().split()[4])
genAFactor = 16807
genBFactor = 48271  # Both of these are provided by the puzzle outside of input

agreement = 0

for round in range(5000000):
    while True:
        genA = (genA*genAFactor) % 2147483647
        if genA % 4 == 0:
            break

    while True:        
        genB = (genB*genBFactor) % 2147483647
        if genB % 8 == 0:
            break

    if genA % 65536 == genB % 65536:
        agreement += 1
        
print(agreement)