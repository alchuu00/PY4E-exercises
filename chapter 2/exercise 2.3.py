# user inputs the data
hours = input("Enter hours: ")
rate = input("Enter rate: ")
# input is always string so we have to convert to float
pay = float(hours) * float(rate)
print(f"For {hours} hours of work you get {pay} dollars.")
