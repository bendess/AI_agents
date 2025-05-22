import os
from google import genai
from dotenv import load_dotenv

load_dotenv(override=True)
gemini_api_key=os.getenv("GENAI_API_KEY")

if gemini_api_key:
    print(f"A chave API do Gemini existe e começa com {gemini_api_key[:8]}")
else:
    print("A chave API do Gemini não foi encontrada.")

client=genai.Client()

messages=[
    {
        "role": "user", 
        "parts": [
               {"text": "Procure uma área que possa valer a pena explorar por uma oportunidade de uso de agentes de IA."}
        ]
    }
]

response=client.models.generate_content(
    model="gemini-2.5-flash-preview-04-17",
    contents=messages
)

answer=response.text
print(answer)

messages=[
    {
        "role": "user", 
        "parts": [
               {"text": "Agora apresente um pain-point nessa indústria - algo desafiador que possa tirar proveito de uma solução com agentes: " + answer}
        ]
    }
]

response=client.models.generate_content(
    model="gemini-2.5-flash-preview-04-17",
    contents=messages
)

answer=response.text
print(answer)

messages=[
    {
        "role": "user", 
        "parts": [
               {"text": "Apresente agora 3 propostas de soluções para esse desafio: " + answer}
        ]
    }
]

response=client.models.generate_content(
    model="gemini-2.5-flash-preview-04-17",
    contents=messages
)

answer=response.text
print(answer)
