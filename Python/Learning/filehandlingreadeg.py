try:
    f=open("filehan.txt","r+")
    content=f.read()
    contentfirstline=f.readline()
    print(content)


except Exception as e:
    print("An error occurred: ", e)