class person:
    def __init__(self, name):
        self.name = name


class student(person):
    def __init__(self,name,grade):
        super().__init__(name)
        self.grade = grade

    def display(self):
        print(self.grade,self.name)


st1=student("Bavan","A")
st1.display()
