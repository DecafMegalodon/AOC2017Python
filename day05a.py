import fileinput

memory = []

for instruction in fileinput.input():
    if(instruction == "\n"):
        break
    memory.append(int(instruction))
    
print (memory)