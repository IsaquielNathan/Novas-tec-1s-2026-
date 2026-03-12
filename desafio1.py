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
    "nome": "xiaomi",
    "preco": 1000,
    "quantidade": 50
    
    }


estoque = [mouse, teclado, celular, tablet]
total = 0
for n in estoque:
    total += n["preco"] * "quantidade"