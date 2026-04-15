notas_brutas = [
    {"aluno": "Ana", 
     "materia": "Matematica", 
     "nota": 8.5},
    {"aluno": "Carlos", "materia": "Fisica", "nota": 6.0},
    {"aluno": "Beatriz", "materia": "Quimica", "nota": 9.0},
    {"aluno": "Joao", "materia": "Historia", "nota": 7.5},
    {"aluno": "Mariana", "materia": "Biologia", "nota": 8.0},
    {"aluno": "Pedro", "materia": "Matematica", "nota": 5.5},
    {"aluno": "Lucas", "materia": "Fisica", "nota": 7.0},
    {"aluno": "Julia", "materia": "Quimica", "nota": 6.5},
    {"aluno": "Rafael", "materia": "Historia", "nota": 9.5},
    {"aluno": "Sofia", "materia": "Biologia", "nota": 10.0},
    {"aluno": "Ana", "materia": "Fisica", "nota": 9.0},
    {"aluno": "Carlos", "materia": "Matematica", "nota": 4.5},
    {"aluno": "Beatriz", "materia": "Matematica", "nota": 7.0},
    {"aluno": "Joao", "materia": "Quimica", "nota": 5.0},
    {"aluno": "Mariana", "materia": "Historia", "nota": 8.5},
    {"aluno": "Pedro", "materia": "Biologia", "nota": 6.0},
    {"aluno": "Lucas", "materia": "Matematica", "nota": 8.0},
    {"aluno": "Julia", "materia": "Fisica", "nota": 7.5},
    {"aluno": "Rafael", "materia": "Quimica", "nota": 8.0},
    {"aluno": "Sofia", "materia": "Historia", "nota": 9.0},
    {"aluno": "Ana", "materia": "Matematica", "nota": 7.5},
    {"aluno": "Carlos", "materia": "Fisica", "nota": 3.0},
    {"aluno": "Beatriz", "materia": "Fisica", "nota": 8.0},
    {"aluno": "Joao", "materia": "Matematica", "nota": 6.5},
    {"aluno": "Mariana", "materia": "Quimica", "nota": 9.5},
    {"aluno": "Pedro", "materia": "Historia", "nota": 4.0},
    {"aluno": "Lucas", "materia": "Biologia", "nota": 7.0},
    {"aluno": "Julia", "materia": "Matematica", "nota": 8.5},
    {"aluno": "Rafael", "materia": "Fisica", "nota": 6.0},
    {"aluno": "Sofia", "materia": "Quimica", "nota": 9.5},
    {"aluno": "Ana", "materia": "Matematica", "nota": 4.0},
    {"aluno": "Carlos", "materia": "Matematica", "nota": 5.0},
    {"aluno": "Beatriz", "materia": "Historia", "nota": 7.5},
    {"aluno": "Joao", "materia": "Biologia", "nota": 8.0},
    {"aluno": "Mariana", "materia": "Matematica", "nota": 6.0},
    {"aluno": "Pedro", "materia": "Fisica", "nota": 5.5},
    {"aluno": "Lucas", "materia": "Quimica", "nota": 9.0},
    {"aluno": "Julia", "materia": "Historia", "nota": 8.0},
    {"aluno": "Rafael", "materia": "Biologia", "nota": 7.5},
    {"aluno": "Sofia", "materia": "Matematica", "nota": 10.0},
    {"aluno": "Ana", "materia": "Quimica", "nota": 8.0},
    {"aluno": "Carlos", "materia": "Historia", "nota": 6.5},
    {"aluno": "Beatriz", "materia": "Biologia", "nota": 9.5},
    {"aluno": "Joao", "materia": "Fisica", "nota": 7.0},
    {"aluno": "Mariana", "materia": "Matematica", "nota": 7.5},
    {"aluno": "Pedro", "materia": "Quimica", "nota": 6.0},
    {"aluno": "Lucas", "materia": "Historia", "nota": 8.5},
    {"aluno": "Julia", "materia": "Biologia", "nota": 9.0},
    {"aluno": "Rafael", "materia": "Matematica", "nota": 5.0},
    {"aluno": "Sofia", "materia": "Fisica", "nota": 8.5},
    {"aluno": "Ana", "materia": "Historia", "nota": 9.0},
    {"aluno": "Carlos", "materia": "Biologia", "nota": 5.5},
    {"aluno": "Beatriz", "materia": "Matematica", "nota": 8.5},
    {"aluno": "Joao", "materia": "Quimica", "nota": 6.0},
    {"aluno": "Mariana", "materia": "Fisica", "nota": 8.0},
    {"aluno": "Pedro", "materia": "Historia", "nota": 7.0},
    {"aluno": "Lucas", "materia": "Biologia", "nota": 7.5},
    {"aluno": "Julia", "materia": "Matematica", "nota": 6.5},
    {"aluno": "Rafael", "materia": "Quimica", "nota": 9.0},
    {"aluno": "Sofia", "materia": "Historia", "nota": 10.0},
    {"aluno": "Ana", "materia": "Biologia", "nota": 8.5},
    {"aluno": "Carlos", "materia": "Quimica", "nota": 4.0},
    {"aluno": "Beatriz", "materia": "Fisica", "nota": 7.0},
    {"aluno": "Joao", "materia": "Historia", "nota": 8.5},
    {"aluno": "Mariana", "materia": "Biologia", "nota": 9.0},
    {"aluno": "Pedro", "materia": "Matematica", "nota": 6.5},
    {"aluno": "Lucas", "materia": "Fisica", "nota": 8.0},
    {"aluno": "Julia", "materia": "Quimica", "nota": 7.0},
    {"aluno": "Rafael", "materia": "Historia", "nota": 6.0},
    {"aluno": "Sofia", "materia": "Biologia", "nota": 9.5},
    {"aluno": "Ana", "materia": "Matematica", "nota": 9.5},
    {"aluno": "Carlos", "materia": "Fisica", "nota": 5.0},
    {"aluno": "Beatriz", "materia": "Quimica", "nota": 8.0},
    {"aluno": "Joao", "materia": "Matematica", "nota": 7.0},
    {"aluno": "Mariana", "materia": "Historia", "nota": 8.5},
    {"aluno": "Pedro", "materia": "Biologia", "nota": 5.0},
    {"aluno": "Lucas", "materia": "Matematica", "nota": 9.0},
    {"aluno": "Julia", "materia": "Fisica", "nota": 8.5},
    {"aluno": "Rafael", "materia": "Quimica", "nota": 7.5},
    {"aluno": "Sofia", "materia": "Historia", "nota": 9.0},
    {"aluno": "Ana", "materia": "Fisica", "nota": 8.0},
    {"aluno": "Carlos", "materia": "Matematica", "nota": 6.0},
    {"aluno": "Beatriz", "materia": "Matematica", "nota": 9.0},
    {"aluno": "Joao", "materia": "Quimica", "nota": 5.5},
    {"aluno": "Mariana", "materia": "Fisica", "nota": 7.0},
    {"aluno": "Pedro", "materia": "Historia", "nota": 6.5},
    {"aluno": "Lucas", "materia": "Biologia", "nota": 8.0},
    {"aluno": "Julia", "materia": "Matematica", "nota": 7.5},
    {"aluno": "Rafael", "materia": "Fisica", "nota": 8.0},
    {"aluno": "Sofia", "materia": "Quimica", "nota": 10.0},
    {"aluno": "Ana", "materia": "Quimica", "nota": 9.0},
    {"aluno": "Carlos", "materia": "Historia", "nota": 4.5},
    {"aluno": "Beatriz", "materia": "Biologia", "nota": 8.5},
    {"aluno": "Joao", "materia": "Fisica", "nota": 6.5},
    {"aluno": "Mariana", "materia": "Matematica", "nota": 9.0},
    {"aluno": "Pedro", "materia": "Quimica", "nota": 5.5},
    {"aluno": "Lucas", "materia": "Historia", "nota": 7.0},
    {"aluno": "Julia", "materia": "Biologia", "nota": 8.0},
    {"aluno": "Rafael", "materia": "Matematica", "nota": 6.5},
    {"aluno": "Sofia", "materia": "Fisica", "nota": 9.5}
]



            

