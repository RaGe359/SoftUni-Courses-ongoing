x = float(input())
y = float(input())
h = float(input())

front_wall = x*x - 1.2*2
back_wall = x*x

frontback_walls = front_wall + back_wall
side_wall_1 = x*y - 1.5*1.5
side_wall_2 = x*y - 1.5*1.5
side_walls = side_wall_1 + side_wall_2
total_walls = frontback_walls + side_walls
green_paint = total_walls / 3.4

roof_1 = 2 * (x*y)
roof_2 = 2 * (0.5 * (x*h))
total_roof = roof_1 + roof_2
red_paint = total_roof / 4.3

print(f'{green_paint:.2f}')
print(f'{red_paint:.2f}')