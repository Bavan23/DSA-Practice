#Positional Arguements
'''
def add(a,b):
    return a+b
print(add(2,3))
'''
#Default Arguements
'''
def add(a,b=0):
    return a+b
print(add(2))
'''
#Keyword Arguements
'''
def add(a,b):
    return a+b
print(add(b=3,a=2)) #This is the same as add(a=2,b=3)
'''
#Arbitary Arguements

#1) *Args
'''
def add(*args):
    print(args)#stores as a tuple
    return sum(args)
print(add(2,3,4,5,6))
'''
#2) **Kwargs
'''
def add(**kwargs):
    print(kwargs)#stores as a dictionary
    return sum(kwargs.values())
print(add(a=2,b=3,c=4,d=5,e=6))
'''
#3) *Args and **Kwargs
'''
def add(*args,**kwargs):
    print(args)
    print(kwargs)
    return sum(args)+sum(kwargs.values())
print(add(2,3,4,a=5,b=6,c=7))
'''

def shipping_address(*args,**kwargs):
    for name in args:
        print(name,end=" ")
    print()
    for add,val in kwargs.items():
        if "postcode" in kwargs:
            print(f"{add} : {val}")
        else:
            print(kwargs["str"])    

shipping_address("Mr","Bavankalyan","P V",str="313/51",area="Ranga Nagar",city="Hosur",postcode="635109")