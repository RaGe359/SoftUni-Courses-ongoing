bad_grades_amt = int(input())
bad_grades = 0
sum_grades = 0
problems_amt = 0

while True:
    task_name = input()

    if task_name == "Enough":
        print(f"Average score: {avg_grade:.2f}")
        print(f"Number of problems: {problems_amt}")
        print(f"Last problem: {last_task}")
        break

    grade = int(input())

    if grade <= 4:
        bad_grades += 1

    if bad_grades == bad_grades_amt:
        print(f"You need a break, {bad_grades} poor grades.")
        break
    
    problems_amt += 1
    sum_grades += grade
    avg_grade = sum_grades / problems_amt
    last_task = task_name