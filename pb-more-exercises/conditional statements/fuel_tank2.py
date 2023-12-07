type = input()
litres = float(input())
card = input()

if type == "Diesel":
    if card == "Yes":
        price = litres * 2.21
        if 20 < litres <= 25:
            price_final = price * 0.92
            print(f'{price_final:.2f} lv.')
        elif litres > 25:
            price_final = price * 0.9
            print(f'{price_final:.2f} lv.')
        else:
            print(f'{price:.2f} lv.')
    elif card == "No":
        price = litres * 2.33
        if 20 < litres <= 25:
            price_final = price * 0.92
            print(f'{price_final:.2f} lv.')
        elif litres > 25:
            price_final = price * 0.9
            print(f'{price_final:.2f} lv.')
        else:
            print(f'{price:.2f} lv.')  
elif type == "Gasoline":
    if card == "Yes":
        price = litres * 2.04
        if 20 < litres <= 25:
            price_final = price * 0.92
            print(f'{price_final:.2f} lv.')
        elif litres > 25:
            price_final = price * 0.9
            print(f'{price_final:.2f} lv.')
        else:
            print(f'{price:.2f} lv.')  
    elif card == "No":
            price = litres * 2.22
            if 20 < litres <= 25:
                price_final = price * 0.92
                print(f'{price_final:.2f} lv.')
            elif litres > 25:
                price_final = price * 0.9
                print(f'{price_final:.2f} lv.')
            else:
                print(f'{price:.2f} lv.')  
elif type == "Gas":
    if card == "Yes":
        price = litres * 0.85
        if 20 < litres <= 25:
            price_final = price * 0.92
            print(f'{price_final:.2f} lv.')
        elif litres > 25:
            price_final = price * 0.9
            print(f'{price_final:.2f} lv.')
        else:
            print(f'{price:.2f} lv.')  
    elif card == "No":
        price = litres * 0.93
        if 20 < litres <= 25:
            price_final = price * 0.92
            print(f'{price_final:.2f} lv.')
        elif litres > 25:
            price_final = price * 0.9
            print(f'{price_final:.2f} lv.')
        else:
            print(f'{price:.2f} lv.')