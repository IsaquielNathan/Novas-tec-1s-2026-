mouse =  {
    "nome": "fallen",
    "preco": 200,
    "quantidade": 200
    
    }

teclado =  {
    "nome": "reddragon",
    "preco":300,
    "quantidade": 100
    
    }

celular =  {
    "nome": "rog phone",
    "preco": 800,
    "quantidade": 100
    
    }


tablet =  {
    "nome": "xiaomi-v3",
    "preco": 1000,
    "quantidade": 50
    
    }

mousepad = {
    "nome": "logitech series",
    "preco": 65,
    "quantidade": 0


}    


estoque = [mouse, teclado, celular, tablet, mousepad]
total = 0
caros = []

for n in estoque:
    total += (n["preco"] * n["quantidade"])
    if n["preco"] > 500:
        caros.append(n["nome"])

produtos_zerados = [n["nome"] for n in estoque if n["quantidade"] == 0 ]



print(f"Itens caros da loja : {caros}\n")
print(f"Valor do estoque: {total}\n")
print(f"Sem produto: {produtos_zerados}")