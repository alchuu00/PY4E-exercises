# user inputs the data
hours = input("Enter hours: ")
rate = input("Enter rate: ")

# input is always string, so we have to convert to float
try:
    hours = float(hours)
    rate = float(rate)
except:
    print("Error, please enter numeric input.")
    quit()

pay = hours * rate

if hours >= 40:
    pay = pay * 1.5
    print("You worked overtime!")

else:
    print("You worked regular!")

print(f"For {hours} hours of work you get {pay} dollars.")
