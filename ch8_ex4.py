fname = input('file name: ')
try:
    fhand = open(fname)
except:
    print('Fail!')
    exit()

all_words = []
for lines in fhand:
    line_words = lines.split()
    for word in line_words:
        if word in all_words: continue
        all_words.append(word)
all_words.sort()
print(all_words)
