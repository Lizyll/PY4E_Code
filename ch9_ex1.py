fname = input('Enter a file name: ')
try:
    fhandle = open(fname)
except:
    print('Fail to open the file.')
    exit()

fwords = dict()
for line in fhandle:
    words = line.split()
    for word in words:
        fwords[word] = fwords.get(word)
while True:
    w = input('What word do you want to find?')
    if w == 'done': break
    print(w in fwords)
