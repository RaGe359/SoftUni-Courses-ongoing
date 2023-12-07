price_vegetables = float(input())
price_fruits = float(input())
kg_vegetables = int(input())
kg_fruits = int(input())

total_vegetables = price_vegetables * kg_vegetables
total_fruits = price_fruits * kg_fruits

total_bgn = total_vegetables + total_fruits

total_eur = total_bgn / 1.94

print(f'{total_eur:.2f}')