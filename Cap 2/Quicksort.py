#Exercico proposto no CAP 4

lista = ['Somente Exemplo']
def soma(num1,num2):
    total = num1 + num2
    for n in range(lista):
        soma(total,n)
    return total

#Algoritimo DC(Dividir para Conquistar!)
