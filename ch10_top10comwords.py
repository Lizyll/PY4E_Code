fhand = open('romeo.txt')
count = dict()
for line in fhand:
    words = line.split()
    for word in words:
        count[word] = count.get(word, 0) + 1

lst = list()
for key, val in count.items():
    tmp = (val, key)
    lst.append(tmp)

lst = sorted(lst, reverse = True)

for val, key in lst[:10] :
    print(key, val)
