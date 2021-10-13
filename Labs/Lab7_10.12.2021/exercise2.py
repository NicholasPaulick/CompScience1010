numbers = []

for e in range(20):
    numbers.append(int(input(f"Please enter the {e + 1}st number: ")))

numbers.sort()
length = len(numbers)
print(f"Lowest: {numbers[0]}")
print(f"Highest: {numbers[length-1]}")

t = 0
for e in numbers:
    t += e
print(f"Total:",t)
print(f"Average:", t/length)