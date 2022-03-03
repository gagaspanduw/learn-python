print (1 < 1)
print (1 <= 1)
print (1 > 1)
print (1 >= 1)
print (1 == 1)
print (1 != 1)

name = input("What's your name?")
if name == "Jessica":
    print("Hello, nice to see you {}".format(name))
elif name == "Danielle":
    print("Hello, you are a great person!")
elif name == "Kingston": 
    print("Hi, {}, let's have lunch soon!".format(name))
else:
    print("Have a nice day!")

# Conditionals in calculator
def add():
    a = float(input("Enter a number."))
    b = float(input("Enter another number."))
    print(a + b)

def substraction():
    a = float(input("Enter a number."))
    b = float(input("Enter another number."))
    print(a - b)

def multiply():
    a = float(input("Enter a number."))
    b = float(input("Enter another number."))
    print(a * b)

def divide():
    a = float(input("Enter a number."))
    b = float(input("Enter another number."))
    print(a / b)

on = True    
while on:
    operation = input("What do you want calculate? type +, -, *, /, or quit:")
    if operation == '+':
        add()
    elif operation == '-':
        substraction
    elif operation == '*':
        multiply()
    elif operation == '/':
        divide()
    elif operation == 'quit':
        on = False
    else:
        print("That operation is not available.")