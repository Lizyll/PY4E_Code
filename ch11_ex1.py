import re
fname = 'mbox.txt'
hand = open(fname)
x = input('Enter a regular expression:')
count = 0
for line in hand:
    line = line.rstrip()
    if re.findall(x, line) != []:
        count += 1
print(fname, 'had', count, 'lines that matched', x)
