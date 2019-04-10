#counting words in text
fname = input('Enter a file name: ')
try:
    fhandle = open(fname)
except:
    print('Fail to open the file.')
#words dic
counts = dict()
for line in fhandle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
#cal the big count
bigword = None
bigcount = None
for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
print('bigword: ', bigword, ', big count: ', bigcount)
