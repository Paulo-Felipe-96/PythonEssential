sc = float(input('Informe o salário de Carlos R$ '))
pc = round(sc * 0.02, 2)
sj = round(sc / 3, 2)
pj = round(sj * 0.05, 2)

print(f'Salário de Carlos: R${sc}\n'
      f'Poupança de Carlos: R${pc}\n'
      f'Salário de João: R${sj}\n'
      f'Poupanaça de João: R${pj}\n'
      f'Diferença entre os rendimentos: R${round(pc - pj, 2)}')
