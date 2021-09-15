x = float(input("Please enter your grade score: "))
if x > 100 or x < 0:
    print("The score you input is invalid, the proram will now exit, please try again later.")
else:
    if x >= 95:
        print("Hello, your letter grade in correspondence with your socre is: A+")
    elif x < 95 and x >= 90:
        print("Hello, your letter grade in correspondence with your socre is: A")
    elif x < 90 and x >= 87:
        print("Hello, your letter grade in correspondence with your socre is: B+")
    elif x < 87 and x >= 82:
        print("Hello, your letter grade in correspondence with your socre is: B")
    elif x < 82 and x >= 80:
        print("Hello, your letter grade in correspondence with your socre is: B-")
    elif x < 80 and x >= 75:
        print("Hello, your letter grade in correspondence with your socre is: C+")
    elif x < 75 and x >= 70:
        print("Hello, your letter grade in correspondence with your socre is: C")
    elif x < 70 and x >= 68:
        print("Hello, your letter grade in correspondence with your socre is: D+")
    elif x < 68 and x >= 61:
        print("Hello, your letter grade in correspondence with your socre is: D")
    elif x < 61 and x >= 0:
        print("Hello, your letter grade in correspondence with your socre is: F")