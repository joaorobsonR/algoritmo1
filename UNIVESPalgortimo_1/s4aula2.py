ano = input('Digite o ano: ')
mes = input('Digite o mes: ')
dia = input('Digite o dia')
print('{}/{}/{}'.format(dia, mes, ano))
print(dia, mes, ano, sep='/')
print(type(ano))
eval(ano)
print(type(eval(ano)))