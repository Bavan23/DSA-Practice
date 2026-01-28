class rectangle:
    def __init__(self,width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width
    
    @property
    def height(self):
        return self._height
    
    @width.setter
    def width(self, value):
        if value < 0:
            raise ValueError("Width cannot be negative")
        self._width = value

    @height.setter
    def height(self, value):
        if value<0:
            raise ValueError("Height cannot be negative")
        self._height=value

    @width.deleter
    def width(self):
        del self._width
        print("DELETED WIDTH")

    @property
    def area(self):
        return float(self._width * self._height)
    

r1=rectangle(1,4)
print(r1.width)
print(r1.height)
r1.width=5
print(f"{r1.area:.2f}cm² ")
#del r1.width