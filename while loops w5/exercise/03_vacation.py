money_needed = float(input())
current_money = float(input())
days_spend = 0
total_days = 0

while True:
    action = input()
    amount = float(input())

    total_days += 1
    
    if action == "save":
        current_money += amount
        days_spend = 0
    elif action == "spend":
        current_money -= amount
        days_spend += 1

        if current_money < 0:
            current_money = 0

    if days_spend == 5:
        print(f"You can't save the money.")
        print(f"{total_days}")   
        break

    if current_money >= money_needed:
        print(f"You saved the money for {total_days} days.")
        break