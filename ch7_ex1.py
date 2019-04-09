fname = input("Enter the file name: ")
try:
	xfile = open(fname)
except:
	print("The file cannot be opened: ", fname)
	exit()
#f = xfile.read()
count = 0
for line in xfile:
	count = count + 1
	line = line.rstrip().upper()  #remove the \n at the end of every line
	print(line)
print("There is ", count, "lines in this file.")
