n1 = int(input('Digite a primeira nota: '))
n2 = int(input('Digite a segunda nota: '))
media = n1 * 0.4 + n2 * 0.6
if media >= 5:
    print('Aluno aprovado ', media)
else:
    print('Aluno \033[31mReprovado', media)
