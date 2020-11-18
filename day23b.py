#  https://adventofcode.com/2017/day/23
#  More info on my decompilation efforts can be found
#  in day23bseudocode and day23input.txt
import math

def isComposite(integer):
    for i in range(2, int(math.sqrt(integer))):
        if integer % i == 0:
            return 1
    return 0
    
nonPrimes = 0
for i in range(105700, 122700+1, 17):
    nonPrimes += isComposite(i)
print(nonPrimes)