rascunho = {}

for aluno_da_vez in notas_brutas:
    nome_do_aluno = aluno_da_vez["aluno"]
    materia = aluno_da_vez["materia"]
    nota = aluno_da_vez["nota"]
    
    
    #aluno novo do dicionario
    if nome_do_aluno  not in rascunho:
        rascunho[nome_do_aluno] = {}
        
    if nome_do_aluno in rascunho:
        if materia not in rascunho[nome_do_aluno]:
            rascunho[nome_do_aluno][materia] = [nota]
            
        elif materia in rascunho[nome_do_aluno]:
            rascunho[nome_do_aluno][materia].append(nota)


#tratar notas Logica central
for nome_do_aluno in rascunho:
    for materia in rascunho[nome_do_aluno]:
        lista_de_notas = rascunho[nome_do_aluno][materia]
        
        while len(lista_de_notas) > 2:
            valor_remover = min(lista_de_notas)
            lista_de_notas.remove(valor_remover)
        rascunho[nome_do_aluno][materia] = lista_de_notas




boletins = {}

for nome_do_aluno in rascunho:
    medias_disciplinas = {}
    lista_medias = []
    for materia in rascunho[nome_do_aluno]:
        notas = rascunho[nome_do_aluno][materia]            
        media = round(sum(notas) / len(notas), 2)
        medias_disciplinas[materia] = media
        lista_medias.append(media)
    media_geral = round(sum(lista_medias) / len(lista_medias), 2) 

    if media_geral >= 7:
        status = "Aprovado"
    elif media_geral >= 5:
        status = "Recuperacao"
    else:
        status = "Reprovado"
    boletins[nome_do_aluno] = {
        "medias_disciplinas": medias_disciplinas,
        "media_geral": media_geral,
        "status": status
    }

print(boletins)
lista_para_ordenar = list(boletins.items())

ranking_completo = sorted(
    lista_para_ordenar, 
    key=lambda x: (-x[1]["media_geral"], x[0])
)

ranking_final = [aluno[0] for aluno in ranking_completo]

# Exibe o resultado final
print("--- RANKING FINAL ---")
print(ranking_final)

