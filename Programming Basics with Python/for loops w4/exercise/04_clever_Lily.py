age = int(input())
washing_machine = float(input())
toy_price = int(input())

initial_gift = 10
toys = 0
money = 0

for i in range(1, age+1):
    if i % 2 == 0 and i == 2:
        money += initial_gift
        money -= 1
    elif i % 2 == 0:
        money += initial_gift + 10
        initial_gift += 10
        money -= 1
    else:
        toys += 1

savings = money + toys * toy_price
diff = abs(savings - washing_machine)

if savings >= washing_machine:
    print(f'Yes! {diff:.2f}')
else:
    print(f'No! {diff:.2f}')
