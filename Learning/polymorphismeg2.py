class shape:
    def area(self):
        return 0

class rectangle(shape):
    def __init__(self, length, width):
        self.length = length
        self.width=width

    def area(self):
        return self.length * self.width
        

box=rectangle(5,6)
print(box.area())  # Output: 30
