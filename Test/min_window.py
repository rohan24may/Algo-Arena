# Minimum Window Substring 🔥🔥 👉 Smallest substring containing all chars of another string

from collections import Counter

def min_window(s, t):
    need = Counter(t)
    have = {}
    l = 0
    res = ""
    count = 0

    for r in range(len(s)):
        ch = s[r]
        have[ch] = have.get(ch, 0) + 1

        if ch in need and have[ch] <= need[ch]:
            count += 1

        while count == len(t):
            if res == "" or (r-l+1) < len(res):
                res = s[l:r+1]

            have[s[l]] -= 1
            if s[l] in need and have[s[l]] < need[s[l]]:
                count -= 1
            l += 1

    return res