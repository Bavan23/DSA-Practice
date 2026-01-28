#for logging
def logging(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with arguments {args} and keyword arguments {kwargs}")
        func(*args, **kwargs)
    return wrapper

@logging
def say_hello(name):
    print(f"Hello, {name}!")

say_hello("Bavan")


#for authencation
def req_login(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with arguments {args} and keyword arguments {kwargs}")
        if not user.get("is_login"):
            print("please Login First!!")
            return
        return func(*args, **kwargs)
    return wrapper

@req_login
def welcome(*args, **kwargs):
    print(f"Welcome, {user["name"]}!")


user={"name":"Bavan","is_login":True}
welcome(user)


