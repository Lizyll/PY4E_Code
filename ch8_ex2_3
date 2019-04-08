fname = input('file name: ')
try:
    fhand = open(fname)
except:
    print('Fail!')
    exit()
count = 0
for line in fhand:
    words = line.split()
    if len(words) >2 and words[0] == 'From':
        print(words[2])
