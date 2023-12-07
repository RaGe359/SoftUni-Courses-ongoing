b1 = float(input())
b2 = float(input())
h = float(input())

area = (b1 + b2) * h / 2
rounded_area = round(area, 2)

print('{:.2f}'.format(rounded_area))