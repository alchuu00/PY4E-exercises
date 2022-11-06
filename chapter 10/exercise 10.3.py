fname = input("Enter file name: ")
file = open(fname)
file = file.read()
count = {}

alphabet = "abcdefghijklmnopqrstuvxwyz"

for character in file:
    if character in alphabet:
        count[character] = count.get(character, 0) + 1

lst = list()
for k, v in count.items():
    character_tuple = (v, k)
    lst.append(character_tuple)

lst = sorted(lst, reverse=True)

for k, v in lst:
    print(k, v)
