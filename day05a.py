import fileinput

memory = [int(instruction) 
            for instruction in fileinput.input() 
            if instruction != "\n"]

pc = 0 #Program counter
steps = 0

while pc < len(memory):
    curMemory = memory[pc]
    memory[pc] += 1
    pc += curMemory
    steps += 1
    
print(steps)