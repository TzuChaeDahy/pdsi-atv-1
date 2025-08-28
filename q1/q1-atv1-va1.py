import cv2
import numpy as np

altura_preta, largura_preta = 28, 28
imagem_preta = np.zeros((altura_preta, largura_preta, 3), dtype=np.uint8)

cv2.imwrite("./q1/imagem_preta_28x28.png", imagem_preta)
print("Imagem preta de 28x28 criada com sucesso como 'imagem_preta_28x28.png'")

altura_azul, largura_azul = 256, 256
imagem_azul = np.zeros((altura_azul, largura_azul, 3), dtype=np.uint8)
cor_azul = [255, 0, 0] 

imagem_azul[:] = cor_azul

cv2.imwrite("q1/imagem_azul_256x256.png", imagem_azul)
print("Imagem azul de 256x256 criada com sucesso como 'imagem_azul_256x256.png'")