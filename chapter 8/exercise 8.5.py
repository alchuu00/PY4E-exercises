count = 0
fname = input("Enter file name: ")
file = open(fname)
for line in file:
    line = line.rstrip()
    if line.startswith("From:"):
        count += 1
        words = line.split()
        print(count, words[1])