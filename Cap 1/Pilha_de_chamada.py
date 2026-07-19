#Exe. Extra CAP3

# Pilha de Chamada(Call stack) é um conjunto de sub rotinas empilhadas,
#porém deve se manter o cuidado ao uso pois seu uso indevido pode causar
#o famoso stack overflow.

nome = 'Exemplo de variavel a ser usada'
def saudação(nome):#Função 1
    return print(f'Olá {nome}')

def despedida(nome):#Função 2
    return print(f'Até mais {nome}')

def exemplo_de_pilha(nome):#Função 3 += Função 1+2
    saudação(nome)
    print('Prazer em conheçe-lo')
    despedida(nome)
