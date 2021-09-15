annualsalary = int(input("What is your annual salary?: $"))
yearsemployed = int(input("How many years have you been employed?: "))

if annualsalary >= 45000:
    print("Congratulations, you have satisfied the minimimum wage requirements.")
    if yearsemployed >= 3:
        print("Congratulations, you qualify for the loan.")
    else:
        print("We are sorry, but you must have been working for at least 3 years before we can approve your loan.")
else:
    print("We are sorry, but at this time we are not able to approve your lone application as the required salary is $45000")
