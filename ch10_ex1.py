fname = input('Enter a file name:')
try:
    fhand = open(fname)
except:
    print('Fail to open', fname)
    exit()

d = dict()
for line in fhand:
    line = line.rstrip()
    words = line.split()
    if len(words) == 0 or len(words) < 2 or words[0] != 'From': continue
    if words[1] not in d:
        d[words[1]] = 1
    else:
        d[words[1]] += 1
#print(d)

lst = list()
for email, count in d.items():
    lst.append( (count, email) )
lst.sort(reverse = True)
for count, email in lst[:1]:
    print(email, count)
