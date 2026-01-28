a=int(input())
b=int(input())

def add(a,b):
    print("ADDITION-",a+b)
    
def sub(a,b):
    print("SUBTRACTION-",a-b)

def mul(a,b):
    print("MULTIPLICATION-",a*b)

def div(a,b):
    print("DIVISION-",a/b)

op=input()

if(op=="add"):
    add(a,b)
elif(op=="sub"):
    sub(a,b)
elif(op=="mul"):
    mul(a,b)
elif(op=="div"):
    div(a,b)
else:
    print("INVALID OPERATION!")
