#https://adventofcode.com/2017/day/11
import fileinput

path = fileinput.input().readline()[:-1:].split(',') #Trim out newline at the end and split up!
print(path)