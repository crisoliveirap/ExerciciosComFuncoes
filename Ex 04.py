# Função que descobre qual o maior valor
from time import sleep
# O asterisco indica que podemos colocar quantos parâmetros quisermos


def maior(* num):
    cont = maior = 0
    print('-=' * 30)
    print('\nAnalisando os valores passados...')
    for valor in num:
        print(f'{valor}', end=' ')
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'\nForam informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
