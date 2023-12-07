actor_name = input()
academy_pts = float(input())
jury = int(input())
total_pts = academy_pts

for i in range(jury):
    juror_name = input()
    juror_pts = float(input())

    total_pts += (len(juror_name) * juror_pts / 2)

    if total_pts > 1250.5:
        print(f"Congratulations, {actor_name} got a nominee for leading role with {total_pts:.1f}!")
        break
    
if total_pts <= 1250.5:
    diff = 1250.5 - total_pts
    print(f"Sorry, {actor_name} you need {diff:.1f} more!")