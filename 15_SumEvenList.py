# 15. Write a program to find the sum of only even numbers in a list
l=input("Enter the list elements : ").split(" ")
numbers = []
for i in l:
    numbers.append(int(i))
print(numbers)
sum = 0
for i in numbers : 
    if i%2==0 :
        sum+=i
print("Sum of even numbers in the list : ",sum)

