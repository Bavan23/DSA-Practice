const_username="bavan"
const_password="bavan.2312"

uname=input()
password=input()

def validate():
    if uname==const_username and password==const_password:
        return True
    else:
        return False
    
a=validate()
print(a)