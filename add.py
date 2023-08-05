x = input("Enter first number: ")
y = input("Enter second number: ")
try:
    first = int(x)
    second = int(y)
    print(first / second)
except ValueError:
    print("Please Enter valid numbers")
except ZeroDivisionError:
    print("The second number can't be zero")