count = dict()
fname = input("Enter file name: ")
file = open(fname)
for line in file:
    line = line.rstrip()
    if line.startswith("From "):
        emails = line.split()
        emails = emails[1]
        count[emails] = count.get(emails, 0) + 1

print(count)