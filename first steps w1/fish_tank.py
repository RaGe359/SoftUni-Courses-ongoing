length = int(input())
width = int(input())
height = int(input())
percentage = float(input())

volume = length * width * height

volume_litres = volume * 0.001

taken_space = percentage / 100

needed_litres = volume_litres * (1 - taken_space)

print(needed_litres)