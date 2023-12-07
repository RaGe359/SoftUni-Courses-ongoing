deposit = float(input())
term = int(input())
percent = float(input())

amount = deposit + term * (((deposit * percent) / 12) / 100)

print(amount)