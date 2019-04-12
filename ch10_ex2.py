fname = input('Enter a file name: ')
try:
    fhand = open(fname)
except:
    print('Fail to open', fname)
    exit()

tod = dict()
for line in fhand:
    line = line.rstrip()
    words = line.split()
    if len(words) == 0 or len(words) < 6 or words[0] != 'From': continue
    hrs = words[5].split(':')[:1]  #hrs is a list, dict cannot put a list as its key
    if hrs[0] not in tod:
        tod[hrs[0]] = 1
    else:
        tod[hrs[0]] += 1
print(tod)

lst = list()
for hrs, count in tod.items():
    lst.append((hrs, count))

lst.sort()
for hrs, count in lst:
    print(hrs, count)
