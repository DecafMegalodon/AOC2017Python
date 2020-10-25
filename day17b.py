#  https://adventofcode.com/2017/day/17
import fileinput

puzInput = int(fileinput.input().readline().strip("\n"))
position = 1
curAnswer = 1

for i in range(1, 50000000+1):
    if position == 0:
        curAnswer = i
    position += (puzInput + 1) 
    position %= (i + 2)
    
print(curAnswer)