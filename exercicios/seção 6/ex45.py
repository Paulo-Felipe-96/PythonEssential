res = 'sim'

while res == 'sim':
    n = int(input('Informe um valor de velocidade: '))
    km = n / 3.6
    ms = n * 3.6
    print(f'Velocidades: \n'
          f'Km/h: {km}\n'
          f'M/s: {ms}')
    res = input('Deseja continuar? (sim/não) ')
