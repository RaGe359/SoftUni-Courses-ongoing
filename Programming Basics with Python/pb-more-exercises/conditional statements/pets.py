import math

days = int(input())
food = int(input())
dog = float(input())
cat = float(input())
turtle = float(input())

total_dog = dog * days
total_cat = cat * days
total_turtle = turtle * days / 1000

total_needed = total_dog + total_cat + total_turtle

diff = abs(food - total_needed)

if food >= total_needed:
    print(f'{math.floor(diff)} kilos of food left.')
else:
    print(f'{math.ceil(diff)} more kilos of food are needed.')