def maiusculas(frase):
    letras_maiusculas = ""
    for i in range(len(frase)):
        if ord(frase[i]) >= 65 and ord(frase[i]) <= 90:
            letras_maiusculas += frase[i]
    return letras_maiusculas


frase = "Programamos em python 2?"
frase2 = 'Programamos em Python 3.'
frase3 = 'PrOgRaMaMoS em python!'
frase4 = 'Programamos em Python 3'
frase5 = 'oi, Daniela e David'

print(maiusculas(frase))
print(maiusculas(frase2))
print(maiusculas(frase3))
print(maiusculas(frase4))
print(maiusculas(frase5))


