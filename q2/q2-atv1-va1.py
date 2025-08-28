import cv2
import os

pasta_entrada = 'data'
pasta_saida = 'q2/resultados'

if not os.path.exists(pasta_entrada):
    print(f"Erro: A pasta '{pasta_entrada}' não foi encontrada.")
    print("Por favor, crie a pasta e adicione suas imagens nela.")
    exit()

if not os.path.exists(pasta_saida):
    os.makedirs(pasta_saida)
    print(f"Pasta '{pasta_saida}' criada para salvar os resultados.")

arquivos_na_pasta = os.listdir(pasta_entrada)

print(f"\nIniciando o processamento de {len(arquivos_na_pasta)} arquivo(s) em '{pasta_entrada}'...")

for nome_arquivo in arquivos_na_pasta:
    nome_base = os.path.splitext(nome_arquivo)[0]
    
    caminho_completo_entrada = os.path.join(pasta_entrada, nome_arquivo)
    
    imagem_bgr = cv2.imread(caminho_completo_entrada)
    if imagem_bgr is None:
        print(f"-> Ignorando '{nome_arquivo}', não é um arquivo de imagem válido.")
        continue

    print(f"-> Processando '{nome_arquivo}'...")

    caminho_saida_bgr = os.path.join(pasta_saida, f"{nome_base}_bgr.png")
    cv2.imwrite(caminho_saida_bgr, imagem_bgr)

    imagem_rgb = cv2.cvtColor(imagem_bgr, cv2.COLOR_BGR2RGB)
    caminho_saida_rgb = os.path.join(pasta_saida, f"{nome_base}_rgb.png")
    cv2.imwrite(caminho_saida_rgb, imagem_rgb)

    imagem_cinza = cv2.cvtColor(imagem_bgr, cv2.COLOR_BGR2GRAY)
    caminho_saida_cinza = os.path.join(pasta_saida, f"{nome_base}_gray.png")
    cv2.imwrite(caminho_saida_cinza, imagem_cinza)

print("\nProcessamento concluído com sucesso!")
print(f"Todos os resultados foram salvos na pasta '{pasta_saida}'.")