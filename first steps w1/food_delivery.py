chicken_menu_price = 10.35
fish_menu_price = 12.40
veggie_menu_price = 8.15

chicken_menu_count = int(input())
fish_menu_count = int(input())
veggie_menu_count = int(input())

chicken_menu_total = chicken_menu_count * chicken_menu_price
fish_menu_total = fish_menu_count * fish_menu_price
veggie_menu_total = veggie_menu_count * veggie_menu_price

total_menu_amount = chicken_menu_total + fish_menu_total + veggie_menu_total
dessert = total_menu_amount * 0.2
delivery = 2.50
total_price = total_menu_amount + dessert + delivery

print(total_price)