class student:
    def __init__(self):
        self.name = ''
        self.age = 0
        self.register=0

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Register: {self.register}")

ram=student()
ram.name="Ram"
ram.age=20
ram.register=2

ram.display()