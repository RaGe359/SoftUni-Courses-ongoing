a = float(input())
h = float(input())

area = a * h / 2
area_rounded = round(area, 2)

print('{:.2f}'.format(area_rounded))