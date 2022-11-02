fname = input("Enter file name: ")
# file name is: mbox-short.txt
fhand = open(fname)
for line in fhand:
    line = line.rstrip()
    print(line.upper())