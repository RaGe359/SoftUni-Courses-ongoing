n = int(input())
wage = int(input())

for _ in range(n):
    name = input()
    
    if name == "Facebook":
        wage -= 150
    elif name == "Instagram":
        wage -= 100
    elif name == "Reddit":
        wage -= 50

    if wage <= 0:
        print("You have lost your salary.")
        break

else:
    print(wage)