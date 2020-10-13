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
    modRope = workSpan[start:start+length][::-1]
    
    for i in range(0,length):
        workRope[(start+i)%len(rope)] = modSpan[i]
    workSpan = workSpan[0:len(rope)]
    
    return workRope

indata = fileinput.input().readline()
data = [int(num) 
            for num in indata.split(',')
            ]

