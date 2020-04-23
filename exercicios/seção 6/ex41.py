r1 = 0
r2 = 0

r = 1

while r != 0:
    r1 = int(input('Resistor 1: '))
    r2 = int(input('Resistor 2: '))
    r = (r1 * r2) / (r1 + r2)
    print(f'Resistor: {round(r, 2)}')
