# 8. Count Vowels in a String
# Write a Python function that counts the number of vowels in a given string.

def count_vowels(n) :
    vowels = "aeiouAEIUO"
    count = 0
    for char in n :
        if char in vowels :
            count+=1
    print(f"Count of vowels is {count}")

n = input("Enter String : ")
count_vowels(n)
