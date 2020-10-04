import fileinput

rollingChecksum = 0

for line in fileinput.input():
    if(line == "\n"):
        break
    nums = line.split()
    nums = [int(''.join(chars)) for chars in nums]
    permutations = []
    for first in range(0, len(nums)):
        for second in range(first+1, len(nums)):
            permutations.append( [nums[first], nums[second]])
            
    for perm in permutations:
        if perm[0] % perm[1] == 0 or perm[1] % perm[0] == 0:
            rollingChecksum += max(perm[0], perm[1]) // min(perm[0], perm[1])
            break

print(rollingChecksum)