#https://adventofcode.com/2017/day/7
import fileinput
import collections

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
        
    progData = {"name" : name, "childNames": subprograms, "childData": [], "weight": weight, "baseWeight": weight}
    unmatchedProgs.append(progData)
    
    for child in subprograms:
        parentLookupTable[child] = progData
    
#Build the tree
while(len(unmatchedProgs) > 1):
    for prog in unmatchedProgs:
        if len(prog["childNames"]) != len(prog["childData"]):
            continue #Don't find parents for parents who haven't found all their children yet
        #All of this program's children (if any) are accounted for. We can find its parents now!
        #But first, are our children (if any) "balanced"? Defined as all being the same
        if(len(prog["childData"]) > 0):
            weights = [child["weight"] for child in prog["childData"]]
            weightSet = set(weights)
            if(len(set(weights)) > 1): #Children NOT balanced. We need to find the one that's different
                leastCommon = collections.Counter(weights).most_common()[-1][0] #The weight of our errant program, including children if any
                mostCommon = collections.Counter(weights).most_common()[0][0]
                badWeightIndex = weights.index(leastCommon)
                print(prog["childData"][badWeightIndex]["baseWeight"] - (leastCommon-mostCommon))
                #print(weights)
                exit()
            
        parentData = parentLookupTable[prog["name"]]
        parentData["childData"].append(prog)
        parentData["weight"] += prog["weight"]
        unmatchedProgs.remove(prog)

#print(unmatchedProgs[0]["name"])