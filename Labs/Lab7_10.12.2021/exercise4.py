square = [[],[],[]]

for r in range(len(square)):
    for c in range(3):
        square[r].insert(c, int(input("Please enter a number (1-9): ")))

for r in square:
    for c in range(3):
        if sum(r) == sum(square[c][c] for c in range(3)):
            if sum(r) == sum(r[c] for r in square):
                answer = "true"
        else:
            answer = "false"

print("The inputs are",answer)