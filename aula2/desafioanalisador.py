frase = input("Digite uma frase: ")
palavras = frase.lower().split()

contagem = {}

for p in palavras:
    if p in contagem:
        contagem[p] += 1
    else:
        contagem[p] = 1

unicas = set(palavras) 
total_unicas = len(unicas)

repetidas = [p for p, qtd in contagem.items() if qtd > 1]

palavra_frequente = ""
maior_frequencia = 0

for p, qtd in contagem.items():
    if qtd > maior_frequencia:
        maior_frequencia = qtd
        palavra_frequente = p

print("\nRelatorio final")
print(f"Total de palavras: {len(palavras)}")
print(f"Palavras únicas: {total_unicas}")
print(f"Palavras repetidas: {repetidas}")
print(f"Palavras frequentes: '{palavra_frequente}' (apareceu {maior_frequencia} vezes)")