from math import ceil

height = int(input())
width = int(input())
perc_taken = int(input())

area = ceil(height * width * 4)
percentage = 1 - perc_taken/100
total_paint_needed = area * percentage
painted = 0

litres_paint = input()
while litres_paint != "Tired!":
    painted += int(litres_paint)
    if painted == total_paint_needed:
        print(f"All walls are painted! Great job, Pesho!")
        break
    elif painted > total_paint_needed:
        print(f"All walls are painted and you have {int(painted-total_paint_needed)} l paint left!")
        break

    litres_paint = input()

if litres_paint == "Tired!":
    diff = total_paint_needed - painted
    print(f"{int(diff)} quadratic m left." )