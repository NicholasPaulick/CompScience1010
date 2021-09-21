Investment = int(input("Enter the investment amount: "))
Years = int(input("Enter the number of years: "))
Rate = int(input("Enter the yearly intrest rate in %: "))

print("Year\tBeginBalance\tIntrest\tEnd Balance")

EndBalance = Investment

for y in range(Years):
    BeginBalance = round(EndBalance, 2)
    Intrest = round(BeginBalance * (0.01 * Rate), 2)
    EndBalance = round(BeginBalance + Intrest, 2)
    print("{year}\t{Bal:.2f}\t{Intr}\t{End}".format(year = (y + 1), Bal = BeginBalance, Intr = Intrest, End = EndBalance))