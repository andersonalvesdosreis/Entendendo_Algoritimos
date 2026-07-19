#Parte 2 do exe. do CAP3

#Usando Abordagem sem  Recursão:

caixa = 'Somente Exemplo'
chave = 'Somente Exemplo'
def analisar_caixas(caixas):
    while True:
        if caixa in caixas:
            if chave in caixa:
                break
            continue
        elif chave in caixas:
            break
        else:
            continue
    return print('Achei a Chave!')
