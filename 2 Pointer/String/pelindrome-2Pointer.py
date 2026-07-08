"""
125. Valid Palindrome

Given a string s, return True if it is a palindrome,
otherwise return False.

A palindrome reads the same forwards and backwards.

Example 1:
Input: "racecar"
Output: True

Example 2:
Input: "hello"
Output: False
"""

s = input("Enter a string: ")

left = 0
right = len(s) - 1

is_palindrome = True

while left < right:

    if s[left] == s[right]:
        left += 1
        right -= 1

    else:
        is_palindrome = False
        break

if is_palindrome:
    print("It is a Palindrome ✅")
else:
    print("It is NOT a Palindrome ❌")