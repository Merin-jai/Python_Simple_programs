# 4. Palindrome Checker
# Check whether a given string is a palindrome.
# (Input: "madam" → Output: True)

s = input("Enter a string : ")
if(s == s[::-1]) :
    print("Palindrome string")
else :
    print("Not palindrome")