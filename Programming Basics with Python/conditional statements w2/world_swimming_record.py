import math

record = float(input())
distance_m = float(input())
time_for_m = float(input())

# delay is 12.5 secs per 15 metres
time = distance_m * time_for_m
delay = math.floor(distance_m / 15) * 12.5
total_time = time + delay

if total_time < record:
    print(f'Yes, he succeeded! The new world record is {total_time:.2f} seconds.')
else:
    print(f'No, he failed! He was {total_time-record:.2f} seconds slower.')