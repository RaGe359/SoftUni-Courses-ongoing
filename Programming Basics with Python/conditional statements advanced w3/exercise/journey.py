budget = float(input())
season = input()
destination = ""
type = ""
spent = 0

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        spent = budget * 0.3
        type = "Camp"
    elif season == "winter":
        spent = budget * 0.7
        type = "Hotel"
elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        spent = budget * 0.4
        type = "Camp"
    elif season == "winter":
        spent = budget * 0.8
        type = "Hotel"
else:
    destination = "Europe"
    spent = budget * 0.9
    type = "Hotel"

print("Somewhere in", destination)

print(f"{type} - {spent:.2f}")