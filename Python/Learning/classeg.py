class rectangle:
    def __init__(self,width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height
    
    @property
    def width(self):
        return self.width
    
    @property   
    def height(self):
        return self.height
    
    
     
r1=rectangle(4,5)
print(r1.width)
