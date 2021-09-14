# 2. You have been tasked with creating a program that asks the user for the original price of a given item X, Considering it is the test drive phase of the program, the store is offering a 15% discount for all customers who came to the store to purchase item X.
#    Your program will calculate the cost of the item X after the discount, the sales tax associated with the transaction (5.6%) and the final cost of the transaction.
#    The sample output should include the price of item after discount has been applied, the total amount of tax that was due, and the total cost of the transaction.
#    Remember, each of those prices that are being displayed must follow a lead in sentence indicating which number is what:
#       a) The price of item X after discount is: 
# 	    b) The sales tax associated with the transaction is:
# 	    c) The total cost of the transaction is: 

x = int(input("Original Price: "))
print("")

dis = x - (x * 0.15) 

tax = dis * 0.056


print("Cost with discount: " + str(dis))
print("Tax: " + str(tax))
print("Cost of transaction: "+ str(tax + dis))