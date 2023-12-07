from sys import maxsize

inpt = input()
max_num = -maxsize

while inpt != "Stop":
    number = int(inpt)

    if number > max_num:
        max_num = number

    inpt = input()

print(max_num)
