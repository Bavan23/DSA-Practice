class student:
    count=0        #class Variable
    total_gpa=0


    #constructor
    def __init__(self,name,gpa): 
        self.name=name      #instance variable
        self.gpa=gpa
        student.count+=1
        student.total_gpa+=gpa

    #instance method
    def display_details(self):
        print("Name:",self.name)
        print("GPA:",self.gpa)


    #class method
    @classmethod
    def get_count(cls):
        return cls.count
    
    @classmethod
    def get_total_gpa(cls):
        return f"{cls.total_gpa/cls.count:.2f}"
    
    #static method
    @staticmethod
    def is_valid_gpa(gpa):
        return gpa>=0 and gpa<=4
     

stu1=student("Bavan",3.5)
stu2=student("Rahul",3.8)
stu3=student("Thila",4)



print(student.get_count())
print(student.get_total_gpa())

print(student.is_valid_gpa(3))  

