from huggingface_hub import InferenceClient
from dotenv import load_dotenv
import os


load_dotenv()


api_key = os.getenv("HUGGINGFACE_API_KEY")


prompt = input("¿Qué quieres preguntar? ")


client = InferenceClient(api_key=api_key)


messages = [
    {
        "role": "user",
        "content": prompt
    }
]


completion = client.chat.completions.create(
    model="meta-llama/Llama-3.2-1B-Instruct", 
    messages=messages, 
    max_tokens=500
)


print(completion["choices"][0]["message"]["content"])