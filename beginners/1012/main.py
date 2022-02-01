a, b, c = input().split(" ")
a, b, c = float(a), float(b), float(c)

class shape:
    height = 0
    width = 0
    
    def __init__(self, height = 0, width = 0):
        self.height = height
        self.width = width
    
    def __str__(self) -> str:
        return f"{self.__class__.__name__.upper()}: {self.area:.3f}"
    
    def calculate_area():
        pass

class triangulo(shape):
    def calculate_area(self):
        self.area = (self.height * self.width) / 2
    
class circulo(shape):
    def calculate_area(self):
        self.area = 3.14159 * self.height**2

class trapezio(shape):
    def calculate_area(self):
        self.area = (self.height * self.width) / 2

class quadrado(shape):
    def calculate_area(self):
        self.area = self.height ** 2

class retangulo(shape):
    def calculate_area(self):
        self.area = self.height * self.width

for s in [triangulo(a, c), circulo(c), trapezio((a+b), c), quadrado(b, b), retangulo(a, b)]:
    s.calculate_area()
    print(s)
