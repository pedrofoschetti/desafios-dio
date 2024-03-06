capacidade_atual, aumento_percentual = map(int, input().split())

aumento = (capacidade_atual * aumento_percentual) / 100

nova_capacidade = capacidade_atual + aumento

print(int(nova_capacidade))
