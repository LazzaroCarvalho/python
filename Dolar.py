real = float(input('Quanto você tem em Real Brasileiro? '))
dolar = 5.41

qtd = real / dolar

print('Com R${} você consegue comprar US${:.2f}'. format(real, qtd))
