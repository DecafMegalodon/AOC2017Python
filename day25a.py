#  https://adventofcode.com/2017/day/25
import fileinput

'''Reduce the input stream only what matters (tm).
Does not perform integer conversion
EX:
In state A:
  If the current value is 0:
    - Write the value 1.
    - Move one slot to the right.
    - Continue with state B.
  If the current value is 1:
    - Write the value 0.
    - Move one slot to the left.
    - Continue with state B.

In state B:
...
\/
iterator containing: A 0 1 right B 1 0 left B B ...
'''
def filterInput(inputOb):
    for line in inputOb:
        if line == '\n':
            continue
        yield line.split()[-1].strip('.:\n')

puzInput = fileinput.input()
startState = puzInput.readline().split()[3].strip(".\n") #  Begin in state ?.
numSteps = int(puzInput.readline().split()[5]) #  Perform a diagnostic checksum after ? steps.
stateTable = {}

filteredInput = list(filterInput(puzInput))
puzInput.close()

for bIndx in range(0, len(filteredInput), 9):
    instate = filteredInput[bIndx]    
    for offset in (1+bIndx, 5+bIndx):
        curVal = int(filteredInput[offset])
        writeVal = int(filteredInput[offset + 1])
        moveDir = filteredInput[offset + 2]
        jumpState = filteredInput[offset + 3]
        stateTable[(instate, curVal)] = {'writeValue': writeVal, 
                                         'moveDirection': 1 if moveDir == 'right' else -1,
                                         'nextState': jumpState}

print(stateTable)