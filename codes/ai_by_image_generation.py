import openai
import requests
from PIL import Image
from io import BytesIO

from dotenv import load_dotenv
import os

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")

response = openai.Image.create(
  model="dall-e-3",
  prompt="Language Translation	Metin veya konuşmayı bir dilden diğerine gerçek zamanlı olarak çevirir. Temel Özellikler: Kimlik Doğrulama: Kullanıcı kendine ait bir hesap oluşturarak oturum açabilmeli.  Dil Seçimi: Kullanıcının çeviri yapmak istediği kaynak ve hedef dilleri kolayca seçebilmesini sağlayan bir arayüz. Metin Girişi: Kullanıcının çeviri yapılacak metni yazabileceği bir alan. Sesli Giriş: Kullanıcının metin yerine sesli komutlarla çeviri yapmasına olanak tanıyan bir özellik. Çeviri Butonu: Tek bir tıklama ile çeviri işlemini başlatan bir düğme. Çeviri Sonucu Ekranı: Çeviri yapılan metnin hedef dilde görüntülendiği bir alan. Kopyalama Özelliği: Çeviri metnini kopyalamaya olanak tanıyan bir seçenek.Tarihçe: Daha önce yapılan çevirilerin kaydedildiği ve kolayca erişilebildiği bir bölüm. bu özelliklere sahip mobil uygulamamın logosunu yap ",
  quality = "hd", #This param is only supported for dall-e-3.
  size="1024x1024",  #The size of the generated images. Must be one of 256x256, 512x512, or 1024x1024 for dall-e-2. Must be one of 1024x1024, 1792x1024, or 1024x1792 for dall-e-3 models.
  style="natural", #The style of the generated images. Must be one of vivid or natural. Vivid causes the model to lean towards generating hyper-real and dramatic images.
                  #Natural causes the model to produce more natural, less hyper-real looking images. This param is only supported for dall-e-3.
  n=1, #integer or null, Optional, Defaults to 1 , The number of images to generate. Must be between 1 and 10. For dall-e-3, only n=1 is supported.
  #response_format = "b64_json", #string or null, Optional, Defaults to url, 
  # The format in which the generated images are returned. Must be one of url or b64_json. URLs are only valid for 60 minutes after the image has been generated.
)
print(response)

image_url = response.data[0].url

image_response = requests.get(image_url)
img = Image.open(BytesIO(image_response.content))

img.save(r"C:\Users\ceyha\OneDrive\Masaüstü\openai\images\cat.png")
print("Görüntü kaydedildi: bald-women.png")
