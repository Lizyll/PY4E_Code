import string

fname = input('Enter a file name: ')
try:
    fhandle = open(fname)
except:
    print('Fail to open the ', fname)
    exit()

count = dict()
for line in fhandle:
    #Python treat 'soft!' and 'soft'; 'Soft' and 'soft' as different words.Thus we need to remove punctuation marks and lowercase all
    line = line.rstrip().lower()  
    # line = line.translate(line.maketrans(fromstr, tostr, deletestr)
    line = line.translate(line.maketrans('', '', string.punctuation))
    words = line.split()
    for word in words:
        count[word] = count.get(word, 0) + 1
print(count)
