#  https://adventofcode.com/2017/day/24
import fileinput

'''Battleplan:
Data classes for connectors and bridges
    Can request iterator for matching unused connectors
    Ideally with otimized lookup
Recursively build all possible bridges and store them for later inspection
Sort the bridges by strength
Reach the CPU over the void!
'''


class bridgeComps:
    
    def __init__(self):
        self._pinLookupDict = {}
        self._pinTable = []
        
    def addConnector(self, pins1, pins2):
        newIndex = len(self._pinTable)
        self._pinTable.append([pins1 + pins2, 0])
        for pin in (pins1, pins2):
            
            try:
                self._pinLookupDict[pin].append(newIndex)
            except:
                self._pinLookupDict[pin] = [newIndex]

    def getMatchingPins(self, hostPins):
        try:
            for match in self._pinLookupDict[hostPins]:
                if self._pinTable[match][1] == 0: #  If it hasn't been used yet
                    self._pinTable[match][1] = 1 #  Mark as used
                    yield self._pinTable[match][0] - hostPins
                    self._pinTable[match][1] = 0 #  Mark as no longer used
        except: #  No pins matching our hostPins
            return




bridgeBits = bridgeComps()
maxBridgeSize = -1
for line in fileinput.input():
    if line == '\n':
        break
    splitLine = line.split('/')
    bridgeBits.addConnector(int(splitLine[0]),int(splitLine[1].strip('\n')))
    
#Finds the strongest buildable bridge with the parts given
def recurseBuildBridge(bridgeParts, curStrength, curConnector):
    maxStren = curStrength
    for match in bridgeParts.getMatchingPins(curConnector):
        maxStren = max(maxStren, curConnector + recurseBuildBridge(bridgeParts, curStrength, match))
    return maxStren + curConnector
    

print(recurseBuildBridge(bridgeBits, 0, 0))
#1554 too low