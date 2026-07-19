#Parte Final do EXE. do CAP3

#Usando Abordagem com Recursão:

chave = 'Somente Exemplo'
caixa = 'Somente Exemplo'
def analisar_caixa(caixas):
    if caixa in caixas:
        analisar_caixa(caixa)
    elif chave in caixas:
        return print('Achei a Chave!')
    