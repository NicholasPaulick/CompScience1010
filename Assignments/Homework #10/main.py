Spanish = {}
German = {}
Output = ""

English = input("Please enter English words: ")
English = English.split(",")
SpanishInput = input("Please enter corresponding Spanish translations: ")
SpanishInput = SpanishInput.split(",")
GermainInput = input("Please enter corresponding German translations: ")
GermainInput = GermainInput.split(",")

for index, word in enumerate(English):
    Spanish[English[index]] = SpanishInput[index]
    German[English[index]] = GermainInput[index]
SentenceInput = input("Please input your sentence: ")
SentenceInput = SentenceInput.split(" ")
TargetLanguage = input("Please input target language (spanish/german): ")

if TargetLanguage == "spanish":
    for word in SentenceInput:
        try:
            Output += Spanish[word]
        except KeyError:
            Output += word
        Output += " "
elif TargetLanguage == "german":
    for word in SentenceInput:
        try:
            Output += German[word]
        except KeyError:
            Output += word
        Output += " "
print(Output.strip())
