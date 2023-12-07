goal = 10000
total_steps = 0

while total_steps < goal:
    steps = input()
    if steps == "Going home":
        steps_to_home = int(input())
        total_steps += steps_to_home
        break

    steps_int = int(steps) 
    total_steps += steps_int

diff = abs(total_steps - goal) 

if total_steps >= goal:
    print(f"Goal reached! Good job!")
    print(f"{diff} steps over the goal!")
elif total_steps < goal:
    print(f"{diff} more steps to reach goal.")