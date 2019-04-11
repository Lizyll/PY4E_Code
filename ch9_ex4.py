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

bigword = None
bigcount = None
for word, count in eaddr.items():
    if bigcount is None or bigcount < count:
        bigcount = count
        bigword = word
print(eaddr)
print('Maximum messages from:', bigword, 'who has sent', bigcount, 'times.')
