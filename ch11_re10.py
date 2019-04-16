import re

hand = open('mbox1.txt')
for line in hand:
    line = line.rstrip()
    #start with 'X' followed by any non whitespace characters and ':'
    #followed by a space and any number
    #the number can include a decimal
    if re.search('^X-\S*: [0-9.]+', line):
        print(line)
