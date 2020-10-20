#https://adventofcode.com/2017/day/10
import fileinput

"""
Our input is a list of lengths
Our "state" is 256 elements long, circular, and 0 indexed
Lengths larger than the size of the list are invalid.


Reverse the order of that length of elements in the list
    starting with the element at the current position.
Move the current position forward by that length plus the skip size.
Increase the skip size by one.
"""


#Reverses a subrange of a list given a start and length, wrapping around if needed.
def reverseSpan(rope, start, length):
    #Technically, we're working with "string" not a "rope",
        #but rope was chosen as  name here for clarity
    workRope = rope+rope
    modRope = workRope[start:start+length][::-1]
    
    for i in range(0,length):
        workRope[(start+i)%len(rope)] = modRope[i]
    workRope = workRope[0:len(rope)]
    
    return workRope
    
"""Returns the hexadecimal equivalent in string form of the binary hash"""
def printableHash(denseHash):
    fullHash = ""
    for eightbits in denseHash:
        partHash = hex(eightbits)
        partHash = partHash[2::] #Trim off the 0x
        if(len(partHash) == 1):
            partHash = '0' + partHash
        fullHash += partHash
    return(fullHash)


"""Takes a string input and returns it back as a knothash in a list, 8 bits at a time"""
def calcKnotHash(datastring):
    rope = [i for i in range(0,256)]
    denseHash = []
    curPos = 0
    skip = 0
    
    data = [ord(char) for char in datastring]
    data += [17,31,73,47,23]
    
    for round in range(0,64):
        for length in data:
            rope = reverseSpan(rope, curPos, length)
            curPos += length
            curPos += skip
            curPos %= len(rope)
            skip += 1
            
    for block in range(0,16):
        blockData = rope[block*16]
        for subblock in range(1,16):
            blockData = blockData ^ rope[block*16+subblock]
        denseHash.append(blockData)
    
    return denseHash


indata = fileinput.input().readline()[:-1:] #Omit the trailing newline python adds
knothash = calcKnotHash(indata)
print(printableHash(knothash))