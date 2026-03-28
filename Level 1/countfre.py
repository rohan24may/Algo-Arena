s = input("Enter string: ")

freq = {}

# count frequency
for ch in s:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

# collect all unique characters
res = []

for ch in s:
    if freq[ch] == 1:
        res.append(ch)

print("Unique characters:", res)