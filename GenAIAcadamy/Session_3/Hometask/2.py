#write function to check the given string is Palindrome

def isPalindrom(word):
    return word == word[::-1]

word = str(input("Enter the word: "))
print(isPalindrom(word))