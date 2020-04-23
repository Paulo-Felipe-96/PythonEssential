km = float(input('Quilômetros percorridos Km: '))
lt = float(input('Quantidade de combustível consumido em Litros: '))
con = km / lt

if con < 8:
    print(f'{con}, venda o carro!')
elif 8 <= con <= 14:
    print(f'{con}, econômico!')
elif con > 14:
    print(f'{con}, supereconômico!')
