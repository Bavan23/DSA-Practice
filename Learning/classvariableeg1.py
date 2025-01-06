class mobile:

    #class variable - Common for all the objects
    chargertype="C-type"

    #instance variable -  chnages with each and every object
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
    
    def display(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Price: {self.price}, Charger Type: {self.chargertype}")

realme=mobile("Realme","Realme 11 Pro",25000)
realme.display()