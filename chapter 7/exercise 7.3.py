fname = input("Enter file name: ")
if fname == "na na boo boo":
    print("NA NA BOO BOO TO YOU - You have been punk'd!")
    quit()
else:
    count = 0
    total_confidence = 0

    # file name is: mbox-short.txt or mbox.txt
    fhand = open(fname)
    for line in fhand:
        if line.startswith("X-DSPAM-Confidence:"):
            space_index = line.find(" ")
            num = float(line[space_index+1:])
            total_confidence += num
            count += 1

    average = total_confidence / count
    print(f"Average spam confidence: {average}")
