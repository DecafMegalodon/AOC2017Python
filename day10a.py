#https://adventofcode.com/2017/day/10
import fileinput

"""
Our input is a list of lengths
Our "state" is 256 elements long, circular, and 0 indexed
Lengths larger than the size of the list are invalid.


Reverse the order of that length of elements in the list, starting with the element at the current position.
Move the current position forward by that length plus the skip size.
Increase the skip size by one.
"""

#Technically, we're working with "string" not a "rope",
#but rope was chosen as  name here for clarity
def reverseSpan(rope, start, length):
    workSpan = rope+rope
    prespan = workSpan[0:start]
    span = workSpan[start:start+length][::1]
    postspan = workSpan[start+length:16+start]
    print(prespan, span, postspan)
    #workSpan = workSpan[0:length-1] + workSpan[start:start+length][::-1] + workSpan[start+length:16+start-length] #Everything is in the right order, but shifted a bit now
    #print(workSpan)
    assert len(workSpan) == 16
    return workSpan
    
    
rope = [i for i in range(0,16)]
print(reverseSpan(rope,12,5))