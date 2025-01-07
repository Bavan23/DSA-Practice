class classa:
    def __init__(self):
        print("A")

class classb(classa):
    def __init__(self):
        super().__init__()
        print("B")
        
class classc(classb,classa):
    def __init__(self):
        super().__init__()
        print("C")



ram=classc()