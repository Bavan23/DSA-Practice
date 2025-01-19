import random

list=[1,2,3,4,5,6,7]
for i in reversed(list):
    print(i,end=" ")
print()

dict={
    "name":"John",
    "age":30,
    "city":"New York"
    }

dict.update({"name":"bavan"})
print(dict)
dict["post"]="635109"

for key,value in dict.items():
    print(f"{key} = {value}")
