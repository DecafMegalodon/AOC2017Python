import fileinput

rollingChecksum = 0

for line in fileinput.input():
    if(line == "\n"):
        break
    nums = line.split()
    nums = [int(''.join(chars)) for chars in nums]
    for first in range(0, len(nums)):
        for second in range(first+1, len(nums)):
            print("%d ? %d" % (nums[first], nums[second]))

print(rollingChecksum)