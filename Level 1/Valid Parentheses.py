def is_valid(s):
    stack = []
    mp = {')':'(', '}':'{', ']':'['}

    for ch in s:
        if ch in mp.values():
            stack.append(ch)
        else:
            if not stack or stack[-1] != mp[ch]:
                return False
            stack.pop()

    return True if not stack else False


s = input()
print(is_valid(s))