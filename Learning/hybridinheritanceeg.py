class dad:
    def money(self):
        print("THis is the money from dad")

class land:
    def land1(self):
        print("This is the land from dad for only son 1")

class son1(dad,land):
    pass
class son2(dad):
    pass
class son3(dad):
    pass

ram=son1()
ram.money()
ram.land1()

sam=son2()
sam.money()
