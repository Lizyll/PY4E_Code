fname = input('Enter a file name: ')
try:
    fhand = open(fname)
except:
    print('Fail to open ', fname)
    exit()

dow = dict()
for line in fhand:
    words = line.split()
    if len(words) == 0 or len(words) < 2 or words[0] != 'From': continue
    if words[2] not in dow:
        dow[words[2]] = 1
    else:
        dow[words[2]] += 1
print(dow)

#AttributeError: 'int' object has no attribute 'get'
#get function used on context is a dictionary function. But The type of context in the function here is Not a dictionary and thats why the error.
