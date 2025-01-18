a={
    "Name":"Bavan",
    "Age":19,
    "Year":"2nd Year",
    "Motivated":True,
    "Programming Lang":["C","Pyhton","Javascript"]
    }

print(a)


print(a["Name"])

print(a.keys())
print(a.values())

a["Motivated"]=False
print(a)

a.update({"Motivated":True})
print(a)

a["Status"]="single"
print(a)

#a.clear()
#print(a)

#del a

for i,j in a.items():
    print(i,j)
