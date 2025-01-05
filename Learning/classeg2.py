class laptop:
    price=""
    processor=""
    RAM=""
    storage=""

hp=laptop()
lenovo=laptop()
dell=laptop()

hp.price=int(input("Price for HP- "))
hp.processor=input("Processor for HP- ")
hp.RAM=input("RAM of HP- ")
hp.storage=input("Storage for HP- ")

dell.price=int(input("Price for dell- "))
dell.processor=input("Processor for dell- ")
dell.RAM=input("RAM for Dell- ")
dell.storage=input("Storage for Dell- ")

lenovo.price=int(input("Price for lenovo- "))
lenovo.processor=input("Processor for lenovo- ")
lenovo.RAM=input("RAM for lenovo- ")
lenovo.storage=input("Storage for Lenovo- ")

print("DETAILS=")

print("1)HP- Price:",hp.price,",Processor:",hp.processor+" ,RAM:",hp.RAM+" ,Storage:",hp.storage)
print("2)HP- Price:",dell.price,",Processor:",dell.processor+" ,RAM:",dell.RAM+" ,Storage:",dell.storage)
print("3)HP- Price:",lenovo.price,",Processor:",lenovo.processor+" ,RAM:",lenovo.RAM+" ,Storage:",lenovo.storage)








'''

class Laptop:
    def __init__(self, price, processor, RAM, storage):
        self.price = price
        self.processor = processor
        self.RAM = RAM
        self.storage = storage

# Creating objects for different laptops
hp = Laptop(
    int(input("Price for HP: ")),
    input("Processor for HP: "),
    input("RAM for HP: "),
    input("Storage for HP: ")
)

dell = Laptop(
    int(input("Price for Dell: ")),
    input("Processor for Dell: "),
    input("RAM for Dell: "),
    input("Storage for Dell: ")
)

lenovo = Laptop(
    int(input("Price for Lenovo: ")),
    input("Processor for Lenovo: "),
    input("RAM for Lenovo: "),
    input("Storage for Lenovo: ")
)

# Printing the details
print("\nDETAILS:")
print(f"1) HP - Price: {hp.price}, Processor: {hp.processor}, RAM: {hp.RAM}, Storage: {hp.storage}")
print(f"2) Dell - Price: {dell.price}, Processor: {dell.processor}, RAM: {dell.RAM}, Storage: {dell.storage}")
print(f"3) Lenovo - Price: {lenovo.price}, Processor: {lenovo.processor}, RAM: {lenovo.RAM}, Storage: {lenovo.storage}")

'''