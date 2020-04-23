c = 1
n = 1

for i in range(1, 100 + 1, 1):
    print(f'{i}')

print('Fim bloco FOR')

while c != 3:

    while n < 101:
        print(f'{n}')
        n += 1
    n = 0
    c += 1

    print('Fim bloco while')
