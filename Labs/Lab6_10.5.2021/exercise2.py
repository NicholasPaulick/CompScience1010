def pig(s):
    words = ""
    for i in s.split():
        words += (i[1:] + i[0] + 'AY ')
    print("Pig Latin:", words)

pig(input("English:"))
