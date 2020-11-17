#  Automated test for AOC 2017 based on my personal puzzle inputs
import fileinput
import subprocess
import time


ioPipe = open("inputs/day01.txt")

start = time.time()
print(start)
output = subprocess.run(args=["python3", 'day01b.py'], stdin=ioPipe, capture_output=True)
print(output.stdout)

# for day in range(1,25+1):
    # for part in ('a', 'b'):
        # if day == 25 and part == 'b': #  No part b on on 25th
            # print("Tests complete!")
            # exit(0)
        # print(str(day) + part + '.py')
        
