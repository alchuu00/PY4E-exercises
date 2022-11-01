# user inputs the data
hours = input("Enter hours: ")
rate = input("Enter rate: ")
# input is always string, so we have to convert to float
pay = float(hours) * float(rate)

if pay > 40:
    pay = pay * 1.5
    print("You worked overtime!")
    print(f"For {hours} hours of work you get {pay} dollars.")
else:
    print(f"For {hours} hours of work you get {pay} dollars.")
