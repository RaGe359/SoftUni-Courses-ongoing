price = 7.61

area = int(input())

total_amount = area * price
amount_discounted = total_amount - total_amount*0.18

discount = round(total_amount - amount_discounted, 2)

print(f'The final price is: {amount_discounted} lv.')
print(f'The discount is: {discount} lv')