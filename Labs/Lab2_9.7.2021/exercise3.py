# 3. You have been instructed to create a program that calculate the monthly payment that is due for the user. 
#    The program will first ask the user to enter the annual expenses that are responsible for, then the program will calculate the monthly cost, the quarterly cost and the bi-annual cost in which the user must pay and display it on terminal. 

x = int(input("Annual expenses: "))
print("")

month = round(x/12, 2)

quarter = round(x/4, 2)

bianually = round(x/2, 2)

print("Monthly Payment: " + str(month))
print("Quarterly Payment: " + str(quarter))
print("Biannually Payment: " + str(bianually))