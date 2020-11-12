#  https://adventofcode.com/2017/day/25
import fileinput

'''Input format
Begin in state A.
Perform a diagnostic checksum after 6 steps.

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
'''

puzInput = fileinput.input()
startState = puzInput.readline().split()[3].strip(".\n") #  Begin in state ?.
numSteps = int(puzInput.readline().split()[5])

print(startState, numSteps)