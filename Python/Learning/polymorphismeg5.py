class employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

class manager(employee):
    def __init__(self,name,salary,depat):
        super().__init__(name,salary)
        self.depat=depat

    def display(self):
        print(f"Name: {self.name},Salary: {self.salary},Department: {self.depat}")

emp1=manager("Bavan",1200000,"IT")
emp1.display()