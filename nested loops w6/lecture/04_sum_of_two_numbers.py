beg = int(input())
end = int(input())
magic_number = int(input())
comb_num = 0
comb_found = False

for x in range(beg, end+1):
    for y in range(beg, end+1):
        comb_num += 1
        if x + y == magic_number:
            comb_found = True
            break
    if comb_found:
        break

if comb_found:
    print(f"Combination N:{comb_num} ({x} + {y} = {magic_number})")
else:
    print(f"{comb_num} combinations - neither equals {magic_number}")