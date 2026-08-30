class Solution:
    def isPalindromic(self, s: str) -> bool:
        binary_string=''.join(format(ord(c),'08b')
                             for c in s)
        return binary_string == binary_string[::-1]