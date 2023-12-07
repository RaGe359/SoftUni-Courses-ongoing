price_pens = 5.80
price_markers = 7.20
price_cleaner = 1.20

pens_amount = int(input())
markers_amount = int(input())
cleaner_amount_litres = int(input())
discount_percentage = int(input())

total_pens = pens_amount * price_pens
total_markers = markers_amount * price_markers
total_cleaner = cleaner_amount_litres * price_cleaner
total_all = total_pens + total_markers + total_cleaner
discount = discount_percentage / 100
total_discounted = total_all - (total_all * discount)

print(total_discounted)