# Função para Fatorial
def fatorial(n, show=True):
    """
    -> Calcula o Fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostra ou não os cálculos do fatorial.
    :return: O valor do fatorial de um número n.
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(f' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f

# Se colocar show=True, mostra o cálculo completo.
# Se colocar show=False, mostra somente o resultado.


num = int(input('Digite um número para saber seu fatorial: '))
print(fatorial(num, show=False))
help(fatorial)
