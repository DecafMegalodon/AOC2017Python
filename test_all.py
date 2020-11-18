#  Automated test for AOC 2017 based on my personal puzzle inputs
import fileinput
import subprocess
import time

# output = subprocess.run(args=["python3", 'day01b.py'], stdin=ioPipe, capture_output=True)
# print(output.stdout)
results = open("inputs/results.txt")

for day in range(1,3+1):
    paddedDay = ('0' if day < 10 
                else '') + str(day)
    dayInput = open("inputs/day" + paddedDay + ".txt")
    for part in ('a', 'b'):
        if day == 25 and part == 'b': #  No part b on on 25th
            print("Tests complete!")
            exit(0)
        progName = ''.join(['day', paddedDay, part, '.py'])
        startTime = time.time()
        subProc = subprocess.run(args=["python3", progName],
                                stdin=dayInput, capture_output=True)
        stopTime = time.time()
        output = str(subProc.stdout.decode('utf-8')).strip('\n')
        expected = results.readline().strip('\n')
        result = "OK" if output == expected else "FAIL"
        timeTaken = round(stopTime - startTime, 4)
        print("D" + paddedDay + part, str(result), timeTaken, "seconds")
        dayInput.seek(0,0)
