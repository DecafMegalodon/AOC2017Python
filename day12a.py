#https://adventofcode.com/2017/day/12
import fileinput

network = {'0'} #0 is implicitly connected to itself
unconnecteds = {} #Nodes we haven't yet determined if they're connected to 0 or not

for line in fileinput.input():
    if line == '\n':
        break
    splitline = line.split()
    children = [address.strip(",") for address in splitline[2::]]
    unconnecteds[splitline[0]] = children
    
changed = True

while changed:
    changed = False
    for con in unconnecteds:
        if con in network:
            changed = True
            network.update(unconnecteds[con])
            del unconnecteds[con]
            break
print(len(network))