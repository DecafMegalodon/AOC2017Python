import fileinput

history = []
numOps = 0;

indata = fileinput.input().readline()
banks = [int(num) 
            for num in indata.split()
            ]
            
while banks not in history:
    history.append(banks.copy())
    numOps += 1
    curIndex = banks.index(max(banks)) #find the >lowest-indexed< maximum value
    curBlocks = banks[curIndex]
    banks[curIndex] = 0
    while curBlocks > 0:
        curIndex += 1
        curIndex %= len(banks)
        banks[curIndex] += 1
        curBlocks -= 1
    #print (banks)
    #print (history)
    
print (numOps)