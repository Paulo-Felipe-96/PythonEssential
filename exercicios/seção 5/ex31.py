h = float(input('Informe sua altura: '))
kg = float(input('Informe seu peso: '))

if h < 1.20:
    if kg <= 60:
        print(f'Peso {kg}, Altura {h}\n'
              f'Classe A')
    elif kg > 60 and kg <= 90:
        print(f'Peso {kg}, Altura {h}\n'
              f'Classe D')
    elif kg > 90:
        print(f'Peso {kg}, Altura {h}\n'
              f'Classe G')
elif h >= 1.20 and h <= 1.70:
    if kg <= 60:
        print(f'Peso {kg}, Altura {h}\n'
              f'Classe B')
    elif kg > 60 and kg <= 90:
        print(f'Peso {kg}, Altura {h}\n'
              f'Classe E')
    elif kg > 90:
        print(f'Peso {kg}, Altura {h}\n'
              f'Classe H')
elif h > 1.70:
    if kg <= 60:
        print(f'Peso {kg}, Altura {h}\n'
              f'Classe C')
    elif kg > 60 and kg <= 90:
        print(f'Peso {kg}, Altura {h}\n'
              f'Classe F')
    elif kg > 90:
        print(f'Peso {kg}, Altura {h}\n'
              f'Classe I')
