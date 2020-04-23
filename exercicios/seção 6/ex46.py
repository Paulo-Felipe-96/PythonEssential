import random

n = 0
na = 1
tt = 0

while n != na:
    na = random.randint(1, 1000)
    n = int(input('Número: '))
    tt += 1

    if n > na:
        print(f'O chute é maior que o número gerado! \n'
              f'Resposta certa: {na}')
    elif n < na:
        print(f'O chute é menor que o número gerado! \n'
              f'Resposta certa: {na}')
    elif n == na:
        print(f'Acertou!\n'
              f'Número aleatório: {na} \n'
              f'Número usuário: {n} \n'
              f'Tentativas: {tt} \n'
              f'Fim de jogo!')
