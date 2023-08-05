#This is a comment
#print("Hello World")

# Variables and Constants
# x='Hello World'
# y = 5
# z = [1,2,3,4,5]

# print (type(x))
# print (type(y))
# print (type(z))

# Add two numbers in python
# print("Addition of two numbers")
# first = int(input("Enter first number: "))
# second = int(input("Enter second number: "))
# addition = first + second
# print(addition)
# print(f"The addition of {first} and {second} is {addition}")

# Functions 
# print("Addition of two numbers")
# def addTwoNumbers(first,second):
#     addition = first + second
#     print(f"The addition of {first} and {second} is {addition}")

# addTwoNumbers(4,5)

# Return key word
# def addFive(x):
#     return x + 5
# print(addFive(5))

# Kwargs

# def multiple(*names):
#     print(names)
# multiple('Hello', 'Hi', 'Good', 'Morning')

# def multiples(**names):
#     print(f"My name is {names['fname']}")

# multiples(fname="Gasana", lname = "Junior")

# Looping and Conditionals
# if if else for while

# x = 17
# if (x > 18):
#     print("Welcome to the Bar")
# elif (x == 17):
#     print("Just a year to go")
# else:
#     print("Gerarahiya")

# Loops
# for i in range(20):
#     if (i % 2 == 0):
#         continue
#     print(i)

# fruit = 'banana'
# count = 0
# for letter in fruit:
#     if letter == 'a':
#         count = count + 1
# print(count) 

# String Slices
# name = 'GASANA Didas Junior'
# print(name[7:12])
# s = 'Hello World'
# print(type(s))
# print(dir('str'))

# numbers = []
# while True:
#     num = input("Enter a number: ")
#     if num == 'done':
#         print(f"You entered {len(numbers)} numbers")
#         print(f"Their Sum is {sum(numbers)}")
#         print(f"Their average is {sum(numbers)/len(numbers)}")
#         break
#     else:
#         numb = int(num)
#         numbers.append(numb)

#### Dictionaries
# myDict = {}

# myDict['first'] = 1
# myDict['second'] = 2
# print(myDict['first'])

word = 'anna has two mangoes'
count = {}
for letter in word:
    if letter in count:
        count[letter] = count[letter] + 1
    else:
        count[letter] = 1
#print(count)
print(count.get('z', 0))

