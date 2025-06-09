# Aplicação Python ChatGPT

Esta é uma aplicação Python simples que interage com o ChatGPT usando um prompt fixo. A aplicação está containerizada usando Docker.

## Pré-requisitos

- Python 3.9 ou superior
- Docker instalado no seu sistema
- Chave de API da OpenAI
- Conta no Docker Hub (para CI/CD)

## Configuração do Ambiente

### 1. Configuração Local

1. Clone o repositório:
```bash
git clone [URL_DO_REPOSITÓRIO]
cd [NOME_DO_DIRETÓRIO]
```

2. Crie e ative um ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
.\venv\Scripts\activate  # Windows
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

### 2. Configuração do Docker Hub

1. Crie uma conta no Docker Hub (se ainda não tiver):
   - Acesse https://hub.docker.com/
   - Clique em "Sign Up" e siga as instruções

2. Crie um token de acesso:
   - Faça login no Docker Hub
   - Vá em "Account Settings" > "Security"
   - Clique em "New Access Token"
   - Dê um nome ao token (ex: "github-actions")
   - Copie o token gerado

3. Configure os secrets no GitHub:
   - Vá para seu repositório no GitHub
   - Clique em "Settings" > "Secrets and variables" > "Actions"
   - Adicione os seguintes secrets:
     - `DOCKER_USERNAME`: seu nome de usuário do Docker Hub
     - `DOCKER_PASSWORD`: seu token de acesso do Docker Hub

## Como Executar

### Executando Localmente

1. Configure sua chave da OpenAI:
```bash
export OPENAI_API_KEY="sua_chave_api_aqui"
```

2. Execute o script:
```bash
python app.py
```

### Executando com Docker

1. Construa a imagem Docker:
```bash
docker build -t chatgpt-app .
```

2. Execute o container:
```bash
docker run -e OPENAI_API_KEY="sua_chave_api_aqui" chatgpt-app
```

## Personalizando o Prompt

Para alterar o prompt, modifique a variável `prompt` no arquivo `app.py`:

```python
def get_chatgpt_response():
    prompt = "Seu novo prompt aqui"
    # ... resto do código
```

## Pipeline CI/CD

Este projeto inclui um workflow do GitHub Actions que:

1. Valida o código usando flake8
2. Constrói a imagem Docker
3. Publica a imagem no Docker Hub

O workflow é executado automaticamente em:
- Push para a branch main
- Pull requests para a branch main

### Acessando a Imagem do Container

Após uma execução bem-sucedida do workflow, você pode baixar a imagem do Docker Hub:

```bash
docker pull seu_usuario/chatgpt-app:latest
```

## Solução de Problemas

### Erro de Autenticação
- Verifique se sua chave da OpenAI está correta
- Certifique-se de que a chave está sendo passada corretamente como variável de ambiente

### Erro no Docker Hub
- Verifique se as credenciais do Docker Hub estão configuradas corretamente nos secrets do GitHub
- Confirme se o token de acesso do Docker Hub é válido

## Contribuindo

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/nova-feature`)
5. Abra um Pull Request
