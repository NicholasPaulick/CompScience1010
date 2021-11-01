import random

try:
    file = open("random.txt", "x")
except:
    file = open("random.txt", "w")
numbers = int(input("How many numbers: "))
for _ in range(numbers):
    file.write(str(random.randint(0,500))+"\n")
file.close()