saved = 0

while True:
    destination = input()
    if destination == "End":
        break

    budget = float(input())

    while True:
        savings = float(input())
        saved += savings

        if saved >= budget:
            print(f'Going to {destination}!')
            saved = 0
            break