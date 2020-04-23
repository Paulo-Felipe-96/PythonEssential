pa = float(input('Preço antigo: '))
pn = 0

# Taxação
if pa <= 50:
    pn = pa + (pa * 0.05)
elif pa > 50 and pa <= 100:
    pn = pa + (pa * 0.10)
elif pa > 100:
    pn = pa + (pa * 0.15)

# Nova Tabela
if pn <= 80:
    print(f'Preço novo R${pn} | Barato')
elif pn > 80 and pn <= 120:
    print(f'Preço novo R${pn} | Normal')
elif pn > 120 and pn <= 200:
    print(f'Preço novo R${pn} | Caro')
elif pn > 200:
    print(f'Preço novo R${pn} | Muito caro')
