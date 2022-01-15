
import re

def isaPalindrome(string):
    '''https://www.linkedin.com/learning/python-code-challenges/identify-a-palindrome'''
    letters = ''.join(re.findall(r'(?ai)[a-z]+', string))
    
    # backwl = letters[::-1].lower()
    backwl = ''.join(reversed(letters))
    return backwl.lower() == letters.lower()

def main():
    string = input("Type a word: ")
    return isaPalindrome(string)

if __name__ == '__main__': main()
