# 3. Factorial of a Number
# Write a function to find the factorial of a number using a loop.
# (Input: 4 → Output: 24)
n=int(input("Enter the limit : "))
fact = 1
for i in range(1,n+1) :
    fact *=i

print("Factorial of ",n," is ",fact)