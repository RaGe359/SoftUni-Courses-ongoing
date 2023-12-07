month = input()
nights = int(input())
price_st = 0
price_ap = 0

if month == "May" or month == "October":
    price_st = nights * 50
    if 7 < nights <= 14:
        price_st *= 0.95
    elif nights > 14:
        price_st *= 0.7
    price_ap = nights * 65
    if nights > 14:
        price_ap *= 0.9
elif month == "June" or month == "September":
    price_st = nights * 75.20
    if nights > 14:
        price_st *= 0.8
    price_ap = nights * 68.70
    if nights > 14:
        price_ap *= 0.9
elif month == "July" or month == "August":
    price_st = nights * 76
    price_ap = nights * 77
    if nights > 14:
        price_ap *= 0.9


print(f"Apartment: {price_ap:.2f} lv.")

print(f"Studio: {price_st:.2f} lv.")