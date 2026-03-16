start = int(input("Enter start number: "))
end = int(input("Enter end number: "))

for num in range(start, end + 1):

    temp = num
    sum = 0

    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10

    if num == sum:
        print(num)