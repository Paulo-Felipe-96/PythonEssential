vlr = float(input('Valor do produto R$ '))
uf = input('Estado/UF destino (MG/SP/RJ/MS): ').upper()
vlf = 0

if uf == 'MG':
    vlf = vlr + (vlr * 0.07)
    print(f'Estado/UF MG\n'
          f'Valor original: R${vlr}\n'
          f'Valor + juros de 7%: R${vlf}')
elif uf == 'SP':
    vlf = vlr + (vlr * 0.12)
    print(f'Estado/UF SP\n'
          f'Valor original: R${vlr}\n'
          f'Valor + juros de 12%: R${vlf}')
elif uf == 'RJ':
    vlf = vlr + (vlr * 0.15)
    print(f'Estado/UF RJ\n'
          f'Valor original: R${vlr}\n'
          f'Valor + juros de 15%: R${vlf}')
elif uf == 'MS':
    vlf = vlr + (vlr * 0.08)
    print(f'Estado/UF MS\n'
          f'Valor original: R${vlr}\n'
          f'Valor + juros de 8%: R${vlf}')
