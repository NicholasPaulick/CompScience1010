x = int(input("Annual expenses: "))
print("")

month = round(x/12, 2)

quarter = round(x/4, 2)

bianually = round(x/2, 2)

print("Monthly Payment: " + str(month))
print("Quarterly Payment: " + str(quarter))
print("Biannually Payment: " + str(bianually))