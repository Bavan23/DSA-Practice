class mobile:

    chargertype = "B type"
    
    #instance method/func
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    #class method/func
    @classmethod
    def changechargertype(cls):
        cls.chargertype = "C type"

    #static method/func
    @staticmethod
    def manufacture():
        print("Manufactured By India")

    def display(self):
        print(f"Brand: {self.brand},Model: {self.model},Price: {self.price},ChargerType: {self.chargertype}")

realme=mobile("Realme","Realme 11 Pro",25000)
realme.display()
mobile.changechargertype()
realme.display()
mobile.manufacture()
