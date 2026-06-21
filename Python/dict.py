nums = [1,2,2,3,3,3]

dict = {}

for i in nums:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1

print(dict)