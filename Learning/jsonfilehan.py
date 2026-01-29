import json

employee={
    "name": "Bavan",
    "age": 19,
    "city": "Hosur",
    "is_manager": False
}

file_path="detail.json"

"""
f=open(file_path,"w")
json.dump(employee,f,indent=4)
print("json file created!")
"""

#or

try:
    with open(file_path,"w") as f:
        json.dump(employee,f,indent=4)
        print("json file created!")
except FileExistsError as e:
    print("file already exists!")

try:
    with open(file_path,"r") as f:
        data=json.load(f)
        print(data)

except Exception:
    print("file not found!")