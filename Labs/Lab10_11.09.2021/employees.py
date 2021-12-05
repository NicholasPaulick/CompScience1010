class Employee():
    def __init__(self, name, id, department, title):
        self.__name = name
        self.__id_number = id
        self.__department = department
        self.__title = title
        
    def get_name(self):
        return self.__name

    def get_id(self):
        return self.__id_number
    
    def get_department(self):
        return self.__department
    
    def get_title(self):
        return self.__title
    
    def __str__(self):
        result = 'Name: ' + self.get_name() + \
            '\nID Number: ' + self.get_id() + \
            '\nDepartnemtn: ' + self.get_department() + \
            '\nTitle ' + self.get_title()
        return result