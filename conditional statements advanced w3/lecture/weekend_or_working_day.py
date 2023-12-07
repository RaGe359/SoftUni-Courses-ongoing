day = input()
list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
list1 = ["Saturday", "Sunday"]

if day in list:
    print("Working day")
elif day in list1:
    print("Weekend")
else:
    print("Error")