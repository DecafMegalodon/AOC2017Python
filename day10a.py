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
    workRope = rope+rope

    #Our modified potion of the hash state, which may or may not have wrapped around to the "front" of the string
    modRope = workSpan[start:start+length][::-1]
    
    for i in range(0,length):
        workRope[(start+i)%256] = modSpan[i]
    workSpan = workSpan[0:256]
    
    return workRope

indata = fileinput.input().readline()
data = [int(num) 
            for num in indata.split(',')
            ]
print(data)

#0 1 2] 3 4 5 [6 7 8
#modSpan == 2 1 0 8 7 6
#NewSpan needs to == 8 7 6] 3 4 5 [2 1 0