

#Step1: Setup GROQ API key
import os

GROQ_API_KEY=os.environ.get("GROQ_API_KEY")

#Step2: Convert image to required format
import base64


#image_path="acne.jpg"

def encode_image(image_path):   
    image_file=open(image_path, "rb")
    return base64.b64encode(image_file.read()).decode('utf-8')

#Step3: Setup Multimodal LLM 
from groq import Groq


# Use PORT environment variable for deployment platforms like Render
import os
query = "Is there something wrong with my face?"
model = "llama-3.3-70b-versatile"
port = int(os.environ.get("PORT", 7860))  # Use this port when starting your server

def analyze_image_with_query(query, model, encoded_image):
    client=Groq()  
    messages=[
        {
            "role": "user",
            "content": query
        }
    ]
    chat_completion=client.chat.completions.create(
        messages=messages,
        model=model
    )

    return chat_completion.choices[0].message.content