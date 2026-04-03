# print ('hello world')

nota_bimestre01 = float(input(f'Digite a nota do Primeiro Bimestre: '))

nota_bimestre02 = float(input(f'Digite a nota do Segundo Bimestre: '))

nota_bimestre03 = float(input(f'Digite a nota do Terceiro Bimestre: '))

nota_bimestre04 = float(input(f'Digite a nota do Quarto Bimestre: '))

soma = (nota_bimestre01 + nota_bimestre02 + nota_bimestre03 + nota_bimestre04)

media = soma / 4

print (f'Para o aluno XPTO, a média anual das notas foi de {media:.2f} com o acumulado de {soma}')
