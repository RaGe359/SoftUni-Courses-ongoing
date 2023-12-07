puzzle = 2.60
doll = 3
bear = 4.10
minion = 8.20
truck = 2

excursion_price = float(input())
puzzle_amt = int(input())
doll_amt = int(input())
bear_amt = int(input())
minion_amt = int(input())
truck_amt = int(input())

total_toys_amt = puzzle_amt + doll_amt + bear_amt + minion_amt + truck_amt

total_puzzle = puzzle_amt * puzzle
total_doll = doll_amt * doll
total_bear = bear_amt * bear
total_minion = minion_amt * minion
total_truck = truck_amt * truck

total_toys_price = total_puzzle + total_doll + total_bear + total_minion + total_truck

if total_toys_amt >= 50:
    total_toys_price = total_toys_price * 0.75

total_toys_price = total_toys_price * 0.9

if total_toys_price >= excursion_price:
    print(f'Yes! {total_toys_price - excursion_price:.2f} lv left.')
else:
    print(f'Not enough money! {abs(total_toys_price - excursion_price):.2f} lv needed.')

