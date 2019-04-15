import re

fhand = open('mbox.txt')
num = list()
for line in fhand:
    line = line.rstrip()
    stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)
    if len(stuff) != 1: continue #if not match, returns an empty list
    print(stuff)
    n = float(stuff[0])
    num.append(n)
print('Maximum:', max(num))
