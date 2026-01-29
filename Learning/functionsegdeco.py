#assigning a func to an variable
def greet(name):
    print(f"Hello, {name}!")

bavan=greet
print(bavan)  # Output: <function greet at 0x7f9f0
bavan("Bavan")

#Function inside a Function
def outer_function():
    def inner_function():
        print("Hello from inner function")
    inner_function()

outer_function()

#Function as an Arguement
def shout(func):
    def wrapper(*args,**kwargs):
        print("Shouting!!")
        func(*args,**kwargs)
    return wrapper


def greet(name):
    print(f"Hello, {name}!")


greet("Bavan")
shout(greet)("Bavan")
loud=shout(greet)
loud("Bavan")  # Output: Shouting!! Hello, Bavan!