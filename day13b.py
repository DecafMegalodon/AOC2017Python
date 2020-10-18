#https://adventofcode.com/2017/day/13
import fileinput
import copy

firewall = {}
severity = 0
maxdepth = -1
curdepth = -1

for line in fileinput.input():
    if line == '\n':
        break
    splitline = line.split()
    firewall[splitline[0].strip(':')] = {'position': 0, 'range': int(splitline[1]), 'direction': 1}
    maxdepth = max(maxdepth, int(splitline[0].strip(':')))
    
    
#Input: dictionary of: {position, range, direction}. Output: None (Modifies original object)
def advanceSingleFirewallDepth(depth):
    depth['position'] += depth['direction']
    if depth['position'] == depth['range']-1:
        depth['direction'] = -1
    elif depth['position'] == 0:
        depth['direction'] = 1

def advanceFirewall(firewall):
    for depth in firewall:
        fwobject = firewall[depth]
        advanceSingleFirewallDepth(fwobject)
def calcSeverity(OGFirewall, maxdepth):
    firewall = copy.deepcopy(OGFirewall)
    severity = 0
    for i in range(0,maxdepth+1):
        if str(i) in firewall:
            if firewall[str(i)]["position"] == 0:
                #print("Caught at", i)
                severity += i * firewall[str(i)]["range"]
        advanceFirewall(firewall)
    return severity
    
print(calcSeverity(firewall,maxdepth))