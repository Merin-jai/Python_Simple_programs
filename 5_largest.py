# 5. Find the Largest Number
# Take three numbers from the user and print the largest one.
a=int(input("Enter first "))
b=int(input("Enter second "))
c=int(input("Enter third "))
if a > b :
    if a > c :
        large = a
    else :
        large = c 
elif a > c :
    large = a
else :
    if b > c :
        large = b
    else :
        large = c
print(f"Largest is {large}")
