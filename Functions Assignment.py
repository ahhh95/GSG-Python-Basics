def calculate_final_grade(attendance, homework, quiz, participation):
    final_grade = (
        attendance * 0.20
        + homework * 0.35
        + quiz * 0.35
        + participation * 0.10
    )
    return final_grade


def get_student_status(final_grade, attendance):
    if attendance < 50:
        return "Failed because of low attendance"
    elif final_grade >= 85:
        return "Excellent"
    elif final_grade >= 70:
        return "Good"
    elif final_grade >= 50:
        return "Needs Improvement"
    else:
        return "Failed"


def get_student_advice(attendance, homework, quiz, participation):
    if attendance < 50:
        return "You need to attend more sessions."
    elif homework < 50:
        return "You need to focus more on homework."
    elif quiz < 50:
        return "You need to study more for quizzes."
    elif participation < 50:
        return "Try to participate more during sessions."
    else:
        return "Keep up the good work."


def print_student_report(name, final_grade, status, advice):
    print("------------------------------")
    print("Student Report")
    print(f"Name: {name}")
    print(f"Final Grade: {final_grade:.2f}")
    print(f"Status: {status}")
    print(f"Advice: {advice}")
    print("------------------------------")


def get_valid_score(message):
    while True:
        score = float(input(message))

        if 0 <= score <= 100:
            return score

        print("Invalid score. Please enter a number between 0 and 100.")


def get_valid_students_number():
    while True:
        number = int(input("How many students do you want to evaluate? "))

        if number > 0:
            return number

        print("Invalid number. Please enter a number greater than 0.")


# ---------------- Main Program ----------------

students_number = get_valid_students_number()

excellent_count = 0
good_count = 0
needs_improvement_count = 0
failed_count = 0

total_grades = 0

highest_grade = None
lowest_grade = None

for i in range(students_number):
    print(f"\nStudent {i + 1}")

    student_name = input("Enter student name: ")

    attendance = get_valid_score("Enter attendance score: ")
    homework = get_valid_score("Enter homework score: ")
    quiz = get_valid_score("Enter quiz score: ")
    participation = get_valid_score("Enter participation score: ")

    final_grade = calculate_final_grade(
        attendance,
        homework,
        quiz,
        participation,
    )

    status = get_student_status(final_grade, attendance)

    advice = get_student_advice(
        attendance,
        homework,
        quiz,
        participation,
    )

    print_student_report(
        student_name,
        final_grade,
        status,
        advice,
    )

    total_grades += final_grade

    if highest_grade is None or final_grade > highest_grade:
        highest_grade = final_grade

    if lowest_grade is None or final_grade < lowest_grade:
        lowest_grade = final_grade

    if status == "Excellent":
        excellent_count += 1
    elif status == "Good":
        good_count += 1
    elif status == "Needs Improvement":
        needs_improvement_count += 1
    else:
        failed_count += 1


class_average = total_grades / students_number

print("================================")
print("Final Group Summary")
print(f"Total students: {students_number}")
print(f"Excellent students: {excellent_count}")
print(f"Good students: {good_count}")
print(f"Needs improvement: {needs_improvement_count}")
print(f"Failed students: {failed_count}")
print(f"Class average: {class_average:.2f}")
print(f"Highest grade: {highest_grade:.2f}")
print(f"Lowest grade: {lowest_grade:.2f}")
print("================================")