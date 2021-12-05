import random
numbers = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0}

for _ in range(100):
    randomint = random.randint(1, 10)
    numbers[randomint] += 1

for each in numbers:
    print(str(each) + "\t" + str(numbers[each]))