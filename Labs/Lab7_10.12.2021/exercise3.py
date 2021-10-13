score = 0
question_num = 1
student = []

with open("student_solution.txt", "r") as f:
    data = f.readlines()

for _ in range(20):
    student.append(str(input(f"{question_num} A, B, C, D: ")))
    question_num += 1

question_num = 0

for line in data:
    if student[question_num] == str(line.strip()):
        print(line)
        score += 1
        question_num += 1
    else:
        question_num += 1

print(f"Your score is:", score)
if score >= 15:
    print("You passed!")
else:
    print("Try again")
