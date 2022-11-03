num_list = []
while True:
    numbers_str = input("Enter a number: ")
    if numbers_str == "done":
        break
    try:
        numbers = float(numbers_str)
    except:
        print("invalid input")
        continue
    num_list.append(numbers)

print("maximum is", max(num_list))
print("minimum is", min(num_list))
