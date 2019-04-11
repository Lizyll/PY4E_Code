fname = input('Enter a file name: ')
try:
    fhand = open(fname)
except:
    print('Fail to open ', fname)
    exit()

eaddr = dict()
for line in fhand:
    #if not line.startswith('From'): continue
    #many lines that start with From also have addr in them. using this line would double the outcome
    #be specific about the data line we want 
    words = line.split()
    if len(words) == 0 or len(words) < 1 or words[0] != 'From': continue
    words[1] = words[1].split('@')[-1]
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
