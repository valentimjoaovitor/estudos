# Atividade 8.11 Mensagens arquivadas página 194
lista_de_mensagens = ['bom dia', 'boa noite', 'como vai?', 'dia lindo não?']

def send_messages(assuntos):
    '''Função para mostrar as mensagems que foram enviadas'''
    print('\nAs mensagens enviadas são essas aqui: ')
    mensagens_enviadas = []
    while assuntos:
        mensagem_atual = assuntos.pop()
        mensagens_enviadas.append(mensagem_atual)
    
    print(mensagens_enviadas)

send_messages(lista_de_mensagens[:])
print('Mensagens arquivadas',lista_de_mensagens)

