import math

shape = input()

if shape.lower() == "square":
    sq = float(input())
    sq_area = sq * sq
    print(f"{sq_area:.3f}")
elif shape.lower() == "rectangle":
    rec_side1 = float(input())
    rec_side2 = float(input())
    rec_area = rec_side1 * rec_side2
    print(f"{rec_area:.3f}")
elif shape.lower() == "circle":
    cir = float(input())
    cir_area = math.pi * cir**2
    print(f"{cir_area:.3f}")
elif shape.lower() == "triangle":
    tri_1 = float(input())
    tri_2 = float(input())
    tri_area = tri_1 * tri_2 / 2
    print(f"{tri_area:.3f}")