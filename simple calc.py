while True:
    try:
        a = float(input("What is your first number into the calculator: "))
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.")


oper = input("What is the operation you would like to use out of: +, -, *, /: ")
while oper not in ['+', '-', '*', '/']:
        oper = input("Invalid operation. Please choose from +, -, *, or /.")


while True:
    try:
        b = float(input("What is your second number into the calculator: "))
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.")


ans = 0

if oper == "+":
    ans = a+b
elif oper == "-":
    ans = a-b
elif oper == "*":
    ans = a*b
elif oper == "/":
    ans = a/b

print("your answer is:", ans)