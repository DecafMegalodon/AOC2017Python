#  https://adventofcode.com/2017/day/18
import fileinput

registers = {}
for regName in range(ord("a"),ord("z")+1):
    registers[chr(regName)] = 0

def readMem(registers, target):
    try: #Is target a number?
        return int(target)
    except: #target is not a number
        return registers[target]
        
def writeMem(registers, target, value):
    registers[target] = readMem(registers, value)
        
program = [line.split() for line in fileinput.input()]
pc = 0
lastSound = None

while True:
    instruction = program[pc]
    op = instruction[0]
    v1 = instruction[1]
    v2 = instruction[2] if len(instruction) > 2 else None

    #print(instruction)
    if op == 'snd':
        lastSound = readMem(registers, v1)
    elif op == 'set':
        writeMem(registers, v1, v2)
    elif op == 'add':
        writeMem(registers, v1, 
            readMem(registers, v1) + readMem(registers, v2))
    elif op == 'mul':
        writeMem(registers, v1, 
            readMem(registers, v1) * readMem(registers, v2))
    elif op == 'mod':
        writeMem(registers, v1, 
            readMem(registers, v1) % readMem(registers, v2))
    elif op == 'rcv':
        if readMem(registers, v1) != 0:
            print(lastSound)
            exit(0)
    elif op == 'jgz':
        if readMem(registers, v1) > 0:
            pc += readMem(registers, v2)
            continue #  Skip the PC increase
    
    pc += 1