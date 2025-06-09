# Aplicação Python ChatGPT

Esta é uma aplicação Python simples que interage com o ChatGPT usando um prompt fixo. A aplicação está containerizada usando Docker.

## Pré-requisitos

- Docker instalado no seu sistema
- Chave de API da OpenAI
- Conta no Docker Hub (para CI/CD)

## Como Executar

1. Construa a imagem Docker:
```bash
docker build -t chatgpt-app .
```

2. Execute o container com sua chave de API da OpenAI:
```bash
docker run -e OPENAI_API_KEY=sua_chave_api_aqui chatgpt-app
```

Substitua `sua_chave_api_aqui` pela sua chave de API real da OpenAI.

## Personalizando o Prompt

Para alterar o prompt, modifique a variável `prompt` no arquivo `app.py` e reconstrua a imagem Docker.

## Pipeline CI/CD

Este projeto inclui um workflow do GitHub Actions que:

1. Valida o código usando flake8
2. Constrói a imagem Docker
3. Publica a imagem no Docker Hub

O workflow é executado em:
- Push para a branch main
- Pull requests para a branch main

### Configuração do CI/CD

Para que o pipeline funcione corretamente, você precisa configurar os seguintes secrets no seu repositório GitHub:

- `DOCKER_USERNAME`: Seu nome de usuário no Docker Hub
- `DOCKER_PASSWORD`: Sua senha do Docker Hub

### Acessando a Imagem do Container

Após uma execução bem-sucedida do workflow, você pode baixar a imagem do Docker Hub:

```bash
docker pull seu_usuario/chatgpt-app:latest
```

Substitua `seu_usuario` pelo seu nome de usuário no Docker Hub.
