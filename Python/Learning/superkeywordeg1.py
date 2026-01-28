class shape:
    def __init__(self, color,is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f"Shape with color {self.color} and is_filled {self.is_filled}")

class square(shape):
    def __init__(self, color,is_filled,side_length):
        super().__init__(color,is_filled)
        self.side_length = side_length

    def describe(self):
        print(f"The area of the square is {self.side_length**2}cm")
        super().describe()

sq1=square("red",True,5)
sq1.describe()