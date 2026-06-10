print(50 * "=")
print("Question 1: Multiplication Table")
print(50 * "=")

number = int(input("Enter a number to generate its multiplication table: "))
print(f"Multiplication Table for {number}:")
for i in range(1, 11):
    result = number * i
    print(f"{number} x {i} = {result}")

print(50 * "=")
print("Question 2: Count Even Numbers")
print(50 * "=")

print("Even numbers from 1 to 30 are:")
count = 0
for number in range(1, 31):
    if number % 2 == 0:
        print(number)
        count += 1
print(f"\nTotal even numbers: {count}")

print(50 * "=")
print("Question 3: Password Attempts")
print(50 * "=")

correct_password = "python123"
attempts = 0
while attempts < 3:
    user_input = input("Enter the password: ")
    if user_input == correct_password:
        print("Access granted!")
        break
    else:
        attempts += 1
        print(f"Incorrect password. Attempts left: {3 - attempts}")
print("Account locked")

print(50 * "=")
print("Question 4: Calculate Average Marks")
print(50 * "=")

marks_number = int(input("How many marks do you want to enter? "))
total_marks = 0
for i in range(marks_number):
    marks = int(input(f"Enter mark {i + 1}: "))
    total_marks += marks
    
marks_avg = total_marks / marks_number
print(f"Average marks: {marks_avg}")

print(50 * "=")
print("Question 5: Number Guessing Game")
print(50 * "=")

secret_number = 7
while True:
    guess = int(input("Guess the number: "))
    if guess < secret_number:
        print("Too low")
    elif guess > secret_number:
        print("Too high")
    else:
        print("Correct!")
        break

print(50 * "=")
print("Question 6: Simple ATM Menu")
print(50 * "=")

balance = 1000
while True:
    print("\nATM Menu:")
    print("1. Check balance")
    print("2. Deposit money")
    print("3. Withdraw money")
    print("4. Exit")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        print(f"Your current balance is: {balance}")
    elif choice == 2:
        deposit_amount = float(input("Enter the amount to deposit: "))
        balance += deposit_amount
        print(f"{deposit_amount} deposited successfully. New balance: {balance}")
    elif choice == 3:
        withdraw_amount = float(input("Enter the amount to withdraw: "))
        if withdraw_amount > balance:
            print("Insufficient balance.")
        else:
            balance -= withdraw_amount
            print(f"{withdraw_amount} withdrawn successfully. New balance: {balance}")
    elif choice == 4:
        print("Thank youe!")
        break
    else:
        print("Invalid choice. Please try again.")

print(50 * "=")
print("Bonus 1 — Very Advanced Level: Shopping Cart System")
print(50 * "=")

counter = 0
total_cost = 0.0
max_price = None
min_price = None

while True:
    item_price = float(input("Enter item price or 0 to finish: "))

    if item_price == 0:
        break

    total_cost += item_price
    counter += 1

    if max_price is None or item_price > max_price:
        max_price = item_price

    if min_price is None or item_price < min_price:
        min_price = item_price

if counter == 0:
    print("No items were added.")
else:
    price_avg = total_cost / counter

    print(f"Number of items: {counter}")
    print(f"Total price: {total_cost}")
    print(f"Average item price: {price_avg}")
    print(f"Most expensive item: {max_price}")
    print(f"Cheapest item: {min_price}")

print(50 * "=")
print("Bonus 2 — Very Advanced Level: Simple Student Grading System")
print(50 * "=")

students_number = int(input("How many students do you want to enter? "))

counter_passed = 0
counter_failed = 0
highest_avg = 0
top_student = ""

for i in range(students_number):
    student_name = input(f"\nEnter the name of student {i + 1}: ")

    print(f"\nEntering marks for student {student_name}:")
    marks_number = int(input(f"How many marks for {student_name}? "))

    total_marks = 0

    for j in range(marks_number):
        marks = int(input(f"Enter mark {j + 1}: "))
        total_marks += marks

    marks_avg = total_marks / marks_number

    if marks_avg >= 50:
        grade = "Passed"
        counter_passed += 1
    else:
        grade = "Failed"
        counter_failed += 1

    if marks_avg > highest_avg:
        highest_avg = marks_avg
        top_student = student_name

    print(f"\n{student_name}'s average is: {marks_avg}")
    print(f"Result: {grade}")

print("\nSummary:")
print(f"Total students: {students_number}")
print(f"Passed students: {counter_passed}")
print(f"Failed students: {counter_failed}")
print(f"Highest average: {highest_avg}")
print(f"Top student: {top_student}")