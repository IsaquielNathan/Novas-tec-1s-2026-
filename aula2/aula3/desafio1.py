dados_brutos = [
    {"nome": "Isaquiel Nathan", "email": "isaquiel@gmail.com", "status_ativo": True},
    {"nome": "Natan Isaque", "email": "natan@gmail.com", "status_ativo": True},
    {"nome": "Isaqueu Natael", "email": "nataeuisaqueu@gmail.com", "status_ativo": True},
    {"nome": "Neymar jr", "email": "nj@gmail.com", "status_ativo": False},
    {"nome": "Isaque Silva", "email": "silva@gmail.com", "status_ativo": False}
]


def limpar_dados(lista):
    
   
    usuarios_ativos = list(filter(lambda u: u["status_ativo"] == True, lista))
  
    for usuario in usuarios_ativos:

        usuario["nome"] = usuario["nome"].upper()
        usuario["email"] = usuario["email"].lower()
        
    return usuarios_ativos


dados_higienizados = limpar_dados(dados_brutos)

print("Usuários True")
for d in dados_higienizados:
    print(d)
             