try:
  
    f=open("filehan.txt","a")
    f.write("Hello, world!\n")
    f.close()

    w=open("filehan.txt","r")
    print(w.read())

except Exception as e:
    print("An error occurred: ", e)