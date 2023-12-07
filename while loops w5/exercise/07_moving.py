width = int(input())
length = int(input())
height = int(input())
total_space = width * length * height
space_taken = 0

while True:
    boxes = input()
    if boxes == "Done":
        print(f"{diff} Cubic meters left.")
        break

    boxes = int(boxes)
    space_taken += boxes
    diff = abs(total_space - space_taken)

    if space_taken >= total_space:
        print(f"No more free space! You need {diff} Cubic meters more.")
        break