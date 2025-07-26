# 9. Simple Calculator
# Create a simple calculator that can add, subtract, multiply, or divide two numbers based on user input.

a=int(input("a = "))
b=int(input("b = "))

ch = input("Enter operator (+,-,/,*)")

if ch == '+' :
    r = a + b
elif ch == '-' :
    r = a-b
elif ch == '/' :
    if (b==0) :
        print("Division by zero not possible")
    else :
        r = a/b
elif ch == '*' :
    r = a*b
else :
    r = "Invalid input"

print ("result ",r)