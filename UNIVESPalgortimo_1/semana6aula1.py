'''l = ['cão', 'gato', 'peixe']
for c in l:
    print(c)'''
cont = 0
palavra = input('digite a palavra: ')
for c in palavra:
    if c in 'aeiou':
        print(c, end=' ')
        cont += 1
print(cont)
