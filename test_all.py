#  Automated test for AOC 2017 based on my personal puzzle inputs
import fileinput
import subprocess
import time

testsPassed = 0
testsFailed = 0
testsSlow = 0
results = open("inputs/results.txt")

for day in range(1,25+1):
    paddedDay = ('0' if day < 10 
                else '') + str(day)
    dayInput = open("inputs/day" + paddedDay + ".txt")
    for part in ('a', 'b'):
        if day == 25 and part == 'b': #  No part b on on 25th
            break
        progName = ''.join(['day', paddedDay, part, '.py'])
        startTime = time.time()
        subProc = subprocess.run(args=["python3", progName],
                                stdin=dayInput, capture_output=True)
        stopTime = time.time()
        output = str(subProc.stdout.decode('utf-8')).strip('\n')
        expected = results.readline().strip('\n')
        testCorrect = (output == expected)
        result = "OK" if testCorrect else "FAIL"
        timeTaken = round(stopTime - startTime, 4)
        print("D" + paddedDay + part, str(result), timeTaken, "seconds")
        
        if testCorrect:
            testsPassed += 1
        else:
            testsFailed += 1

        if timeTaken >= 15:
            testsSlow += 1

        dayInput.seek(0,0)

print("Test results: %d passed, %d failed, %d slow" % (testsPassed, testsFailed, testsSlow))