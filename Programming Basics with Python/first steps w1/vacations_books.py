book_pages = int(input())
pages_per_hpur = int(input())
days_needed = int(input())

total_time = book_pages // pages_per_hpur
time_per_day = total_time // days_needed

print(time_per_day)