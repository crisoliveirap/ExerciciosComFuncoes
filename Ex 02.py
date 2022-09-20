# Mensagens com bordas
def escreva(msg):
    tam = len(msg)
    print('~' * tam)
    print(msg)
    print('~' * tam)


mensagem = str(input('Digite sua mensagem: '))
escreva(mensagem)
