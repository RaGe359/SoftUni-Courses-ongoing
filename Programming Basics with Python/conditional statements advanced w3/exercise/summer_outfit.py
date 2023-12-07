deg = int(input())
time = input()
outfit = ""
shoes = ""

if time == "Morning":
    if 10 <= deg <= 18:
        outfit = "Sweatshirt"
        shoes = "Sneakers"
    elif 18 < deg <= 24:
        outfit = "Shirt"
        shoes = "Moccasins"
    elif deg >= 25:
        outfit = "T-Shirt"
        shoes = "Sandals"
elif time == "Afternoon":
    if 10 <= deg <= 18:
        outfit = "Shirt"
        shoes = "Moccasins"
    elif 18 < deg <= 24:
        outfit = "T-Shirt"
        shoes = "Sandals"
    elif deg >= 25:
        outfit = "Swim Suit"
        shoes = "Barefoot"
elif time == "Evening":
    if 10 <= deg <= 18:
        outfit = "Shirt"
        shoes = "Moccasins"
    elif 18 < deg <= 24:
        outfit = "Shirt"
        shoes = "Moccasins"
    elif deg >= 25:
        outfit = "Shirt"
        shoes = "Moccasins"

print(f"It's {deg} degrees, get your {outfit} and {shoes}.")