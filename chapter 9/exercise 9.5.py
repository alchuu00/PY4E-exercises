fname = input("Enter file name: ")
file = open(fname)
count = {}

for line in file:
    if line.startswith("From "):
        line = line.rstrip()
        email = line.split()[1]
        domain = email.split("@")[1]
        count[domain] = count.get(domain, 0) + 1

print(count)