#Advent of code day 04b
import fileinput

def split(string):
    return [char for char in string]

validPasswords = 0

for line in fileinput.input():
    if(line == "\n"):
        break
    words = line.split()
    #Sort the characters within the string. Anagrams will result in identical strings when sorted
    words = [''.join(sorted(split(word))) for word in words]
    #print(words)
    
    if len(words) == len(set(words)):
        validPasswords += 1
        
print(validPasswords)