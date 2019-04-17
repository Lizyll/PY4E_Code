import urllib.request, urllib.parse, urllib.error
fname = input('Enter - ')
try:
    fhand = urllib.request.urlopen(fname)
except:
    print('invalid url')
    exit()
char = 0
for line in fhand:
    words = line.decode()
    char = char + len(words)
    if char < 3000:
        print(line.decode().strip())
print(char)
