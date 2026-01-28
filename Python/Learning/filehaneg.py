file_path="emplolyee.txt"
employee=["bavan","ram","krushna","sam"]
try:
    with open(file_path,"a") as f:
        for every in employee:
            f.write(every+"\n")
except Exception as e:
    print(e)


try:
    with open(file_path,"r")  as f:
        print(f.read())
except Exception as e:
    print(e)