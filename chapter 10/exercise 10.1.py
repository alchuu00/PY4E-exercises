fname = input("Enter file name: ")
file = open(fname)
count = {}

for line in file:
    if line.startswith("From "):
        line = line.rstrip()
        email = line.split()[1]
        count[email] = count.get(email, 0) + 1

lst = list()
for k,v in count.items():
    count_tuple = (v, k)
    lst.append(count_tuple)

lst = sorted(lst, reverse=True)

for v, k in lst[:1]:
    print(v, k)



