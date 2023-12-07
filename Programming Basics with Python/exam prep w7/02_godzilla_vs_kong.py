import math

record_time = float(input())
distance = float(input())
time_per_m = float(input())

slow_factor = math.floor(distance / 50) * 30
time_needed = distance * time_per_m + slow_factor
diff = abs(record_time - time_needed)

if time_needed < record_time:
    print(f"Yes! The new record is {time_needed:.2f} seconds.")
else:
    print(f"No! He was {diff:.2f} seconds slower." )