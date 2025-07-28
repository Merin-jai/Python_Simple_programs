# 5. Find the Largest Number
# Take three numbers from the user and print the largest one.
a=int(input("Enter first "))
b=int(input("Enter second "))
c=int(input("Enter third "))
if a > b & a > c :
        large = a
elif b > c:
        large = b
else :
        large = c
large = max(a,b,c)
print(f"Largest is {large}")

