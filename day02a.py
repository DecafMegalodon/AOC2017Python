import fileinput

for line in fileinput.input():
    splitNumbers = line.split()
    splitNumbers = [int(''.join(chars)) for chars in splitNumbers]
    for datum in splitNumbers:
        print(datum)