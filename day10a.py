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

#Technically, we're working with "string" not a "rope",
#but rope was chosen as  name here for clarity
def reverseSpan(rope, start, length):
    workSpan = rope+rope
    print(workSpan)
    
    #Our modified potion of the hash state, which may or may not have wrapped around to the "front" of the string
    modSpan = workSpan[start:start+length][::-1]
    print(modSpan)
    
    for i in range(0,length):
        print((start+i)%16)
        workSpan[(start+i)%16] = modSpan[i]
    workSpan = workSpan[0:16]
    
    assert len(workSpan) == 16
    return workSpan
    
    
rope = [i for i in range(0,16)]
print(reverseSpan(rope,15,2))


#0 1 2] 3 4 5 [6 7 8
#modSpan == 2 1 0 8 7 6
#NewSpan needs to == 8 7 6] 3 4 5 [2 1 0