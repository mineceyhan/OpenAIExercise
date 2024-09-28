import openai
import requests
from PIL import Image
from io import BytesIO
from dotenv import load_dotenv
import os

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")
# (DALL·E 2 only)
response = openai.images.create_variation( 
  image=open(r"C:\Users\ceyha\OneDrive\Masaüstü\openai\images\zoo.png", "rb"), # file, Required, The image to edit. Must be a valid PNG file, less than 4MB, and square.
                                                                              #If mask is not provided, image must have transparency, which will be used as the mask.
  n=1,
  size="1024x1024" # Must be one of 256x256, 512x512, or 1024x1024.
  #response_format = "b64_json", #string or null, Optional, Defaults to url, The format in which the generated images are returned.
  # Must be one of url or b64_json. URLs are only valid for 60 minutes after the image has been generated.
)
image_url = response.data[0].url
print(f"Image URL: {image_url}")

image_response = requests.get(image_url)
img = Image.open(BytesIO(image_response.content))

img.save("zoo-variation.png")
print("Görüntü kaydedildi")
