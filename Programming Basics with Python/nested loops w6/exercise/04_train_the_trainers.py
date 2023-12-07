jury = int(input())
grades = 0
presentation_counter = 0
total_grades = 0

while True:
    presentation = input()
    if presentation == "Finish":
        break

    for i in range(1, jury+1):
        grade = float(input())
        grades += grade
        avg_grade = grades / jury

    print(f"{presentation} - {avg_grade:.2f}.")
    grades = 0
    presentation_counter += 1
    total_grades += avg_grade

avg_total_grades = total_grades / presentation_counter

print(f"Student's final assessment is {avg_total_grades:.2f}.")