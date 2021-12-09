pets = ['cão', 'gato', 'peixe']
print(pets)
pets[0] = 'coelho'  #adiciona na posição 0
print(pets)
print(pets[-1])  #mostra o ultimo elemento
pets.append('cão')  #adiciona um elemento do final da lista
print(pets)
print(pets.index('gato'))   #retoma a posição do elemento escolhido
pets.insert(1, 'galinha')   #adiciona um elemento na posição escolhida
print(pets)
pets.remove('peixe')    #remove o elemento selecionado da lista
print(pets)
print(pets.pop()) #remove o ultimo elemento da lista
pets.reverse() #inverte os elentos da lista ex: ['a', 'b', 'c'] pets.reverse ['c', 'b', 'a']
print(pets)
pets.sort() #deixa todos os elementos em ordem alfabetica ou numerica dependendo dos elemnetos da lista
print(pets)
