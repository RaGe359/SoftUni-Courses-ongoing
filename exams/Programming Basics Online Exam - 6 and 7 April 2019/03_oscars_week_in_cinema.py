movie_name = input()
theater_type = input()
purchased_tickets = int(input())

if movie_name == "A Star Is Born":
    if theater_type == "normal":
        price = 7.50
    elif theater_type == "luxury":
        price = 10.50
    elif theater_type == "ultra luxury":
        price = 13.50
elif movie_name == "Bohemian Rhapsody":
    if theater_type == "normal":
        price = 7.35
    elif theater_type == "luxury":
        price = 9.45
    elif theater_type == "ultra luxury":
        price = 12.75
elif movie_name == "Green Book":
    if theater_type == "normal":
        price = 8.15
    elif theater_type == "luxury":
        price = 10.25
    elif theater_type == "ultra luxury":
        price = 13.25
elif movie_name == "The Favourite":
    if theater_type == "normal":
        price = 8.75
    elif theater_type == "luxury":
        price = 11.55
    elif theater_type == "ultra luxury":
        price = 13.95

income = price * purchased_tickets

print(f"{movie_name} -> {income:.2f} lv.")