exam_h = int(input())
exam_m = int(input())
arr_h = int(input())
arr_m = int(input())

min_e = exam_h * 60 + exam_m
min_a = arr_h * 60 + arr_m

if min_a > min_e:
    print("Late")
    diff = min_a - min_e
    if diff < 60:
        print(f"{diff} minutes after the start")
    elif diff >=60:
        late = diff // 60
        late1 = diff % 60
        print(f"{late}:{late1:02d} hours after the start")
elif min_a == min_e:
    print("On time")
elif min_a < min_e:
    diff = min_e - min_a
    if diff <= 30:
        print("On time")
        print(f"{diff} minutes before the start")
    elif 30 < diff < 60:
        early = diff // 60
        early1 = diff % 60
        print("Early")
        print(f"{early1} minutes before the start")
    elif diff >= 60:
        early = diff // 60
        early1 = diff % 60
        print("Early")
        print(f"{early}:{early1:02d} hours before the start")