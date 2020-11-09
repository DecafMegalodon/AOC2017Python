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
        self._pinTable.append((pins1, pins2, 0))
        for pin in (pins1, pins2):
            
            try:
                self._pinLookupDict[pin].append(newIndex)
            except:
                self._pinLookupDict[pin] = [newIndex]

bridgeBits = bridgeComps()
bridgeBits.addConnector(1,4)
bridgeBits.addConnector(1,5)
print(bridgeBits._pinTable)
print(bridgeBits._pinLookupDict)