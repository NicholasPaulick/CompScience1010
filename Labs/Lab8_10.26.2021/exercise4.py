file = open("numbers.txt", "r")

total = 0
counter = 0
for each in file:
    total += int(each)
    counter += 1
print(total/counter)