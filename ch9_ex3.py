fname = input('Enter a file name: ')
try:
    fhand = open(fname)
except:
    print('Fail to open ', fname)
    exit()

eaddr = dict()
for line in fhand:
    if not line.startswith('From'): continue
    words = line.split()
    if words[1] not in eaddr:
        eaddr[words[1]] = 1
    else:
        eaddr[words[1]] += 1
print(eaddr)
