class grandpa:
    def money(self):
        print("This the money given by grandpa")

class father:
    def phone(self):
        print ("this is the phone from dad")

class son(father,grandpa):
    def lap(self):
        print("This is the lap from son")

ram=son()
ram.phone()
ram.money()