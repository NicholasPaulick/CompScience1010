def translator(num):
    number = ""
    for each in num:
        if each.isnumeric() == True or each == "-":
            number += each
        else:
            each = each.upper()
            if each == "A" or each == "B" or each == "C":
                number += "2"
            elif each == "D" or each == "E" or each == "F":
                number += "3"
            elif each == "G" or each == "H" or each == "I":
                number += "4"
            elif each == "J" or each == "K" or each == "L":
                number += "5"
            elif each == "M" or each == "N" or each == "O":
                number += "6"
            elif each == "P" or each == "Q" or each == "R":
                number += "7"
            elif each == "T" or each == "U" or each == "V":
                number += "8"
            elif each == "W" or each == "X" or each == "Y" or each == "Z":
                number += "9"
    print("The phone number is",number)

translator(input("Enter the telephone number in the format XXX-XXX-XXXX: "))