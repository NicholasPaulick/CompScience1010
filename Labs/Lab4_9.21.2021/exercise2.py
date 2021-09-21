Retail = 2.5

while True:
    Wholesale_Cost = int(input("Enter the item's wholesale cost: "))
    if Wholesale_Cost == 0:
        print("ERROR: the cost of the item cannot be zero")
    elif Wholesale_Cost < 0:
        print("ERROR: The cost of the item cannot be negitive")
    else:
        TotalCost = Wholesale_Cost * Retail
        print("Retail price: ${0:.2f}".format(TotalCost))
        Again = input("Would you like to look for another item? ")
        if Again == "n" or Again == "N":
            print("Thank you for using our price computation system, have a wonderful day")
            break
        else:
            print("You entered an invalid answer, the program will be exiting...")
            break