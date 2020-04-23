totVendas = float(input('Informe o valor total das vendas: '))
totPagar = totVendas - (totVendas * 0.10)
parce3 = totPagar / 3
cva = totPagar * 0.05
cvp = totVendas * 0.05
print(f'Total a pagar com 10% de desconto R${totPagar} \n'
      f'Parcelamento em 3x R${parce3} \n'
      f'Comissão venda a vista R${cva} \n'
      f'Comissão venda parcelada R${cvp}')
