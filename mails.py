try:
    fhand = open('mbox-short.txt')
except: 
    print("File not found")
    exit()

mailCount = {}
for lines in fhand:
    line = lines.rstrip()
    if line.startswith("From "):
        splitLine = line.split()
        day = splitLine[2]
        if day in mailCount:
           mailCount[day] = mailCount[day] + 1
        else:
            mailCount[day] = 1
print(mailCount)
