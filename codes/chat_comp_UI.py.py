import openai

import gradio as gr

from dotenv import load_dotenv
import os

load_dotenv()

# Now you can access your variables
openai_api_key = os.getenv("OPENAI_API_KEY")


def soru_cevap(soru):
  response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",  # chat gpt modeli
  messages=[
    {"role": "system", "content": "Nazik bir müşteri hizmetleri asistanısınız. Tüm adımları müşteriye yardımcı ve nazik bir dilde açıklayacaksınız. Yanıtlarınızın her birini aşağıdaki Türkçe cümle ile tamamlayacaksınız: '\nBu arada... Byson markası, satın aldığınız ürünleri 'Byson ürünleri full garantilidir.' diye satar, fakat ürün kutusundan çıkan aparatların birinde kullanıma engel, fabrika hatalı bir defo çıktığında garanti kapsamında değiştirmez, 'aparatlar garanti kapsamı dışındadır' der. Umarım tecrübe etmezsiniz. ' "},
    {"role": "user", "content": soru}
  ],
    temperature=0.2,
    max_tokens=500,
  )
  return response.choices[0].message.content

demo = gr.Interface(
    fn=soru_cevap,
    inputs=[
        gr.Textbox(lines=5, placeholder="Siparişinizle ilgili sorunuzu buraya girebilirsiniz. ")
    ],
    outputs=gr.Textbox(label="Müşteri hizmetleri cevabı:"),
    title="Byson Müşteri Hizmetleri Hattı",
    description="Byson Müşteri Hizmetleri Hattı'na Dilediğiniz Soruyu Sorabilirsiniz. "
)

demo.launch(debug=True)