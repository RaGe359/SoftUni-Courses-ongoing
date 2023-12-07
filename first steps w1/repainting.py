nylon_price_sqm = 1.50
paint_price_lt = 14.50
thinner_price_lt = 5.00

nyLon_amount = int(input())
paint_amount = int(input())
thinner_amount = int(input())
time_needed = int(input())

total_nylon = (nyLon_amount + 2) * nylon_price_sqm
total_paint = (paint_amount + (paint_amount * 0.1)) * paint_price_lt
total_thinner = thinner_amount * thinner_price_lt
total_bags = 0.40
total_materials = total_nylon + total_paint + total_thinner + total_bags
craftsman_price = (total_materials * 0.3) * time_needed

total_expenses = total_materials + craftsman_price

print(total_expenses)