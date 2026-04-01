transacoes = [
    (1, "Infraestrutura", 1500.50),
    (2, "Licenças", 450.00),
    (3, "Infraestrutura", 3200.00),
    (4, "Marketing", 800.00),
    (5, "Licenças", 150.00)
]
categorias_unicas = set([t[1] for t in transacoes])
print(categorias_unicas)
gastos = {}
for id_transacao, categoria, valor in transacoes:
    if categoria in gastos:
     gastos[categoria] += valor
    else:
        gastos[categoria] = valor
print("\nGastos por Categoria")
print(gastos)

