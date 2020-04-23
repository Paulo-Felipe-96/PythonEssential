a = float(input('Lado A: '))
b = float(input('Lado B: '))
c = float(input('Lado C: '))

if a < (b + c) and b < (a + c) and c < (a + b):
    if a == b and b == c:
        print('Triangulo equilátero')
    elif a != b and b != c and a != c:
        print('Triangulo escaleno')
    else:
        print('Triangulo isósceles')
else:
    print('Impossível formar um triangulo')
