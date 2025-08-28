# Processamento Digital de Sinais e Imagens - 1ª Atividade (VA1)

- **Aluno:** Vinicius Alves Pacheco
- **Professor:** Edvonaldo Horácio dos Santos
- **Disciplina:** Processamento Digital de Sinais e Imagens
- **Período:** 6º

---

## 📝 Descrição do Projeto

Este repositório contém a resolução da primeira atividade avaliativa da disciplina de Processamento Digital de Sinais e Imagens. Os scripts foram desenvolvidos em Python utilizando a biblioteca OpenCV para manipulação e processamento de imagens, abordando tarefas como criação, conversão de cores e recorte de imagens.

## 🛠️ Pré-requisitos

Antes de começar, certifique-se de que você tem os seguintes softwares instalados em sua máquina:

- [Python](https://www.python.org/downloads/) (versão 3.8 ou superior)
- [Git](https://git-scm.com/downloads/)

## 🚀 Como Configurar e Rodar o Projeto

Siga os passos abaixo para configurar o ambiente e executar os scripts.

### 1. Clonar o Repositório

Abra seu terminal ou Git Bash e clone este repositório para a sua máquina local:

```bash
git clone https://github.com/TzuChaeDahy/pdsi-atv-1

cd pdsi-atv-1
```

### 2. Criar e Ativar o Ambiente Virtual

É uma boa prática usar um ambiente virtual para isolar as dependências do projeto.

```bash
# Criar o ambiente virtual (a pasta 'venv' será criada)

python -m venv venv
```

Agora, ative o ambiente:

- **No Windows (PowerShell/CMD):**
  ```bash
  
  .\venv\Scripts\activate
  ```

- **No macOS ou Linux:**
  ```bash
  source venv/bin/activate
  ```

### 3. Instalar as Dependências

Com o ambiente virtual ativado, instale todas as bibliotecas necessárias usando o arquivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 4. Executando os Scripts

Cada questão da atividade possui um script correspondente. Execute-os a partir da pasta raiz do projeto.

#### **Questão 1: Criação de Imagens**

Este script cria duas novas imagens: uma preta (28x28) e uma azul (256x256).

```bash
python q1/q1-atv1-va1.py
```

- **Resultado:** Os arquivos `imagem_preta_28x28.png` e `imagem_azul_256x256.png` serão gerados.

#### **Questão 2: Carregamento e Conversão de Imagens**

Este script lê todas as imagens da pasta `data/`, converte cada uma para os formatos BGR, RGB e tons de cinza, e salva os resultados em uma nova pasta.

```bash
python q2/q2-atv1-va1.py
```

- **Resultado:** Uma nova pasta chamada `resultados/` será criada com todas as imagens processadas.

#### **Questão 3: Recorte de Imagem**

Este script carrega a imagem `baboon.png` da pasta `data/`, recorta uma sub-região aleatória e salva o resultado.

```bash
python q3/q3-atv1-va1.py
```
