#  https://adventofcode.com/2017/day/18
import fileinput

registers = {}
for regName in range(ord("a"),ord("z")+1):
    registers[chr(regName)] = 0

for instruction in fileinput.input():
    splitline = instruction.split()
    op = splitline[0]
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
    
    