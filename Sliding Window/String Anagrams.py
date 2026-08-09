class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        window = {}
        need = {}
        left = 0
        result = []

        # Count characters in p
        for ch in p:
            need[ch] = need.get(ch, 0) + 1

        # Sliding window over s
        for right in range(len(s)):
            window[s[right]] = window.get(s[right], 0) + 1

            # Keep window size equal to len(p)
            while right - left + 1 > len(p):
                window[s[left]] -= 1

                if window[s[left]] == 0:
                    del window[s[left]]

                left += 1

            # Check if current window is an anagram
            if window == need:
                result.append(left)

        return result