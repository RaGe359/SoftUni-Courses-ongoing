inpt = input()
total = 0

while inpt != "NoMoreMoney":
    amount = float(inpt)

    if amount < 0:
        print("Invalid operation!")
        break 

    total += amount
    print(f'Increase: {amount:.2f}')
    inpt = input()

print(f'Total: {total:.2f}')