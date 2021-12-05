states = ["New York", "Wisconsin", "California", "Texas", "Ohio"]
capitals = ["Albany", "Madison", "Sacramento", "Austin", "Columbus"]
compination = {}

for index, state in enumerate(states):
    compination[state] = capitals[index]
    
print(compination)