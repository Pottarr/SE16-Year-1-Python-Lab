class Name(object) :
    def __init__(self, title, firstName, lastName) :
        self.setName(self, title, firstName, lastName)
        
    def setName(self, t, f, l) :
        self.title = t
        self.firstName = f
        self.lastName = l
    
    def getFullName(self) :
        fullName = "full name: ", self.title, " ", self.firstName, " ", self.lastName
        
class Date(object) :
    def __init__(self, day, month, year) :
        self.setDate(self, d, m, y)
            
    def setDate(self, d, m, y) :
        if d >= 1 and d <= 31 :
            self.day = d
        else :
            print("Invalid Date")
        if m >= 1 and m <= 12 :
            self.month = m
        else :
            print("Invalid Month")
        self.year = year
        
    def getDate(self) :
        return_date = str(self.day) + "/" + str(self.month) + "/" + str(self.year)
        return return_date
    
    def getDateBC(self) :
        return_date = str(self.day) + "/" + str(self.month) + "/" + str(self.year + 543)
        return return_date
    
class Address(object) :
    def __init__(self, houseNo, street, district, city, country, postcode) :
        self.setAddress(self, houseNo, street, district, city, country, postcode)
        
    def setAddress(self, houseNo, street, district, city, country, postcode) :
        self.houseNo = houseNo
        self.street = street
        self.district = district
        self.city = city
        self.country = country
        self.postcode = postcode
        
    def getAddress(self) :
        return_address = str(self.houseNo) + " " + str(self.street) + " " + str(self.district) + " " + str(self.city) + " " + str(self.country) + " " + str(self.postcode)
        return return_address
    
class Department(object) :
    def __init__(self, description) :
        self.description = description
        self.manager = "No manager"
        self.employeeList = []
        
    def addEmployee(self, e) :
        
        self.employeeList.append(e)
        e.department = self.description
        
    def deleteEmployee(self, e) :
        if e in employeeList :
            employeeList.remove(e)
        else :
            print("Error: Employee not found.")
    
    def setManager(self, e) :
        if e not in employeeList :
            print("Error: Employee not found.")
        elif isinstance(e,TempEmployee) :
            print("Error: Temporary employee cannot be a manager.")
        elif isinstance(e,PermEmployee) :
            self.manager = e.getFullName()
        else :
            print("Error: Unexpected error")
    
    def printInfo(self) :
        print("Department:", self.description)
        print("Manager:", self.manager.getFullName())
        print("Employee List:", self.employeeList)
        
class Person(object) :
    def __init__(self, t, f, l) :
        name = Name(t, f, l)
        self.name = name.getFullName
        
        birthdate = Date(d, m, y)
        self.birthdate = birthdate
        
        address = Address(houseNo, street, district, city, country, postcode)
        self.address= address
        
    def printInfo(self) :
        fullName = self.name.getFullName()
        print(fullName)
        
        birthdate = self.birthdate.getDate()
        print("Birthdate:", birthdate)
        
        address = self.address.getAddress()
        print("Adress:", address)
        
class Employee(Person) :
    def __init__(self, d, m, y) :
        super().__init__()
        
        start_date = Date(d, m, y)
        self.start_date = start_date
        
        self.department = "Unemploy"
        
    def printInfo(self) :
        super().printInfo()
        print("Department:", department)
        
class TempEmployee(Employee) :
    def __init__(self, wage) :
        super().__init__()
        self.wage = wage
        
    def printInfo(self) :
        super().printInfo()
        print("Status: Temporary Employee")
        print("Wage:", wage)
        
class PermEmployee(Employee) :
    def __init__(self, salary) :
        super().__init__()
        self.salary = salary
        
    def printInfo(self) :
        super().printInfo()
        print("Status: Permanent Employee")
        print("Salary:", salary)
        