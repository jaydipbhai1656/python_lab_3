class Employee:
    def __init__(self, name, date_of_joining, designation, salary):
        self.name = name
        self.date_of_joining = date_of_joining
        self.designation = designation
        self.salary = salary
    def display_employee_details(self):
        print(f"Employee Name: {self.name}")
        print(f"Date of Joining: {self.date_of_joining}")
        print(f"Designation: {self.designation}")
        print(f"Salary: {self.salary}")
employee = Employee("Karan Rudatala", "2024-03-25", "Software Engineer", 85000)
employee.display_employee_details()