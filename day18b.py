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
        self.registers['p'] = ID
        self.sendQueue = []
        self.numSent = 0
        self.program = initProgram

    def readMem(self, target):
        #print("Trying to read: ", target)
        try: #Is target a number?
            return int(target)
        except: #target is not a number
            return self.registers[target]
            
    def writeMem(self, target, value):
        self.registers[target] = self.readMem(value)
        
    '''Runs the program in memory until it halts for some reason
       Returns the number of instructions run for this invocation of run
    '''
    def run(self, otherComputer):
        numInstructionsRunThisWake = 0
        
        while True:
        
            if self.pc >= len(self.program): #Reached the end of prog
                return numInstructionsRunThisWake
            instruction = self.program[self.pc]
            op = instruction[0]
            v1 = instruction[1]
            v2 = instruction[2] if len(instruction) > 2 else None
            
            print(self.registers['p'], instruction)
            
            if op == 'snd':
                    self.sendQueue.append(self.readMem(v1))
                    self.numSent += 1
            elif op == 'set':
                self.writeMem(v1, v2)
            elif op == 'add':
                self.writeMem(v1, 
                    self.readMem(v1) + self.readMem(v2))
            elif op == 'mul':
                self.writeMem(v1, 
                    self.readMem(v1) * self.readMem(v2))
            elif op == 'mod':
                self.writeMem(v1, 
                    self.readMem(v1) % self.readMem(v2))
            elif op == 'rcv':
                if len(otherComputer.sendQueue) == 0:
                    return numInstructionsRunThisWake
                else:
                    self.writeMem(v1, otherComputer.sendQueue.pop(0))
            elif op == 'jgz':
                if self.readMem(v1) > 0:
                    self.pc += self.readMem(v2)
                    numInstructionsRunThisWake += 1
                    continue #  Skip the PC increase
            self.pc += 1
            numInstructionsRunThisWake += 1


prog1 = Program(program, 0)
prog2 = Program(program, 1)

#  While at least one instruction is executed between the two:
while(prog1.run(prog2) + prog2.run(prog1) > 0):
    continue

print(prog1.numSent)
#6096 too high