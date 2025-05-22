# Gemini API: Explorador de Oportunidades com Agentes de IA

Este projeto utiliza a API Gemini do Google para simular uma conversa em três etapas com um modelo de linguagem grande (LLM). O objetivo é identificar uma área de oportunidade para o uso de agentes de IA, detalhar um "pain-point" (ponto de dor) nessa área e, finalmente, propor soluções para esse desafio.

## Funcionalidades

O script `business.py` executa as seguintes ações:

1.  **Identificação de Área de Oportunidade:** Envia um prompt inicial para o modelo Gemini solicitando a identificação de uma área promissora para a aplicação de agentes de IA.
2.  **Detalhamento do Pain-Point:** Utiliza a resposta anterior para pedir ao modelo que apresente um desafio específico (pain-point) dentro da área identificada que poderia ser solucionado com agentes de IA.
3.  **Proposta de Soluções:** Com base no pain-point, solicita ao modelo que sugira três propostas de solução para o desafio.

As respostas do modelo são impressas no console a cada etapa.

## Pré-requisitos

*   Python 3.x
*   Conta no Google AI Studio e uma chave de API do Gemini.

## Configuração

1.  **Clone o repositório (se aplicável) ou crie os arquivos localmente.**

2.  **Crie um ambiente virtual (recomendado):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows: venv\Scripts\activate
    ```

3.  **Instale as dependências:**
    Crie um arquivo `requirements.txt` com o seguinte conteúdo:
    ```
    google-generativeai
    python-dotenv
    ```
    E então instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure sua chave de API do Gemini:**
    Crie um arquivo chamado `.env` na raiz do projeto e adicione sua chave de API:
    ```env
    GENAI_API_KEY="SUA_CHAVE_API_AQUI"
    ```
    Substitua `"SUA_CHAVE_API_AQUI"` pela sua chave de API real do Gemini.

## Como Executar

Após configurar o ambiente e as dependências, execute o script Python:

```bash
python business.py
```

O script irá imprimir a confirmação de que a chave API foi encontrada e, em seguida, as respostas do modelo Gemini para cada uma das três etapas da conversa.

## Exemplo de Saída (Ilustrativo)

```
A chave API do Gemini existe e começa com AIzaSyBU
[Resposta do Modelo para a primeira pergunta sobre área de oportunidade]
[Resposta do Modelo para a segunda pergunta sobre o pain-point]
[Resposta do Modelo para a terceira pergunta sobre as soluções]
```

## Modelo Utilizado

O script está configurado para usar o modelo `gemini-2.5-flash-preview-04-17`. Você pode alterar o nome do modelo no script se desejar usar outro modelo compatível.
