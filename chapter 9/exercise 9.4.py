fname = input("Enter file name: ")
file = open(fname)
count = {}

for line in file:
    if line.startswith("From "):
        line = line.rstrip()
        emails = line.split()
        emails = emails[1]
        count[emails] = count.get(emails, 0) + 1

max_address = None
max_emails = 0
for key in count:
    if count[key] > max_emails:
        max_address = key
        max_emails = count[key]

print(max_address, max_emails)
