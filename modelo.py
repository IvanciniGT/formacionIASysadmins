#pip3 install transformers torch pillow
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import requests

# Cargar el modelo y el procesador
processor = BlipProcessor.from_pretrained("google/pix2struct-large")
model = BlipForConditionalGeneration.from_pretrained("google/pix2struct-large")

def generate_description(image_url):
    # Descargar y cargar la imagen
    image = Image.open(requests.get(image_url, stream=True).raw)
    print(image)
    # Procesar la imagen
    inputs = processor(images=image, return_tensors="pt")

    # Generar descripción
    outputs = model.generate(**inputs)
    description = processor.decode(outputs[0], skip_special_tokens=True)
    return description

# Ejemplo de uso
image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/9/94/Cane_da_pastore_tedesco_adulto.jpg/640px-Cane_da_pastore_tedesco_adulto.jpg"  # Reemplaza con la URL de tu imagen
description = generate_description(image_url)
print(description)