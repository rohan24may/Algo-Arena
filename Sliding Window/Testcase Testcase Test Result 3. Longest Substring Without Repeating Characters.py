class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        left = 0
        freq = {}
        res = 0

        for right in range(len(s)):

            # Add current character
            freq[s[right]] = freq.get(s[right], 0) + 1

            # Shrink window until duplicate is removed
            while freq[s[right]] > 1:
                freq[s[left]] -= 1

                if freq[s[left]] == 0:
                    del freq[s[left]]

                left += 1

            # Update answer
            res = max(res, right - left + 1)

        return res
        