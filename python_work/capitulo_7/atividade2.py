'''
7.2 atividade "reservas em restaurante" da página 161
'''

reserva_mesa = input("Quantas mesas o senhor gostaria de reservar? ")
reserva_mesa = int(reserva_mesa)

if reserva_mesa > 8:
    print("Vai ser necessário o senhor aguardar por uma mesa.")

else:
    print("A mesa já está disponível.")