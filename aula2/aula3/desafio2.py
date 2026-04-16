class Equipamento:
    def __init__(self, id_equipamento, nome, preco_diaria):
        self.id_equipamento = id_equipamento
        self.nome = nome
        self.preco_diaria = preco_diaria
        self.status = "Disponível"

    def alugar(self):
        self.status = "Alugado"

    def devolver(self):
        self.status = "Disponível"


class Locadora:
    def __init__(self):
        self.inventario = []
        self.faturamento_por_cliente = {}

    def cadastrar_equipamento(self, equipamento):
        self.inventario.append(equipamento)
        print(f"Equipamento '{equipamento.nome}' cadastrado com sucesso!")

    def realizar_locacao(self, nome_cliente, id_equipamento, dias):
        for eq in self.inventario:
            if eq.id_equipamento == id_equipamento:
                
                if eq.status == "Disponível":
                    eq.alugar()
                    
                    custo_total = eq.preco_diaria * dias
                    
                    if nome_cliente in self.faturamento_por_cliente:
                        self.faturamento_por_cliente[nome_cliente] += custo_total
            
                    else:
                        self.faturamento_por_cliente[nome_cliente] = custo_total
                        
                    print(f"\n[SUCESSO] {nome_cliente} alugou o '{eq.nome}'. Valor: R${custo_total:.2f}")
                    return 
                else:
                    print(f"\n[ERRO] O equipamento '{eq.nome}' já está alugado.")
                    return 
        print(f"\n[ERRO] Equipamento com ID {id_equipamento} não encontrado.")

    def equipamentos_disponiveis(self):
        lista_disponiveis = [eq.nome for eq in self.inventario if eq.status == "Disponível"]
        return lista_disponiveis


# 1. Criando a locadora
minha_locadora = Locadora()

eq1 = Equipamento(101, "Furadeira Makita", 45.0)
eq2 = Equipamento(102, "Betoneira 400L", 120.0)
eq3 = Equipamento(103, "Faca Polishop", 20.0)

print("CADASTRANDO")
minha_locadora.cadastrar_equipamento(eq1)
minha_locadora.cadastrar_equipamento(eq2)
minha_locadora.cadastrar_equipamento(eq3)

print("\nLOCAÇÕES")
minha_locadora.realizar_locacao("Isaqui", 102, 3) 
minha_locadora.realizar_locacao("Isaque", 101, 2)
minha_locadora.realizar_locacao("Isaq", 102, 1)

print("\nRELATÓRIO")
print("Equipamentos que sobraram:", minha_locadora.equipamentos_disponiveis())
print("Faturamento Total:", minha_locadora.faturamento_por_cliente)