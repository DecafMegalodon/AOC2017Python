#https://adventofcode.com/2017/day/7
import fileinput

#Input format
#Pgrmname (weight) -> child1, ... , childn
#or
#Pgrmname (weight)

#We -could- find the answer by finding the "program" which isn't referenced as a child to avoid building a tree
#However, we'll probably need the full tree for part B anyway

unmatchedProgs = [] #Programs for which we haven't yet found their parents
parentLookupTable = {} #child name -> parent

#Extract important bits from the puzzle input
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
        
    progData = {"name" : name, "childNames": subprograms, "childData": []}
    unmatchedProgs.append(progData)
    
    for child in subprograms:
        parentLookupTable[child] = progData
    
#Build the tree
while(len(unmatchedProgs) > 1):
    for prog in unmatchedProgs:
        if len(prog["childNames"]) != len(prog["childData"]):
            ##print("Bonk")
            continue #Don't find parents for parents who haven't found all their children yet
        #All of this program's children (if any) are accounted for. We can find its parents now!
        parentData = parentLookupTable[prog["name"]]
        parentData["childData"].append(prog)
        unmatchedProgs.remove(prog)
        
print(unmatchedProgs[0]["name"])