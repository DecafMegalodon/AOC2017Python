#  https://adventofcode.com/2017/day/18
import fileinput

registers = {}
for regName in range(ord("a"),ord("z")+1):
    registers[chr(regName)] = 0

def readMem(memory, target):
    try: #Is target a number?
        return int(target)
    except: #target is not a number
        return memory[target]
        
def writeMem(memory, target, value):
    memory[target] = readMem(memory, value)
        
program = [line.split() for line in fileinput.input]
pc = 0
lastSound = None

while True:
    instruction = program[pc]
    op = instruction[0]
    v1 = instruction[1]
    v2 = instruction[2] if len(instruction) > 2 else None
        
    if op == 'snd':
        continue
    elif op == 'set':
        continue
    elif op == 'add':
        continue
    elif op == 'mul':
        continue
    elif op == 'mod':
        continue
    elif op == 'rcv':
        continue
    elif op == 'jgz':
        continue
    
    