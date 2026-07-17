# Problem

# Given a string s, reverse only the vowels in the string and return the new string.

# Vowels are:

# a, e, i, o, u
# A, E, I, O, U
# Example 1
# Input: s = "hello"

# Output: "holle"

def reverseVowels(s):
    vowels = "aeiouAEIOU"

    s = list(s)

    left = 0
    right = len(s) - 1

    while left < right:

        while left < right and s[left] not in vowels:
            left += 1

        while left < right and s[right] not in vowels:
            right -= 1

        s[left], s[right] = s[right], s[left]

        left += 1
        right -= 1

    return "".join(s)


print(reverseVowels("hello"))
print(reverseVowels("leetcode"))