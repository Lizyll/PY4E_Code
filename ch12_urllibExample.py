import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('https://www.baidu.com/robots.txt')

for line in fhand:
    print(line.decode().strip())
