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

    def retangulo(self):
        catetos = (self.a ** 2) + (self.b ** 2)
        hipotenusa = self.c ** 2
        if catetos == hipotenusa:
            return True
        else:
            return False

    def semelhantes(self, t):
        ka = self.a / t.a
        kb = self.b / t.b
        kc = self.c / t.c
        if ka == kb and kb == kc and ka == kc:
            return True
        else:
            return False

        
        
'''t1 = Triangulo(2, 2, 2)
t2 = Triangulo(2, 2, 2)
print(t1.a)
print(t2.a)
print(t1.semelhantes(t2))'''