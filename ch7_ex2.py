fname = input("Enter the file name: ")
try:
	xfile = open(fname)
except:
	print("The file cannot be opened: ", fname)
	exit()
sum = 0
count = 0
for line in xfile:
    if not line.startswith('X-DSPAM-Confidence:'):
        continue
    pos = line.find(' ')
    val = line[pos:].rstrip()
    val = float(val)
    sum = sum + val
    count = count + 1
print('Average spam confidence: ', sum/count)
