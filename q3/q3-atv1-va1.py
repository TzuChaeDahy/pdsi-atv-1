import cv2
import os
import random

def recortar_imagem(imagem, x, y, largura, altura):
    imagem_recortada = imagem[y:y+altura, x:x+largura]
    return imagem_recortada

caminho_imagem = os.path.join('data', 'baboon.png')

if not os.path.exists(caminho_imagem):
    print(f"Erro: A imagem '{caminho_imagem}' não foi encontrada.")
    print("Por favor, adicione a imagem na pasta 'data' e tente novamente.")
else:
    imagem_original = cv2.imread(caminho_imagem)

    altura_img, largura_img = imagem_original.shape[:2]

    largura_recorte = random.randint(50, largura_img // 2)
    altura_recorte = random.randint(50, altura_img // 2)

    x_inicial = random.randint(0, largura_img - largura_recorte)
    y_inicial = random.randint(0, altura_img - altura_recorte)

    imagem_final_recortada = recortar_imagem(
        imagem_original, 
        x=x_inicial, 
        y=y_inicial, 
        largura=largura_recorte, 
        altura=altura_recorte
    )

    cv2.imwrite("q3/resultado_recorte.png", imagem_final_recortada)
    print("Imagem recortada com sucesso e salva como 'resultado_recorte.png'")