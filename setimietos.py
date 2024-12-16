import os
from dotenv import load_dotenv
import requests


load_dotenv()


API_KEY = os.getenv("HUGGINGFACE_API_KEY")


API_URL = "https://api-inference.huggingface.co/models/cardiffnlp/twitter-roberta-base-sentiment-latest"
headers = {"Authorization": f"Bearer {API_KEY}"}  # Usar el token cargado


def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()


input_text = input("Introduce un texto para analizar su sentimiento: ")


output = query({
    "inputs": input_text,
})

# Imprimir la respuesta completa para depuración
# print("Respuesta de la API:", output)

# Verificar si la respuesta contiene la estructura esperada
if isinstance(output, list) and len(output) > 0 and isinstance(output[0], list) and len(output[0]) > 0:
    # Obtener la lista de sentimientos y puntajes
    sentiment_scores = output[0]
    
    # Ordenar los sentimientos por puntaje (de mayor a menor)
    sentiment_scores.sort(key=lambda x: x['score'], reverse=True)
    
    # Obtener el sentimiento con el puntaje más alto
    top_sentiment = sentiment_scores[0]
    label = top_sentiment['label']
    
    # Imprimir el resultado
    if label == 'positive':
        print("El sentimiento es mayormente positivo.")
    elif label == 'neutral':
        print("El sentimiento es neutral.")
    elif label == 'negative':
        print("El sentimiento es mayormente negativo.")
    else:
        print("Sentimiento desconocido.")
else:
    print("No se pudo obtener el sentimiento o la respuesta no es válida.")