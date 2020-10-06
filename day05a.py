import fileinput

memory = [int(instruction) 
            for instruction in fileinput.input() 
            if instruction != "\n"]

print (memory)