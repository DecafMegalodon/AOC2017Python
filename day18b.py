#  https://adventofcode.com/2017/day/18
import fileinput
        
program = [line.split() for line in fileinput.input()]
pc = 0
lastSound = None

class Program:
    def __init__(self, initProgram, ID):
        self.pc = 0 #program counter
        self.registers = {}
        for regName in range(ord("a"),ord("z")+1):
            self.registers[chr(regName)] = 0
        self.sendQueue = []
        self.numSent = 0

    def readMem(self, target):
        try: #Is target a number?
            return int(target)
        except: #target is not a number
            return self.registers[target]
            
    def writeMem(self, target, value):
        self.registers[target] = self.readMem(registers, value)
        
    def run(self):
        continue

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