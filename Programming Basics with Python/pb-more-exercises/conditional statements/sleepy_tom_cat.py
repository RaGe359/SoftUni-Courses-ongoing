days_off = int(input())

play_norm = 30000
work_days = 365 - days_off
total_play = work_days * 63 + days_off * 127
diff_min = abs(play_norm - total_play)
diff_h = diff_min // 60
diff_m = diff_min % 60

if total_play > play_norm:
    print("Tom will run away")
    print(f'{diff_h} hours and {diff_m} minutes more for play')

if total_play < play_norm:
    print("Tom sleeps well")
    print(f'{diff_h} hours and {diff_m} minutes less for play')  