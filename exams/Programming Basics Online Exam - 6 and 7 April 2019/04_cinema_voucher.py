voucher_value = int(input())
purchased_tickets = 0
purchased_other = 0

while True:
    purchase = input()
    if purchase == "End":
        break

    if len(purchase) > 8:
        price = ord(purchase[0]) + ord(purchase[1])
        if price > voucher_value:
            break
        purchased_tickets += 1
    else:
        price = ord(purchase[0])
        if price > voucher_value:
            break
        purchased_other += 1

    voucher_value -= price

print(f"{purchased_tickets}")
print(f"{purchased_other}")