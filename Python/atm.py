balance = int(input("Balance: "))
amount = int(input("Amount: "))

if amount % 100 != 0:
    print("Invalid Amount")
elif amount > balance:
    print("Insufficient Balance")
elif balance - amount < 500:
    print("Minimum Balance Rule Violated")
else:
    print("Transaction Successful")