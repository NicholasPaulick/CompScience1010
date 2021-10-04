DISCOUNT_PERCENTAGE = 0.2

def get_regular_price():
    return int(input("Enter the item's regular price: "))

def discount(regular, discount):
    print("The sale price is: ${val:.2f}".format(val = regular - (regular * discount)))

regprice = get_regular_price()
discount(regprice, DISCOUNT_PERCENTAGE)
