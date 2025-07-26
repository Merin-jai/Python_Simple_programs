# 7. Multiplication Table Generator
# Write a program that takes a number as input and prints its multiplication table (up to 10).

n = int(input("Enter number : "))
for i in range(1,11) : 
    print(f" {i} x {n} = {i*n}")

