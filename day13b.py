#https://adventofcode.com/2017/day/13
import fileinput
import copy

firewall = {}
severity = 0
maxdepth = -1
curdepth = -1

#Input: dictionary of: {position, range, direction}. Output: None (Modifies original object)
def advanceSingleFirewallDepth(depth):
    depth['position'] += depth['direction']
    if depth['position'] == depth['range']-1:
        depth['direction'] = -1
    elif depth['position'] == 0:
        depth['direction'] = 1


for line in fileinput.input():
    if line == '\n':
        break
    splitline = line.split()
    depth = int(splitline[0].strip(':'))
    fwobject = {'position': 0, 'range': int(splitline[1]), 'direction': 1}
    
    #Line up the firewall so everything is as it will be on our arrival
    for offset in range(int(depth)):
        advanceSingleFirewallDepth(fwobject)
    firewall[depth] = fwobject
    maxdepth = max(maxdepth, int(depth))


def advanceFirewall(firewall):
    for depth in firewall:
        fwobject = firewall[depth]
        advanceSingleFirewallDepth(fwobject)


def calcSeverity(firewall, maxdepth):
    severity = 0
    for i in range(0,maxdepth+1):
        if i in firewall:
            if firewall[i]["position"] == 0:
                severity += i * firewall[i]["range"]
    return severity


def hasSeverity(firewall):
    for depth in firewall:
        if firewall[depth]["position"] == 0:
            return True

wait = 0
while True:
    #print(calcSeverity(firewall,maxdepth))
    if hasSeverity(firewall):
        advanceFirewall(firewall)
        wait += 1
    else:
        break
print(wait)