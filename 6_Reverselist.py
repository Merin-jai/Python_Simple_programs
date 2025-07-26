# 6. Reverse a List
# Write a program to reverse a list without using the built-in reverse() function.

n = input("Enter value for list ").split()
print(n)

# using reverse
# n.reverse()
# print(n)

# # using list slicing [::-1]
# rev = n[::-1]
# print(rev)

# using for loop
rev =[]
for val in n :
    rev.insert(0,val)
print(rev)
 