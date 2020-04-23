importancia = 780_000
ganhador1 = importancia * 0.46
ganhador2 = importancia * 0.32
ganhador3 = importancia * 0.22
importancia -= ganhador1
importancia -= ganhador2
importancia -= ganhador3
print(f'Ganhador 1: R${ganhador1} \n'
      f'Ganhador 2: R${ganhador2} \n'
      f'Ganhador 3: R${ganhador3} \n'
      f'Saldo final da Importância: R${importancia}')
