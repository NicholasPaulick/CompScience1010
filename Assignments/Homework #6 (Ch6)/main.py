file = open("results.txt", "r")

placeholder = []
unusable = 0
for each in file:
    each = each.split(",")
    each[-1] = each[-1].replace("\n", "")
    each[-1] = each[-1].replace(" ", "")
    each = [i for i in each if i != ""]
    placeholder.append(each)

tempcompetitors = []
for each in placeholder:
    if len(each) == 3:
        tempcompetitors.append(each)
    else:
        unusable += 1

competetitors = []
tf = False
for each in tempcompetitors:
    for char in each[2]:
        if char.isalpha() == True:
            tf = True
            break
    if not tf:
        competetitors.append(each)
    else:
        tf = False
        unusable += 1

times = []
for each in competetitors:
    times.append(each[2].split(":"))

# Minutes
min = []
for time in times:
    min.append(int(time[0]))
min = sorted(min)

# Seconds
sec = []
for time in times:
    sec.append(int(time[1]))
sec = sorted(sec)

# Awards
Gold = "a"
Silver = "a"
Bronze = "a"
#Gold
for i, s in enumerate(sec):
    for each in competetitors:
        if each[2].strip() == str(min[0]) + ":" + str(s):
            Gold = each
            competetitors.remove(each)
            break
    if Gold != "a":
        break

#Silver
for i, s in enumerate(sec):
    for each in competetitors:
        if each[2].strip() == str(min[1]) + ":" + str(s):
            Silver = each
            competetitors.remove(each)
            break
    if Silver != "a":
        break

#Bronze
for i, s in enumerate(sec):
    for each in competetitors:
        if each[2].strip() == str(min[2]) + ":" + str(s):
            Bronze = each
            competetitors.remove(each)
            break
    if Bronze != "a":
        break

if Gold != "a":
    print(f"Gold: {Gold[0]} ({Gold[1]}) with a time of {Gold[2]}")
if Silver != "a":
    print(f"Silver: {Silver[0]} ({Silver[1]}) with a time of {Silver[2]}")
if Bronze != "a":
    print(f"Bronze: {Bronze[0]} ({Bronze[1]}) with a time of {Bronze[2]}")
if unusable != 0:
    print(f"There was {unusable} unparseable line(s)!")
