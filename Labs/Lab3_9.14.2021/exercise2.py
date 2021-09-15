first = int(input("First Grade: "))
second = int(input("Second Grade: "))
third = int(input("Third Grade: "))

average = round((first + second + third)/3)
print("The average score of your tests is:", average)

if average >= 95:
    print("Congratulations on scoring high marks on your exam, welcome to the honors roll!")
else:
    print("You didn't qualify")