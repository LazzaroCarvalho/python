prod = float(input('Qual o valor do produto? '))

desc = (prod*5)/100
valor = prod - desc
print('Parabens você recebeu 5% desconto no produto, o produto custava R${:.2f} e agora custa R${:.2f}, foi R${:.2f} '
      'de desconto'.format(prod, valor, desc))