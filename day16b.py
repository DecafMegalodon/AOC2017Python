#https://adventofcode.com/2017/day/16
import fileinput

dance = fileinput.input().readline().split(',')
dance = [instruction.strip('\n') for instruction in dance]

danceline = [chr(i) for i in range(ord('a'),ord('p')+1)]

def spin(danceline, magnitude):
    workline = danceline + danceline
    size = len(danceline)
    return workline[size-magnitude:2*size-magnitude]
    
def exchange(danceline, targ1, targ2):
    buff = danceline[targ1]
    danceline[targ1] = danceline[targ2]
    danceline[targ2] = buff
    
def partner(danceline, targ1, targ2):
    nTarg1 = danceline.index(targ1)
    nTarg2 = danceline.index(targ2)
    danceline[nTarg1] = targ2
    danceline[nTarg2] = targ1

instructionCache = []

for instruction in dance:
    operation = instruction[0]
    splitstruction = instruction[1:].split('/')
    t1 = splitstruction[0]
    t2 = splitstruction[1] if operation != 's' else 0
    if operation == 's' or operation == 'x':
        t1 = int(t1)
        t2 = int(t2)
    instructionCache.append({'op': operation, 
                            't1': t1,
                            't2': t2})
    

for round in range(1000):
    for instruction in instructionCache:
        operation = instruction['op']
        t1 = instruction['t1']
        t2 = instruction['t2']
        if(operation == 's'):  # Spin from back
            danceline = spin(danceline,t1)
        elif(operation == 'x'):  # Exchange positions
            exchange(danceline, t1, t2)
        else:  # This only leaves "partner swap", aka p
            partner(danceline, t1, t2)

print(''.join(danceline))