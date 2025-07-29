# 13. Find the length of a list without using len()
# Use a loop to count how many items are in a list

l=input("Enter the list items : ").split(" ")
count = 0
for _ in l :
    count+=1
print(f"Length of list is {count}")


