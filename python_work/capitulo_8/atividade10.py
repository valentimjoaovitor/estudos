# atividade 8.10 Enviando mensagens página 193 
lista_de_mensagens = ['bom dia', 'boa noite', 'como vai?', 'dia lindo não?']

def show_messages(assuntos):
    print("\nmensagens que estão na lista")
    for mensagem in assuntos:
        print(mensagem)

def send_messages(assuntos):
    '''Função para mostrar as mensagems que foram enviadas'''
    print('\nAs mensagens enviadas são essas aqui: ')
    mensagens_enviadas = []
    while assuntos:
        mensagem_atual = assuntos.pop()
        mensagens_enviadas.append(mensagem_atual)
    
    print(mensagens_enviadas)


show_messages(lista_de_mensagens)
send_messages(lista_de_mensagens)