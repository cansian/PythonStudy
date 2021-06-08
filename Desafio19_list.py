import random
add_mais = ''
lista = []
count = 0
while add_mais != 'n':
    lista.append(input("digite o nome do aluno: "))
    add_mais = input("deseja adicionar mais? (s ou n)")

print("O aluno escolhido foi {}".format(random.choice(lista)))

