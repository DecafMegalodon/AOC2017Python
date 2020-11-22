#https://adventofcode.com/2017/day/13
import fileinput
import copy

firewall = {}
severity = 0
maxdepth = -1
curdepth = -1

#Input: dictionary of: {position, range}. Output: None (Modifies original object)
def advanceSingleFirewallDepth(depth):
    depth['position'] = (depth['position'] + 1) % depth['range']


for line in fileinput.input():
    if line == '\n':
        break
    splitline = line.split()
    depth = int(splitline[0].strip(':'))
    fwCycleTime = int(splitline[1])
    fwCycleTime = (fwCycleTime - 1) * 2
    fwobject = {'position': 0, 'range': fwCycleTime}
    
    #Line up the firewall so everything is as it will be on our arrival
    for offset in range(int(depth)):
        advanceSingleFirewallDepth(fwobject)
    firewall[depth] = fwobject
    maxdepth = max(maxdepth, int(depth))


def advanceFirewall(firewall):
    for depth in firewall:
        fwobject = firewall[depth]
        advanceSingleFirewallDepth(fwobject)


def hasSeverity(firewall):
    for depth in firewall:
        if firewall[depth]["position"] == 0:
            return True

wait = 0
while True:
    if hasSeverity(firewall):
        advanceFirewall(firewall)
        wait += 1
    else:
        break
print(wait)