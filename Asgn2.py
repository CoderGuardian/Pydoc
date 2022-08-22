def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

while True: 
    num1 = float(input("Enter first number: "))
    exp=input("Enter Operation : ")
    num2 = float(input("Enter second number: "))
 
    if exp == '+':
        print(num1, "+", num2, "=", add(num1, num2))
    elif exp == '-':
        print(num1, "-", num2, "=", subtract(num1, num2))
    elif exp == '*':
        print(num1, "x", num2, "=", multiply(num1, num2))
    elif exp == '/':
        print(num1, "/", num2, "=", divide(num1, num2))
    else:
        print("Invalid Input")
    flag = input("Exit? (Y/N): ")
    if flag == "Y" or flag == "y":
        break    
