poem = open ("romeo.txt", "r")
words = []
for line in poem:
    for word in line.split():
        if word not in words:
            words.append(word)
print(sorted(words))
