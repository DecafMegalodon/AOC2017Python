#  https://adventofcode.com/2017/day/25
import fileinput

class TuringTape():
    def __init__(self):
        self.tape = {}
    
    def read(self, pos):
        try:
            return self.tape[pos]
        except:
            return 0
            
    def write(self, pos, value):
        self.tape[pos] = value
        
    def count(self, value):
        occurances = 0
        for key in self.tape:
            occurances += (self.tape[key] == value)
        return occurances

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
tape = TuringTape()
curState = startState
tapePos = 0

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

for step in range(numSteps):
    stateInstruct = stateTable[(curState, tape.read(tapePos))]
    tape.write(tapePos, stateInstruct['writeValue'])
    tapePos += stateInstruct['moveDirection']
    curState = stateInstruct['nextState']
    
print(tape.count(1))