"""
Estruturas condicionais
if, else,elif

if em C
if(ideia < 18) {
    printf("Menor de Idade");
}else{
    printf("Maior de Idade");
}

if em Java
if(ideia < 18) {
    System.out.println("Menor de Idade");
}else{
    System.out.println("Maior de Idade");
}
"""

idade = int(input("Sua idade: "))

if idade < 18:
    print(f'{idade}: menor de idade.')
elif idade == 18 or idade < 22:
    print(f'{idade}: maior de idade.')
else:
    print(f'{idade}: maior de idade e adulto.')
