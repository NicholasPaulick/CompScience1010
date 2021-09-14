# 4. You have been instructed to create a program that transforms a floating-point value into a currency using the format function within a print statement.
#    Your program will first ask the user for a value, and then display the value that was inputted by the user as a currency with 2 decimal points. 

x = float(input("Enter a value: "))
print("")

print(f"${round(x, 2)}")