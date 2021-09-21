Students = int(input("How many students do you have?: "))
Tests = int(input("How many tests scores per student?: "))

for s in range(Students):
    StudentAverage = 0
    print("Student #", s+1)
    print("--------------")
    for t in range(Tests):
        Score = int(input("Test #{Number}: ").format(Number = (t+1)))
        StudentAverage += Score
        if t == (Tests-1):
            StudentAverage /= Tests
            print("The average for student #{Number} is: {Average:.1f}".format(Number = (s+1), Average = StudentAverage))
    print("")
