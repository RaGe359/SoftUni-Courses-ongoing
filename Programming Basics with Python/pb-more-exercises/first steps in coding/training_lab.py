w = float(input())
h = float(input())

# if 3 <= h <= w <= 100:
w_cm = w*100
h_cm = h*100
desks = (h_cm - 100) // 70
rows = w_cm // 120
seats = rows * desks - 3
print(int(seats))