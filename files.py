########## Reading from files #############
# file = input("Please Enter the File: ")
# try:
#     fhand = open(file)
# except: 
#     print("The file you entered can't be found")
#     exit()
# count = 0
# for lines in fhand:
#     line = lines.rstrip()
#     if line.startswith("Hello There"):
#         print(line)

############### Writing to files ##############
fhand1 = open("hello.txt")
fhand = open("hello1.txt", 'w')
text = ''
for lines in fhand1:
    line = lines.rstrip()
    text += line
text1 = "Jackson is cool"
text += text1
fhand.write(text)
fhand.close()