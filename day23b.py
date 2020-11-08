#  https://adventofcode.com/2017/day/18
import fileinput
        
program = [line.split() for line in fileinput.input()]

class Program:
    def __init__(self, initProgram, ID):
        self.pc = 0 #program counter
        self.registers = {}
        for regName in range(ord("a"),ord("h")+1):
            self.registers[chr(regName)] = 0
        self.registers['a'] = 1
        self.program = initProgram #  Shallow copied

    def readMem(self, target):
        try: #Is target a number?
            return int(target)
        except: #target is not a number
            return self.registers[target]
            
    def writeMem(self, target, value):
        self.registers[target] = self.readMem(value)
        
    '''Runs the program in memory until it halts for some reason
       Returns the number of instructions run for this invocation of run
    '''
    def run(self):
        progLen = len(self.program)
        while True:
        
            if self.pc >= progLen: #  Reached the end of prog
                return
            instruction = self.program[self.pc]
            op = instruction[0]
            v1 = instruction[1]
            v2 = instruction[2]
            if op == 'set':
                self.writeMem(v1, v2)
            elif op == 'sub':
                self.writeMem(v1, 
                    self.readMem(v1) - self.readMem(v2))
            elif op == 'mul':
                self.writeMem(v1, 
                    self.readMem(v1) * self.readMem(v2))
            elif op == 'jnz':
                if self.readMem(v1) != 0:
                    self.pc += self.readMem(v2)
                    continue #  Skip the PC increase
            elif op == 'jez':  #Jump if equal to zero
                if self.readMem(v1) == 0:
                    self.pc += self.readMem(v2)
                    continue #  Skip the PC increase
            self.pc += 1


prog0 = Program(program, 0)
prog0.run()

print(prog0.registers['h'])