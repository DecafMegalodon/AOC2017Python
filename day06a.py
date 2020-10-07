import fileinput

indata = fileinput.input().readline()
banks = [int(num) 
            for num in indata.split()
            ]
print (banks)