def longest_substring(s):
    st = set()
    l = 0
    res = 0

    for r in range(len(s)):
        while s[r] in st:
            st.remove(s[l])
            l += 1

        st.add(s[r])
        res = max(res, r - l + 1)

    return res


s = input()
print(longest_substring(s))