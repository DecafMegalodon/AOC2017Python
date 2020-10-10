#https://adventofcode.com/2017/day/8
import fileinput

memory = {}
maxreg = 0 #The highest value a register has achieved so far

def readMemory(memory, register):
    if register in memory:
        return memory[register]
    else:
        return 0 #Undefined registered are implied to be 0

for line in fileinput.input():
    if line == '\n':
        break
    splitLine = line.split()
    targReg = splitLine[0] #The register we -might- modify
    opSign = 1 if splitLine[1] == 'inc' else -1 #Values may only be inc or dec
    targAmount = splitLine[2] #The amount we by which we might increase/decrease the register
    opReg = splitLine[4] #The register we're inspecting for the conditional opcode
    opCondition = splitLine[5] #< > >= == <= != are all allowed
    opTarget = splitLine[6] #The number against which we'll compare opreg
    
    
    
    
    print (splitLine)