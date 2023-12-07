hour = int(input())
day = input()
list1 = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

if hour in range(10,19) and day in list1:
    print("open")
else:
    print("closed")