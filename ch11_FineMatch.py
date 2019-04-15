import re

fname = input('enter a file name:')
try:
    fhand = open(fname)
except:
    print('fail')
    exit()

for line in fhand:
    line = line.rstrip()
    #'^X'=start with 'X-' 
    #'\S'=match any non-whitespace character
    #'+'=one or more time
    #':'=another character
    if re.search('^X-\S+:', line):
        print(line)
