replace_list = ["a", "e", "i", "o", "u"]
decryption = {}
actualdecription = {}

for letter in replace_list:
    symbol = input(f"Encrypted symbol for {letter} is: ")
    decryption[letter] = symbol
    actualdecription[symbol] = letter
print("This is your dictionary:",decryption)


encrypted = open("examplefile.txt", "r")
encrypted = encrypted.readline()
print("The encrypted text is:",encrypted)

decripted = ""
for each in encrypted:
    try:
        actualdecription[each]
        decripted += actualdecription[each]
    except KeyError:
        decripted += each
print("The resulting string is:",decripted)
