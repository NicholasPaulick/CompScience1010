class Evaluator():
    # Gets user input and calls the different functions
    def __init__(self):
        self.num1 = int(input("What's the first number? "))
        self.num2 = int(input("What's the second number? "))

        # Gets if specific inputs are 0 to determine if specific outcomes need to happen
        if self.num2 != 0:
            self.dev()
        if self.num2 == 0 or self.num1 == 0:
            self.multiply = 0
        else:
            self.mult()
        if self.num1 == 0 and self.num2 == 0:
            self.result = False
        else:
            self.power()
        self.answer()

    # Does the devision
    def dev(self):
        self.devisor = self.num1
        self.dividend = self.num2
        self.devcount = 0
        while self.devisor >= self.dividend:
            self.devisor -= self.dividend
            self.devcount += 1

    # Does the Multiplication
    def mult(self):
        self.multiply = self.num1
        for _ in range(self.num2 - 1):
            self.multiply += self.num1

    # Does the Exponenets
    def power(self):
        # Gets Multiplication for power
        def multiplyer(num1, num2):
            multiply = num1
            for _ in range(num2 - 1):
                multiply += num1
            return multiply
        self.result = 1
        for _ in range(self.num2):
            self.result = multiplyer(self.result, self.num1)
    
    # Prints out the outcomes is conditions are met
    def answer(self):
        if self.num2 != 0:
            print("These numbers were evenly divided a total of", self.devcount, "times")
            print("This resulted in a remainder of", str(self.devisor))
        else:
            print("Division impossible due to a divide by zero error")
        print("When multiplied together, the total was", self.multiply)
        if self.result != False:
            print("When raised to the given power, the result was", self.result)
        else:
            print("When raised to the given power, the result was undefined")

# Calls the class
if __name__ == "__main__":
    Evaluator()
