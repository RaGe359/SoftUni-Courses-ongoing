floors = int(input())
rooms = int(input())

for x in range(floors, 0, -1):
    for y in range(0, rooms):
        if x == floors:
             if y == rooms - 1:
                 print(f'L{x}{y}')
                 continue
             else:
                print(f'L{x}{y}', end = " ")
                continue           

        if x % 2 == 0 and y != rooms - 1:
            print(f'O{x}{y}', end = " ")
        elif x % 2 == 0 and y == rooms - 1:
            print(f'O{x}{y}')
        
        if x % 2 != 0 and y != rooms - 1:
             print(f'A{x}{y}', end = " ")
        elif x % 2 != 0 and y == rooms - 1:
            print(f'A{x}{y}')