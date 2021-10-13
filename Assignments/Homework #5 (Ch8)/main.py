def encode():
    Input = input("Please input your sentence: ")
    words = Input.split()
    encoded = ""
    for each in words:
        if each != " ":
            if len(each) > 1:
                encoded += each[1:] + each[0:1] + "ay"
                encoded += " "
            else:
                encoded += each + "ay"
                encoded += ""
    encoded = encoded.strip()
    print(f"The encoded sentence is: {encoded}")

encode()
