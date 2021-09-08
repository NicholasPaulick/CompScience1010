x = int(input("Original Price: "))
print("")

dis = x - (x * 0.15) 

tax = dis * 0.056


print("Cost with discount: " + str(dis))
print("Tax: " + str(tax))
print("Cost of transaction: "+ str(tax + dis))