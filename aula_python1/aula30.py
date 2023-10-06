"""
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
"""
velocidade = 60  # velocidade atual do carro
local_carro = 90  # local em que o carro está na estrada

RADAR_1 = 60  # velocidade máxima do radar 1
LOCAL_1 = 100  # local onde o radar 1 está
RADAR_RANGE = 1  # A distância onde o radar pega

if velocidade > RADAR_1:
    print('velocidade carro passou do radar 1')

if local_carro >= (LOCAL_1 - RADAR_RANGE) and \
    local_carro <=(LOCAL_1 + RADAR_RANGE):
    print('carro foi multado em radar 1')