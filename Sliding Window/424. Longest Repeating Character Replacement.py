class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        freq = {}
        max_freq = 0
        max_len = 0

        for right in range(len(s)):
            # Add current character
            freq[s[right]] = freq.get(s[right], 0) + 1

            # Update the maximum frequency in the current window
            max_freq = max(max_freq, freq[s[right]])

            # If more than k replacements are needed, shrink the window
            while (right - left + 1) - max_freq > k:
                freq[s[left]] -= 1
                left += 1

            # Update the answer
            max_len = max(max_len, right - left + 1)

        return max_len