#https://adventofcode.com/2017/day/7
import fileinput

#Input format
#Pgrmname (weight) -> child1, ... , childn
#or
#Pgrmname (weight)

#We -could- find the answer by finding the "program" which isn't referenced as a child to avoid building a tree
#However, we'll probably need the full tree for part B anyway

for line in fileinput.input():
    if line == '\n':
        break
    splitline = line.split()
    name = splitline[0]
    weight = int(splitline[1][1:-1:])
    if(len(splitline) > 3): #If it has children
        subprograms = [subP.strip(",") for subP in splitline[3::]]
    else:
        subprograms = []
    print(name, weight, subprograms)