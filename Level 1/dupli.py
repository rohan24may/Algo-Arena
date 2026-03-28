n = int(input("Enter size: "))
arr = list(map(int, input("Enter elements: ").split()))

res = []

for x in arr:
    if x not in res:
        res.append(x)

print("Without duplicates:", res)