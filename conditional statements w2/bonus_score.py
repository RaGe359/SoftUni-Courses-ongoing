number = int(input())
bonus = 0

if number <= 100:
    bonus = 5
    score = number + bonus
elif 100 < number <= 1000:
    bonus = number * 0.2
    score = number + bonus
elif number > 1000:
    bonus= number * 0.1
    score = number + bonus

if score % 2 == 0:
    extra_bonus = 1
    score = score + extra_bonus
    bonus = bonus + extra_bonus
elif score % 10 == 5:
    extra_bonus = 2
    score = score + extra_bonus
    bonus = bonus + extra_bonus

print(bonus, score)