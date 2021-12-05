citys = []
populations = []

current_city = ""
current_population = 192168112
while current_city != "done":
    city = input("What is the name of the city? ")
    if city == "done":
        break
    population = float(input("What's the city's population? (in millions) "))
    citys.append(city)
    populations.append(population)

print("Your list of cities:",citys)
print("Your list of city populations:",populations)

greatest = 000
for each in populations:
    if each > greatest and each != greatest:
        greatest = each
for i, j in enumerate(populations):
    if j == greatest:
        Index = i
        break

print("The city with the greatest population is", citys[Index])
print(f"Its population is {greatest} million")

found = False
for i, j in enumerate(citys):
    if j.lower() == "milwaukee":
        print(f"Milwaukee's population is {populations[i]} million")
        found = True
if not found:
    insert = int(input("Where would you like to insert Milwaukee? "))
    milpop = float(input("What's Milwaukee's population? (in millions) "))
    citys.insert(insert, "Milwaukee")
    populations.insert(insert, milpop)

least = 999999
for each in populations:
    if each <= least:
        least = each
if len(populations) > 1:
    for i, j in enumerate(populations):
        if j == least:
            if citys[i].lower() == "milwaukee":
                careful = True
            citys.pop(i)
            populations.pop(i)
            break

print("Your new list of cities:",citys)
print("Your new list of city populations:",populations)

average = 0
for each in populations:
    average += each
print(f"The average population of these cities is {average/len(populations)} million")

print("Originally, the first city in the list is",citys[0])
print("Its population is",populations[0])
citys.reverse()
populations.reverse()
print("The first city in the new list becomes",citys[0])
print("Its population is",populations[0])
