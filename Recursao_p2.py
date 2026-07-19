#Parte 2 do exe. do CAP3
caixa = ''
chave = ''
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
