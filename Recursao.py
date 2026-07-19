#Exercicio proposto no CAP3
#chave = 'exemplo para resolver pseudocodigo'
chave = 'Coloque aqui a num da chave correspodente a sua caixa'
def encontrar_chave(num_de_caixas):
    for n in range(0,num_de_caixas+1):
        if chave in n:
            break
        else:
            continue
    return print(f'Chave encontrada na caixa num{n}')
encontrar_chave('Coloque aqui o num de caixas')