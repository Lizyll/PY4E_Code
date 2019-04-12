import string

fname = input('enter a file name:')
try:
    fhand = open(fname)
except:
    print('fail to open', fname)
    exit()

letters = dict()
for line in fhand:
    line = line.rstrip().lower()
    line = line.translate(line.maketrans('','', string.punctuation))
    line = line.translate(line.maketrans('','', string.digits))
    words = line.split()
    for word in words:
        letters[word] = letters.get(word, 0) + 1

lst = list()
for word, count in letters.items():
    lst.append((word, count))
lst.sort(reverse = True)
for word, count in lst:
    print(word, count)
