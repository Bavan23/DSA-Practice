class calculator:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def add(self):
        print(f"Result is {self.a+self.b}")

    def sub(self):
        print(f"Result is {self.a- self.b}")

    def mul(self):
        print(f"Result is {self.a*self.b}")

    def div(self):
        if b != 0:
            print(f"Result is {self.a/self.b}")
        else:
            print("Error! Division by zero is not allowed.")
            
a = int(input("Enter the value of A: "))
b = int(input("Enter the value of B: "))

cal=calculator(a,b)

op=input("Enter the Opertion add/sub/mul/div-").lower()

if(op=="add"):
    cal.add()
elif(op=="sub"):
    cal.sub()
elif(op=="mul"):
    cal.mul()
elif(op=="div"):
    cal.div()
else:
    print("Invalid Operator")