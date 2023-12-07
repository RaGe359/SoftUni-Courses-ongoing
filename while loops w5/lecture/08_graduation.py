name = input()
year = 1
total = 0
fails = 0

while year <= 12:
    grade = float(input())

    if grade >= 4.00 and fails < 2:
        pass
    elif grade < 4.00 and fails == 0:
        fails += 1
        continue
    else:
        print(f"{name} has been excluded at {year} grade")
        exit()

    total += grade
    year += 1

avg_grade = total / 12

print(f"{name} graduated. Average grade: {avg_grade:.2f}")