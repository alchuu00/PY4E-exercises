count = dict()
fname = input("Enter file name: ")
file = open(fname)
for line in file:
    line = line.rstrip()
    if line.startswith("From "):
        days = line.split()
        days = days[2]
        count[days] = count.get(days, 0) + 1

print(count)
