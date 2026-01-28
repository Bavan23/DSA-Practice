username = input("Enter your username: ")

if len(username)>12:
    print("Username is too long. Please choose a shorter username.")
elif not username.find(" ")==-1:
    print("Username cannot contain spaces. Please choose a different username.")
elif not username.isalpha():
    print("Username can only contain letters. Please choose a different username.")
else:
    print(f"WELCOME {username}")
