"""
844. Backspace String Compare

Question:

Given two strings s and t, return true if they are equal
when both are typed into empty text editors.

'#' means a backspace character.

--------------------------------------------------

Example 1:

Input:
s = "ab#c"
t = "ad#c"

Output:
True

Explanation:
Both become "ac"

Time Complexity : O(n)

Space Complexity : O(1)
"""

s = "ab#c"
t = "ad#c"

i = len(s) - 1
j = len(t) - 1

skipS = 0
skipT = 0

while i >= 0 or j >= 0:

    # Find next valid character in s
    while i >= 0:

        if s[i] == '#':
            skipS += 1
            i -= 1

        elif skipS > 0:
            skipS -= 1
            i -= 1

        else:
            break

    # Find next valid character in t
    while j >= 0:

        if t[j] == '#':
            skipT += 1
            j -= 1

        elif skipT > 0:
            skipT -= 1
            j -= 1

        else:
            break

    # If both have valid characters
    if i >= 0 and j >= 0:

        if s[i] != t[j]:
            print(False)
            exit()

    # If only one string has a character left
    elif i >= 0 or j >= 0:
        print(False)
        exit()

    i -= 1
    j -= 1

print(True)