def Seperator(string):
    seperate = ""
    charnum = 0
    for Letter in string:
        if charnum != 0:
            if Letter.isupper():
                seperate += " "
            seperate += Letter.lower()
        else:
            seperate += Letter
            charnum += 1
    print(seperate)

Seperator(input("Please enter a sentence: "))
