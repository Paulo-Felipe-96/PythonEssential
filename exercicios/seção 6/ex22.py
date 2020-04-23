a = 0
b = 0
c = 0
d = 0
mArit = 0

while a < 10 or a > 20 or b < 10 or b > 20 or c < 10 or c > 20 or d < 10 or d > 20:
    a = int(input('A: '))
    b = int(input('B: '))
    c = int(input('C: '))
    d = int(input('D: '))

    if a < 10 or a > 20 or b < 10 or b > 20 or c < 10 or c > 20 or d < 10 or d > 20:
        break
    else:
        mArit = (a + b + c + d) / 4

print(f'Média aritmética: {mArit}')
