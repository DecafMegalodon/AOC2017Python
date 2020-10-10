#https://adventofcode.com/2017/day/8
import fileinput

operations = {"<": lambda a, b : a<b,
">": lambda a, b : a>b,
">=": lambda a, b : a>=b,
"<=": lambda a, b : a<=b,
"==": lambda a, b : a==b,
"!=": lambda a, b : a!=b}

memory = {}

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
    targAmount = int(splitLine[2]) #The amount we by which we might increase/decrease the register
    #splitLine 3 will always be "if"
    opReg = splitLine[4] #The register we're inspecting for the conditional opcode
    opCondition = splitLine[5] #< > >= == <= != are all allowed
    opTarget = int(splitLine[6]) #The number against which we'll compare opreg
    
    opRegValue = readMemory(memory, opReg)
    targRegValue = readMemory(memory, targReg)
    #Apparently there's no c-style switch case in python. This looks like a good excuse to learn about lambdas
    opfunc = operations[opCondition] #Convert the text version of <, >, !=, etc to python code
    opTrue = opfunc(opRegValue, opTarget)
    
    if opTrue:
        memory[targReg] = targRegValue + opSign*targAmount
    
print(max([memory[register] for register in memory]))