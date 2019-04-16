import re

hand = open('mbox1.txt')
for line in hand:
    line = line.rstrip()
    #start with a single lowercase letter, uppercase letter, or number [a-zA-Z0-9]
    #follow by zero or non blank characters \S*
    #follow by an uppercase or lowercase letter
    x = re.findall('[a-zA-Z0-9]\S+@\S+[a-zA-Z]', line)
    if len(x) > 0:
        print(x)
