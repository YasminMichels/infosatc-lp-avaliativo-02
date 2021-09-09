#Declaração das primeiras listas solicitadas:
listaA = ["your name","10 coisas que odeio em voce","josee, the tiger and the fish","Marley e eu"]
listaB = ["League of Legends","Omori","Minecraft","Genshin Impact"]
listaC = ["O Ickabog","A viagem de Iris","Os crimes ABC","Ladykillers"]
listaD = ["Volei","Basquete","Dança","Muay Thai"]
#Mostrando as listas ao usuário:>
print("Lista de filmes:", listaA)
print("Lista de jogos:", listaB)
print("Lista de livros:", listaC)
print("Lista de esportes:", listaD)
#Adicionando os novos itens nas listas:
listaA.append("A dama e o Vagabundo")
listaA.append("I want to eat your pancreas")
listaB.append("Final Fantasy XVII")
listaB.append("Life is Strange")
listaC.append("A casa torta")
listaC.append("O homem de giz")
listaD.append("Xadrez")
listaD.append("Futebol")
#Mostrando as listas com os novos itens ao usuário:
print("Nova lista A:",listaA)
print("Nova lista B:",listaB)
print("Nova lista C:",listaC)
print("Nova lista D:",listaD)
#Somando as listas e criando a lista de letra E:
listaE = listaA + listaB +listaC + listaD
#Mostrando a lista nova ao usuário
print("Lista E com as outras listas:", listaE)
#Mostrando a posição de um dos itens da lista de livros:
print("Primeiro item da lista C:",listaA [3])
#Removendo um item da lista de esportes:
listaD.remove("Xadrez")
#Mostrando a lista com o item removido ao usuário:
print("Lista D com item removido: ", listaD)
#Criando a lista de disciplinas: 
listaF = ["História","Matemática","Geografia","Literatura"]
#Mostrando a nova lista de disciplinas ao usuário
print("Lista de disciplinas:",listaF)
#Adicionando a outras listas
listaE = listaA + listaB + listaC + listaD + listaF
#Mostrando a alteração feita na lista E
print("Nova lista E com a lista de disciplinas adicionada:",listaE)