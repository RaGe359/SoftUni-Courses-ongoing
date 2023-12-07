import math

mag = int(input())
ziumb = int(input())
rozi = int(input())
kaktusi = int(input())
price = float(input())
# •	Магнолии – 3.25 лева
# •	Зюмбюли – 4 лева
# •	Рози – 3.50 лева
# •	Кактуси – 8 лева
mag_pr = mag * 3.25
ziumb_pr = ziumb * 4
rozi_pr = rozi * 3.50
kaktusi_pr = kaktusi * 8

total_pr = mag_pr + ziumb_pr + rozi_pr + kaktusi_pr
total_final = total_pr * 0.95
diff = abs(price - total_final)

if total_final >= price:
    print(f'She is left with {math.floor(diff)} leva.')
else:
    print(f'She will have to borrow {math.ceil(diff)} leva.')