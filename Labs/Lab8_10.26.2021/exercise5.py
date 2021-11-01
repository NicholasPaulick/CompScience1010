file = open("random.txt", "r")

total = 0
numbers = 0
for each in file:
    print(each)
    total += each
    numbers += 1

print(numbers)
print(total)