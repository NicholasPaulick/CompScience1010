class Employee():
    employee_info = {'47899': ['Susan Meyers', 'Accounting', 'President'], '39119': ['Mark Jones', 'IT', 'Programmer'], '81774': ['Joy Rogers', 'Manufacturing', 'Engineer']}
    def __init__(self):
        options = ["search", "add", "remove", "quit"]
        option = ""
        while option != "quit":
            option = input("What would you like to do? (search, add, remove, quit): ")
            while option not in options:
                print("The choice you entered is invalid. Please enter a valid choice: ")
                option = input("What would you like to do? (search, add, remove, quit): ")
            if option == "search":
                id = input("What id would you like to search?: ")
                try:
                    print("Name:",self.employee_info[id][0])
                    print("Department:",self.employee_info[id][1])
                    print("Title:",self.employee_info[id][2])
                except KeyError:
                    print("The specified ID number was not found")
                    
            elif option == "add":
                id = input("What id would you like to add?: ")
                try:
                    self.employee_info[id]
                    print("The employee already exists")
                    print("Updating employee info")
                    del self.employee_info[id]
                    self.employee_info[id] = [input("Name: "), input("Area:"), input("Title: ")]
                except KeyError:
                    self.employee_info[id] = [input("Name: "), input("Area:"), input("Title: ")]
            
            elif option == "remove":
                id = input("What id would you like to remove?: ")
                try:
                    self.employee_info[id]
                    print("Employee deleted")
                    del self.employee_info[id]
                except KeyError:
                    print("Employee not found")
            
            elif option == "quit":
                for id in self.employee_info:
                    print("Name:",self.employee_info[id][0])
                    print("Id:",id)
                    print("Department:",self.employee_info[id][1])
                    print("Title:",self.employee_info[id][2])
                    print("")
                    
Employee()