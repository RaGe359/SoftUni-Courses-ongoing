kms = int(input())
tod = input()

if kms < 20:
    if tod == "day":
        price = 0.7 + kms * 0.79
        print(f'{price:.2f}')
    else:
        price = 0.7 + kms * 0.90
        print(f'{price:.2f}')
elif 20 <= kms < 100:
    price = kms * 0.09
    print(f'{price:.2f}')
else:
    price = kms * 0.06
    print(f'{price:.2f}')