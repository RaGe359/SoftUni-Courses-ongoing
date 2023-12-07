dog_price = 2.50
cat_price = 4

number_dogs = int(input())
number_cats = int(input())

dog_total = dog_price * number_dogs
cat_total = cat_price * number_cats
total_price = dog_total + cat_total

print(f'{total_price} lv.')