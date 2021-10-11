def Analysis(file):
    Upper = 0
    Lower = 0
    Digits = 0
    Spaces = 0
    for Line in file:
        for Char in Line:
            if Char.isalpha():
                if Char.isupper():
                    Upper += 1
                elif Char.islower():
                    Lower += 1
            elif Char.isnumeric():
                Digits += 1
            elif Char == " ":
                Spaces += 1
    print(f"""
    Uppercase letters: {Upper}
    Lowercase letters: {Lower}
    Digits: {Digits}
    Spaces: {Spaces}
    """)

Analysis(open("text.txt", "r"))