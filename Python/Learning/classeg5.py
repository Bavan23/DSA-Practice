class teacher:
    def __init__(self, name, age, subject):
        self.name = name
        self.age = age
        self.subject = subject
    
    def display(self):
        print(f"The Name of the teacher is {self.name}, the age is {self.age} and the subject she teaches is {self.subject}")

amudha=teacher("Amudha",35,"Maths")
bhuvaneshwari=teacher("Bhuvaneshwari",45,"Tamil")
jennevie=teacher("Jennevie Sharma",50,"English")
sudha=teacher("Sudha",48,"chemistry")

#displaying the details of the teachers
amudha.display()
print("\n")
bhuvaneshwari.display()
print("\n")
jennevie.display()
print("\n")
sudha.display()