#https://adventofcode.com/2017/day/12
import fileinput

unconnecteds = {} #Nodes we haven't yet determined if they're connected to 0 or not

for line in fileinput.input():
    if line == '\n':
        break
    splitline = line.split()
    children = [address.strip(",") for address in splitline[2::]]
    unconnecteds[splitline[0]] = children
    
numNetworks = 0

while len(unconnecteds) > 0:
    numNetworks += 1
    node = unconnecteds.popitem() #Fetch an item... any item.
    network = {node[0]} #And we'll see what connects to it
    network.update(node[1])
    
    changed = True
    while changed:
        changed = False
        for con in unconnecteds:
            if con in network:
                changed = True
                network.update(unconnecteds[con]) #Add the children to the reachable list
                del unconnecteds[con]
                break
print(numNetworks)