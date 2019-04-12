class Triangulo:
    def __init__(self, a,b,c):
        self.a = a
        self.b = b
        self.c = c
    
    def perimetro(self):
        perimetro = self.a + self.b + self.c
        return perimetro

    def tipo_lado(self):
        if self.a != self.b and self.b != self.c and self.a != self.c:
            return "escaleno"
        elif self.a == self.b or self.b == self.c or self.a == self.c:
            if self.a == self.b and self.b == self.c and self.a == self.c:
                return "equilátero"
            return "isósceles"
        
        


'''t = Triangulo(1,1,1)
print(t.a)
print(t.b)
print(t.c)
print(t.perimetro())
print(t.tipo_lado())'''