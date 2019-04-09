fname = input('File name: ')
try:
    fhand = open(fname)
except:
    print('There is an exception.')
    exit()

count = 0
for line in fhand:
    if not line.startswith('From'): continue
    count = count + 1
    words = line.split()
    print(words[1])
print('There is ', count, ' From lines.')
