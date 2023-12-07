sum_prime = 0
sum_nonprime = 0

while True:
    enter = input()
    if enter == "stop":
        break

    entered = int(enter)
    if entered < 0:
        print("Number is negative.")
        continue

    for i in range(2, entered):
        if entered % i == 0:
            sum_nonprime += entered
            break
    else:
        sum_prime += entered

print(f'Sum of all prime numbers is: {sum_prime}')
print(f'Sum of all non prime numbers is: {sum_nonprime}')