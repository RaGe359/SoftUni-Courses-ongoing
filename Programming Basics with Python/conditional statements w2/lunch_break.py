import math

series = input()
runtime = int(input())
break_time = int(input())

lunch = break_time * 1/8
rest = break_time * 1/4

free_time = break_time - lunch - rest
diff = abs(free_time - runtime)
rounded_diff = math.ceil(diff)

if free_time >= runtime:
    print(f"You have enough time to watch {series} and left with {rounded_diff} minutes free time.")
else:
    print(f"You don't have enough time to watch {series}, you need {rounded_diff} more minutes.")