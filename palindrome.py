# Check if a string is a palindrome
text = input("Enter a string: ")

reverse = text[::-1]

if text == reverse:
    print("It is a palindrome string")
else:
    print("It is NOT a palindrome")


# Check if the number is a palindrome
num = int(input("Enter a number: "))

original = num
reverse = 0

while num > 0:

    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

if original == reverse:
    print("It is a palindrome number")
else:
    print("It is NOT a palindrome")