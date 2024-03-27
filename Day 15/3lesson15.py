def is_palindrome(word):
    word = word.lower() 
    return word == word[::-1]


print(is_palindrome("anastasia"))
print(is_palindrome("nini"))
print(is_palindrome("hello"))