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

def advanceFirewall(firewall):
    for depth in firewall:
        fwobject = firewall[depth]
        fwobject['position'] += fwobject['direction']
        if fwobject['position'] == fwobject['range']-1:
            fwobject['direction'] = -1
        elif fwobject['position'] == 0:
            fwobject['direction'] = 1

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