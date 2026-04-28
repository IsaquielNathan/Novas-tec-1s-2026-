
import numpy as np

imagem = np.array([
    [200, 180, 160, 140, 120, 100],
    [ 90,  80,  70,  60,  50,  40],
    [255, 240, 210, 190, 170, 150],
    [ 30,  20,  10,   5,   2,   0]
], dtype=np.uint8)

brilho_medio = np.mean(imagem)

media_linhas = np.mean(imagem, axis=1)

media_colunas = np.mean(imagem, axis=0)

linha_escura = np.argmin(media_linhas)

imagem_binaria = (imagem >= 128) * 255

print("Brilho medio:", brilho_medio)
print("Media por linha:", media_linhas)
print("Media por coluna:", media_colunas)
print("Linha mais escura:", linha_escura)
print("\nImagem binaria:", imagem_binaria)