type = input()
rows = int(input())
columns = int(input())
income = 0
cinema_capacity = rows * columns

if type == "Premiere":
    income = cinema_capacity * 12.00
elif type == "Normal":
    income = cinema_capacity * 7.50
elif type == "Discount":
    income = cinema_capacity * 5.00

print(f"{income:.2f}")

# type = input()
# rows = int(input())
# columns = int(input())
# price = 0

# if type == "Premiere":
#     price = 12.00
# elif type == "Normal":
#     price = 7.50
# elif type == "Discount":
#     price = 5.00

# income = (rows * columns) * price
# print(f"{income:.2f}")