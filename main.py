def operation():

    # greeting
    print("welcome to the calculator")

    # inputs
    num1 = float(input("enter the first number: "))
    operator = input("enter the operator: ")
    num2 = float(input("enter the second number: "))

    # if condition
    if operator == "+":
        print(num1 + num2)
    elif operator == "-":
        print(num1 - num2)
    elif operator == "*":
        print(num1 * num2)
    elif operator == "/":
        print(num1 / num2)
    else:
        print("Error")
    
    # gratitude
    print("thank you")

try:
    operation()
except ValueError:
    print("this is not number")