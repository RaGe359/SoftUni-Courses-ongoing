n = int(input())
is_whole = False

for number in range(1111, 9999+1):
    str_num = str(number)

    for i, digit in enumerate(str_num):
        if int(digit) == 0:
            is_whole = False
            break
        
        result = n/int(digit)
        if result % 1 == 0:
            is_whole = True
        else:
            is_whole = False
            break

    if is_whole:
        print(number, end = ' ')