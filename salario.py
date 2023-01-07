sal = float(input('Digite seu salário para calcularmos o seu aumento: '))
alm = (sal*25)/100

total = sal + alm
print('Você recebeu um aumento de R${:.2f} para R${:.2f}, obrigado.'.format(sal, total))
