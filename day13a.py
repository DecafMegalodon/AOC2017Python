#https://adventofcode.com/2017/day/13
import fileinput

firewall = {}
severity = 0

for line in fileinput.input():
    if line == '\n':
        break
    splitline = line.split()
    firewall[splitline[0].strip(':')] = {'position': 0, 'range': int(splitline[1]), 'direction': 'down'}
print(firewall)