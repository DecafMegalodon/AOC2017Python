#https://adventofcode.com/2017/day/15
import fileinput

# Puzzle input format: Generator X starts with NUM
stdin = fileinput.input()
genA = int(stdin.readline().split()[4])
genB = int(stdin.readline().split()[4])

print(genA, genB)