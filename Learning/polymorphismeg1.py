class animal:
    def sound(self):
        print("Animal Makes Sound!")

class dog(animal):
    def sound(self):
        print("Dog Barks!") 

class bird(animal):
    def sound(self):
        print("Bird Chirps!")   

cuckoo=bird()
cuckoo.sound()