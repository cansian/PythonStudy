import random
add_mais = ''
dicionario = {}
count = 0
while add_mais != 'n':
    dicionario[count] = input("Digite o nome do aluno que quer sortear para apagar o quadro, um por vez: ")
    count += 1
    add_mais = input("deseja adicionar mais? (s ou n)")

n = random.randint(0,len(dicionario))
print("O aluno escolhido foi {}".format(dicionario[n]))
