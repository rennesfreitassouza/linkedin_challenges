
import re

# https://www.linkedin.com/learning/python-code-challenges/identify-a-palindrome
def isaPalindrome(string):
    letters = ''.join(re.findall(r'(?ai)[a-z]+', string))
    
    backwl = letters[::-1].lower()

    return backwl == letters.lower()

def main():
    string = input("Type a word: ")
    return isaPalindrome(string)

if __name__ == '__main__': main()
