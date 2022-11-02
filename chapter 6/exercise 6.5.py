str = 'X-DSPAM-Confidence:0.8475'

num_start = str.find(":")
print(num_start)

num_end = str.find("5")
print(num_end)

num = str[num_start+1 : num_end+1]
num = float(num)

print(num, type(num))

# checked to se if its really float
print(num+10)