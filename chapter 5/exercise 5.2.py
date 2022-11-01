count = 0

while True:
    num_str = input("Enter a number: ")
    if num_str == "done":
        break
    try:
        number = int(num_str)
    except:
        print("Invalid input")
        continue

    if count == 0:
        min_number = number
        max_number = number
    elif number < min_number:
        min_number = number
    elif number > max_number:
        max_number = number

    count = count + 1

print(min_number, max_number)