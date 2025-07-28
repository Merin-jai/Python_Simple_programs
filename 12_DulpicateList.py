# 12. Remove duplicate values from a list using a set or loop
# Input: [1, 2, 2, 3, 4, 4]

l=input ("Enter the list values : ").split(" ")
print(f"List : {l}")
unique_list=list(set(l))
print(f"Unique List : {unique_list}")
