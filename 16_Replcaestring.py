# 16. Replace a word with another in a given string
# Input: "Python is easy" → Replace: "easy" with "fun"
s=input("Enter a string : ")
word=input("Enter the word to replace : ")
replace=input("Enter the replace word : ")
new=s.replace(word,replace)
print(f"Word after replacing : {new}")