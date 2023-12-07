from sys import maxsize

inpt = input()
min_number = maxsize

while inpt != "Stop":
    number = int(inpt)

    if number < min_number:
        min_number = number

    inpt = input()

print(min_number)