print('\033[32mVERIFICANDO A CONSIÇÃO DE EXISTENCIA\033[m')
a = int(input('Digite o lado a do tringulo: '))
b = int(input('Digite o lado b do tringulo: '))
c = int(input('Digite o lado c do tringulo: '))
if abs(b-c) < a and a < (b+c):
    print('A condião de existencia é verdadeira a={}, b={}, c={}'.format(a, b, c))
    if a == b == c:
        print('O triangulo é Equilatero')
    elif a != b != c:
        print('O triangulo é Escaleno')
    else:
        print('O triangulo é Isoceles')
else:
    print('\033[31mEsse triângulo é impossível')
