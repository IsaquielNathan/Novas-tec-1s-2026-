import numpy as np

notas = np.array([
    [7.5, 8.0, 6.5, 9.0],
    [5.0, 4.5, 6.0, 5.5],
    [9.0, 9.5, 8.5, 10.0],
    [3.0, 4.0, 5.0, 4.5],
    [8.0, 7.5, 9.0, 8.5]
])
#Calculo da nota dos alunos
media = np.mean(notas, axis=1)
maior_media= np.argmax(media)
print ("\nMedia dos alunos:", media)
print ("Maior media:", maior_media )

#Broadcast
m = np.mean(notas, axis = 0)
desvio = np.std(notas, axis = 0)
notas_normalizadas = (notas - m) / desvio
print("\nNotas normalizadas:", notas_normalizadas)

#Aprovados
aprovados = media >= 6.0
print ("\nNotas dos alunos aprovados:", notas [aprovados])
