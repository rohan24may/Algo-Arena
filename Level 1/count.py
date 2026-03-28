s = input("Enter a string: ") #Count Vouels in a String 

count = 0
for ch in s:
    if ch in "aeiou":
        count += 1

print(count)