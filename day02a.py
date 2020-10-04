import fileinput

for line in fileinput.input():
    splitNumbers = line.split()
    [''.join(chars) for chars in splitNumbers]
    for datum in splitNumbers: #Don't process newline character at the end
        print(datum)