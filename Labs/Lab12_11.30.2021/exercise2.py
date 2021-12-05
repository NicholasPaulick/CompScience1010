states = ["New York", "Wisconsin", "California", "Texas", "Ohio"]
capitals = ["Albany", "Madison", "Sacramento", "Austin", "Columbus"]
compination = {}

for index, state in enumerate(states):
    compination[state] = capitals[index]

add = input("Would you like to add state and capital to the list: (yes/no) ")
while add.lower() == "yes":
    compination[input("Input the state name: ")] = input("Input the capital name: ")
    add = input("Would you like to add another state and capital (yes/no): ")

for each in compination:
    print(each + " : " + compination[each])