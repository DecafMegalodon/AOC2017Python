#https://adventofcode.com/2017/day/16
import fileinput

dance = fileinput.input().readline().split(',')
dance = [instruction.strip('\n') for instruction in dance]

danceline = [chr(i) for i in range(ord('a'),ord('p')+1)]

def spin(danceline, magnitude):
    workline = danceline + danceline
    return workline[16-magnitude:32-magnitude]
    
def exchange(danceline, targ1, targ2):
    buff = danceline[targ1]
    danceline[targ1] = danceline[targ2]
    danceline[targ2] = buff
    
def partner(danceline, targ1, targ2):
    nTarg1 = danceline.index(targ1)
    nTarg2 = danceline.index(targ2)
    danceline[nTarg1] = targ2
    danceline[nTarg2] = targ1

history = []
# history.append(''.join(danceline))

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
    

for round in range(1000000000):
    for instruction in instructionCache:
        operation = instruction['op']
        t1 = instruction['t1']
        t2 = instruction['t2']
        if(operation == 's'):  # Spin from back
            danceline = spin(danceline,t1)
        elif(operation == 'x'):  # Exchange positions
            danceline[t1], danceline[t2] = danceline[t2], danceline[t1]
        else:  # This only leaves "partner swap", aka p
            partner(danceline, t1, t2)
    stringEquiv = ''.join(danceline)
    if stringEquiv in history:
        index = history.index(stringEquiv)
        period = round-index
        print(history[(1000000000%period)-1])
        break
    else:
        history.append(stringEquiv)