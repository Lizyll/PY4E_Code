import re

hand = open('mbox1.txt')
for line in hand:
    line = line.rstrip()
    #start with 'X' followed by any non whitespace characters and ':'
    #followed by a space and any number, the number can include a decimal
    #then print the number if it is greater than zero
    #while what the whole expression to match, only interested in extracting a portion of the (substring) 
    x = re.findall('^X-\S*: ([0-9.]+)', line)
    if len(x) > 0:
        print(x)
