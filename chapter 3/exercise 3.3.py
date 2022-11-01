score = input("Enter the score (between 0.0 and 1.0): ")
try:
    score = float(score)
except:
    print("Error, please input valid score.")
    quit()

if score < 0 or score > 1:
    print("Score is out of range.")
elif score >= 0.9:
    print(f"Score: {score}, Grade A")
elif 0.9 > score >= 0.8:
    print(f"Score: {score}, Grade B")
elif 0.8 > score >= 0.7:
    print(f"Score: {score}, Grade C")
elif 0.7 > score >= 0.6:
    print(f"Score: {score}, Grade D")
else:
    print(f"Score: {score}, Grade F")