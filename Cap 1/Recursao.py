#Exercicio proposto no CAP3

#Tentativa de Resolver o Problema da Caixa:

#chave = 'exemplo para resolver pseudocodigo'
chave = 'Somente Exemplo'
def encontrar_chave(num_de_caixas):
    for n in range(0,num_de_caixas+1):
        if chave in n:
            break
        else:
            continue
    return print(f'Chave encontrada na caixa num{n}')
encontrar_chave('Coloque aqui o num de caixas')