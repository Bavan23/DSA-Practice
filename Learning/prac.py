'''import time

timer=int(input("Enter the time in seconds: "))

for i in range(timer,0,-1):
    sec=i%60
    min=(i//60)%60
    hour=i//3600
    print(f"{hour:02d}:{min:02d}:{sec:02d}")
    time.sleep(1)

print("Time is Up!!!")'''

class calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def add(self):
        print(self.a+self.b)

    def sub(self):
        print(self.a-self.b)
    
    def div(self):
        print(self.a/self.b)

    def mul(self):
        print(self.a*self.b)



a=float(input())
b=float(input())
calc=calculator(a,b)

op=input()

if op=="add":
    calc.add()
elif op=="sub":
    calc.sub()
elif op=='mul':
    calc.mul()
elif op=='div':
    calc.div()