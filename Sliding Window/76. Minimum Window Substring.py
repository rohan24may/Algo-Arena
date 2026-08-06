class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(t) > len(s):
            return ""

        need = {}
        for ch in t:
            need[ch] = need.get(ch, 0) + 1

        required = len(need)

        window = {}
        formed = 0
        left = 0

        min_len = float("inf")
        start = 0

        for right in range(len(s)):

            # Add current character to window
            window[s[right]] = window.get(s[right], 0) + 1

            # Check if this character is now satisfied
            if s[right] in need and window[s[right]] == need[s[right]]:
                formed += 1

            # Shrink while window is valid
            while formed == required:

                # Update minimum window
                if (right - left + 1) < min_len:
                    min_len = right - left + 1
                    start = left

                # Remove left character
                window[s[left]] -= 1

                # If requirement is no longer satisfied
                if s[left] in need and window[s[left]] < need[s[left]]:
                    formed -= 1

                left += 1

        if min_len == float("inf"):
            return ""

        return s[start:start + min_len]