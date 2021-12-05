codes = {"A":"%", "a":"9", "B":"@", "b":"#", "C":"!", "c":"1", "D":"2", "d":"3", "E":"$", "e":"4", "F":"%", "f":"5", "G":"^", "g":"6", "H":"&", "h":"7", "I":"*","i":"8", "J":"(", "j":")", "K":")", "k":"0", "L":"A", "l":"B", "M":"C", "m":"D", "N":"E", "n":"F", "O":"G", "o":"H", "P":"I", "p":"J", "Q":"K", "q":"L", "R":"M", "r":"N", "S":"O", "s":"P", "T":"Q", "t":"R", "U":"S", "u":"T", "V":"U", "v":"V", "W":"a", "w":"X", "X":"Y", "x":"Z","Y":"b", "y":"c", "Z":"x", "z":"d", "1":"e", "2":"f", "3":"g", "4":"h", "5":"i", "6":"j", "7":"k", "8":"l", "9":"m", "0":"n", " ":" ", "'":"'", ".":"."}

def encode():
    text = open("text1.txt", "r")
    text = text.readlines()
    encrypt = open("encrypt.txt", "w")
    for line in text:
        for letter in line.strip():
            if letter not in codes:
                encrypt.write(letter)
            else:
                encrypt.write(codes[letter])
        encrypt.write("\n")

encode()
def decode():
    encrypted = open("encrypt.txt", "r")
    encrypted = encrypted.readlines()
    decrpyted = open("decripyt.txt", "w")
    for line in encrypted:
        for letter in line.strip():
            for each in codes.keys():
                if letter == codes[each]:
                    decrpyted.write(each)
        decrpyted.write("\n")
decode()