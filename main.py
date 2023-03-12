print('Aumento salarial')

sal = float(input('Digite o seu salário: '))
aum = float(input('Digite o valor do aumento percentual: '))

novosal = sal + (sal * (aum/100))

print('O novo salário é R$ %.2f'%novosal)


