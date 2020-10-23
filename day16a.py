#https://adventofcode.com/2017/day/16
import fileinput

dance = fileinput.input().readline().split(',')
dance = [instruction.strip('\n') for instruction in dance]

danceline = [chr(i) for i in range(ord('a'),ord('p')+1)]
print(danceline)

def spin(danceline, magnitude):
    workline = danceline + danceline
    size = len(danceline)
    return workline[size-magnitude:2*size-magnitude]
    
def exchange(danceline, targ1, targ2):
    newDance = [i for i in danceline]
    buff = danceline[targ1]
    newDance[targ1] = danceline[targ2]
    newDance[targ2] = buff
    return newDance
    
def partner(danceline, targ1, targ2):
    newDance = [i for i in danceline]
    nTarg1 = danceline.index(targ1)
    nTarg2 = danceline.index(targ2)
    newDance[nTarg1] = targ2
    newDance[nTarg2] = targ1
    return newDance

for instruction in dance:
    operation = instruction[0]
    splitstruction = instruction[1:].split('/')
    print(instruction, splitstruction)
    if(operation == 's'):  # Spin from back
        danceline = spin(danceline,int(splitstruction[0]))
    elif(operation == 'x'):  # Exchange positions
        danceline = exchange(danceline, int(splitstruction[0]), int(splitstruction[1]))
    else:  # This only leaves "partner swap", aka p
        danceline = partner(danceline, splitstruction[0], splitstruction[1])
    print(danceline)
    danceCopy = [i for i in danceline]
    danceCopy.sort()
    assert danceCopy == [chr(i) for i in range(ord('a'),ord('p')+1)]
print(''.join(danceline))