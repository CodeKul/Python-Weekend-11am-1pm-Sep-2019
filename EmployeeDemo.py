class Employee:

    def __init__(self, empid, name, salary):
        self.empid = empid
        self.name = name
        self.salary = salary

    def display(self):
        print('ID:', self.empid)
        print('Name:', self.name)
        print('Salary:', self.salary)


class Developer(Employee):
    
    def __init__(self, empid, name, salary, deskid):
        Employee.__init__(self, empid, name, salary)
        self.deskid = deskid

    def display(self):
        Employee.display(self)
        print('Desk id:', self.deskid)

    def build_project(self):
        print('developer is building the project')


class Manager(Employee):

    def __init__(self, empid, name, salary, cabinid):
        Employee.__init__(self, empid, name, salary)
        self.cabinid = cabinid

    def display(self):
        Employee.display(self)
        print('Cabin id:', self.cabinid)

    def release_project(self):
        print('manager is releasing the project')


dev1 = Developer(1, 'ABC', 1000, 10)
dev1.display()
dev1.build_project()

man1 = Manager(3, 'PQR', 3000, 100)
man1.display()
man1.release_project()

emp1 = Employee(2, 'XYZ', 2000)
emp1.display()
emp1.build_project()
emp1.release_project()