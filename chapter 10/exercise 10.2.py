fname = input("Enter file name: ")
file = open(fname)
count = {}

for line in file:
    if line.startswith("From "):
        line = line.rstrip()
        email = line.split()[5]
        hour = email.split(":")[0]
        count[hour] = count.get(hour, 0) + 1

lst = list()
for k, v in count.items():
    hour_tuple = (k, v)
    lst.append(hour_tuple)

lst = sorted(lst)

for k, v in lst:
    print(k, v)

