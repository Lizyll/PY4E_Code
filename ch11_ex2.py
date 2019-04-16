import re
fname = input('Enter a file:')
try:
    hand = open(fname)
except:
    print('Fail to open', fname)
    exit()

lst = list()
for line in hand:
    line = line.rstrip()
    x = re.findall('^New Revision: ([0-9.]+)', line)
    if x !=[]:
        for num in x:
            num = float(num)
            lst = lst + [num]

sum = sum(lst)
count = float(len(lst))
ave = sum/count
print(ave)
