count = 0
total = 0

while True:
    num_str = input("Enter a number: ")
    if num_str == "done":
        break
    try:
        number = int(num_str)
    except:
        print("Invalid input")
        continue
    total = total + number
    count = count + 1

print(total, count, total/count)



