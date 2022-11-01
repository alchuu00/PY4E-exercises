def computegrade(score):
    if score < 0 or score > 1:
        return "Score is out of range."
    elif score >= 0.9:
        return "A"
    elif 0.9 > score >= 0.8:
        return "B"
    elif 0.8 > score >= 0.7:
        return "C"
    elif 0.7 > score >= 0.6:
        return "D"
    else:
        return "F"


score = input("Enter the score (between 0.0 and 1.0): ")
try:
    score = float(score)
except:
    print("Error, please input valid score.")
    quit()

print(f"Score: {score}, grade: {computegrade(score)}")