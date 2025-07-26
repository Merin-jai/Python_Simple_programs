# 10. Fibonacci Series
# Write a program to print the first n numbers of the Fibonacci series.
# (Input: 6 → Output: 0 1 1 2 3 5)

n = int(input("Enter limit : "))
f1=0
f2=1
print(f1," ",f2," ",end="")
for i in range(2,n) :
    f3=f1+f2
    print(f3," ",end="")
    f1 = f2
    f2 = f3
