n1 = int(input())
n2 = int(input())
n3 = int(input())
is_prime = False
count = 0

for i in range(1, n1+1):
    for j in range(1, n2+1):
        for k in range(1, n3+1):
            for prime in range(1, j+1):
                if j % prime == 0:
                    count += 1

            if count == 2:
                is_prime = True

            if i % 2 == 0 and is_prime == True and k % 2 == 0:
                print(f'{i} {j} {k}')
            
            count = 0
            is_prime = False