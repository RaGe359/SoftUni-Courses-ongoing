range_beg = input()
range_end = input()

for num1 in range(int(range_beg[0]), int(range_end[0])+1):
    for num2 in range(int(range_beg[1]), int(range_end[1])+1):
        for num3 in range(int(range_beg[2]), int(range_end[2])+1):
            for num4 in range(int(range_beg[3]), int(range_end[3])+1):
                if num1 % 2 != 0 and num2 % 2 != 0 and num3 % 2 != 0 and num4 % 2 != 0:
                    print(f'{num1}{num2}{num3}{num4}', end = " ")