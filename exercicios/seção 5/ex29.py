print('Seja bem-vindo! Aprenderemos a somar números inteiros de 1 até 100.\n'
      'Para isso, precisamos começar com dois número. Digite-os abaixo.')

a = 0
b = 0
ac = 0
er = 0
rc = 0
c = 0

while c < 6:
    a = int(input('Primeiro número: '))
    b = int(input('Segundo número: '))

    rc = a + b
    res = int(input(f'Quanto é {a} + {b}? '))

    if res == rc:
        print(f'Acertou! {a} + {b} = {rc}')
        ac += 1
    else:
        print(f'Errou, mas não desista! {a} + {b} = {rc}')
        er += 1

    c += 1

print(f'Tentativas: {c - 1}\n'
      f'Acertos: {ac}\n'
      f'Erros: {er}')
