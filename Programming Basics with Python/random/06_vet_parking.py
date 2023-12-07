days = int(input())
hours = int(input())
total_all_days = 0

for d in range(1, days+1):
    total_day = 0
    for h in range(1, hours+1):
        if d % 2 == 0 and h % 2:
            total_day += 2.50
        elif d % 2 and h % 2 == 0:
            total_day += 1.25
        else:
            total_day += 1

    print(f"Day: {d} - {total_day:.2f} leva" )
    total_all_days += total_day

print(f"Total: {total_all_days:.2f} leva")