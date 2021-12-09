altura = float(input('Digite sua altura: '))
sexo = str(input('Digite o sexo M ou F: ')).upper().strip()
if sexo == 'M':
    peso = (72.7 * altura) - 58
elif sexo == 'F':
    peso = (62.1 * altura) - 44.7
else:
    print('\033[32mValor invalido!')
print('Seu peso ideal é ', peso)
