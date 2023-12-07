budget = int(input())
season = input()
fishermen = int(input())
rent = 0

if season == "Spring":
    rent = 3000
    if fishermen <= 6:
        rent *= 0.9
        if fishermen % 2 == 0:
            rent *= 0.95
        else:
            pass
    elif 7 <= fishermen <= 11:
        rent *= 0.85
        if fishermen % 2 == 0:
            rent *= 0.95
        else:
            pass
    else:
        rent *= 0.75
        if fishermen % 2 == 0:
            rent *= 0.95
        else:
            pass
elif season == "Summer":
    rent = 4200
    if fishermen <= 6:
        rent *= 0.9
        if fishermen % 2 == 0:
            rent *= 0.95
        else:
            pass
    elif 7 <= fishermen <= 11:
        rent *= 0.85
        if fishermen % 2 == 0:
            rent *= 0.95
        else:
            pass
    else:
        rent *= 0.75
        if fishermen % 2 == 0:
            rent *= 0.95
        else:
            pass
elif season == "Autumn":
    rent = 4200
    if fishermen <= 6:
        rent *= 0.9
    elif 7 <= fishermen <= 11:
        rent *= 0.85
    else:
        rent *= 0.75
elif season == "Winter":
    rent = 2600
    if fishermen <= 6:
        rent *= 0.9
        if fishermen % 2 == 0:
            rent *= 0.95
        else:
            pass
    elif 7 <= fishermen <= 11:
        rent *= 0.85
        if fishermen % 2 == 0:
            rent *= 0.95
        else:
            pass
    else:
        rent *= 0.75
        if fishermen % 2 == 0:
            rent *= 0.95
        else:
            pass
        
diff = abs(budget-rent)

if budget >= rent:
    print(f"Yes! You have {diff:.2f} leva left.")
else:
    print(f"Not enough money! You need {diff:.2f} leva.") 