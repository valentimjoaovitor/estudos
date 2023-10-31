'''
Atividade 7.8 Lanchonete: página 172
'''

sandwich_orders = ['xbacon', 'xfrango', 'xsalada', 'xfelicidade']
finished_sandwiches = []

while sandwich_orders:
    finalizado = sandwich_orders.pop(0)
    print(f"seu {finalizado} está pronto")
    finished_sandwiches.append(finalizado)
    
print("\n--- Lanches prontos ---")
for i, lanche in enumerate(finished_sandwiches):
    print(i ,lanche)