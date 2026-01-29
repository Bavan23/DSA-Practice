from abc import ABC,abstractmethod

class shape:
     @abstractmethod
     def area(self):
          pass
     
class square(shape):
     def __init__(self,side):
          self.side=side
    
     def area(self):
          return self.side**2



class circle(shape):
     def __init__(self,radius):
          self.radius=radius

     def area(self):
          return 3.14*self.radius**2
     
class pizza(circle):
     def __init__(self,radius):
          super().__init__(radius)
          
    


shapes=[square(5),circle(3),pizza(3)]

for shape in shapes:
     print(shape.area())