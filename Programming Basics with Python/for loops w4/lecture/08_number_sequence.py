from sys import maxsize

n = int(input())
largest = -maxsize
smallest = maxsize

for _ in range(n):
    num = int(input())

    if num > largest:
        largest = num

    if num < smallest:
        smallest = num

print(f'Max number: {largest}')
print(f'Min number: {smallest}')