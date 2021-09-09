item1 = input("Digite o nome de uma cor:")
item2 = input("Digite o nome de uma cor:")
item3 = input("Digite o nome de uma cor:")
item4 = input("Digite o nome de uma cor:")
listacor = [item1,item2,item3,item4]
print(listacor)
verificar = input("Qual item deseja verificar? ")
if verificar in listacor:
    print("Sim, está na lista.")
else:
    print("Não está na lista.")