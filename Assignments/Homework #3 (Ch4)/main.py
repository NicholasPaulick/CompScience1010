# Variables
OPTIONS = ["growth", "decay", "done"]
RUN = ""

# Will ask if you want to growth or decay
while RUN not in OPTIONS:
    RUN = input("Would you like to calculate radioactive growth or decay? ")
    if RUN not in OPTIONS:
        print("Invalid choice! Try again")

# Does the growth function
while RUN in OPTIONS:
    if RUN == "growth":
        # Gets User Input
        GROWTH_RATE = int(input("What's the percent rate of growth? "))
        if GROWTH_RATE <= 0 or GROWTH_RATE > 100:
            print("Error")
            break
        QUANTITY = int(input("What is the initial number of atoms? "))
        TIME = int(input("How much time do you have (in days)? "))

        # Does the Growth Calculation
        for t in range(TIME):
            QUANTITY = QUANTITY + (QUANTITY * (GROWTH_RATE * 0.01))

        # Print Information
        print("The radioactive growth took", str(int(TIME)), "days.")
        print("The number atoms grew to about", str(int(-(-QUANTITY // 1))), "atoms.")

        RUN = ""

    # Does the decay function
    elif RUN == "decay":
        # Gets User Input
        DECAY_RATE = int(input("What is the percent rate of decay? "))
        if DECAY_RATE <= 0 or DECAY_RATE > 100:
            print("Error")
            break
        QUANTITY = int(input("What is the initial number of atoms? "))
        TIME = 0

        # Does the Decay Calculation
        while QUANTITY >= 10:
            QUANTITY = QUANTITY - (QUANTITY * (DECAY_RATE * 0.01))
            TIME += 1

        # Print Information
        print("The radioactive decay took", str(int(TIME)), "days.")
        print("The number atoms decayed to only about", str(int(QUANTITY // 1)), "atoms.")

        RUN = ""

    # Ends the while loop if they enter done
    elif RUN == "done":
        break

    # Allows the user to run the code more than once
    while RUN not in OPTIONS:
        RUN = input("Would you like to calculate radioactive growth or decay again? ")
        if RUN not in OPTIONS:
            print("Invalid choice! Try again")
            # Secondary Check for growth or decay if they enter it wrong last
            while RUN not in OPTIONS:
                RUN = input("Would you like to calculate radioactive growth or decay? ")
                if RUN not in OPTIONS:
                    print("Invalid choice! Try again")
