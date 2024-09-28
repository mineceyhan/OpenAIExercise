import openai
import json
import gradio as gr
from dotenv import load_dotenv
import os

load_dotenv()

# Now you can access your variables
openai.api_key = os.getenv("OPENAI_API_KEY")

# print(openai.models.list())
# print(openai.fine_tuning.jobs.list())


with open(r'C:\Users\ceyha\OneDrive\Masaüstü\openai\files\data.json', 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)

# JSONL dosyasına yaz
with open(r'C:\Users\ceyha\OneDrive\Masaüstü\openai\files\data.jsonl', 'w', encoding='utf-8') as jsonl_file:
    for item in data:
        jsonl_file.write(json.dumps(item) + '\n')
                         
file = openai.File.create(
  file=open(r'C:\Users\ceyha\OneDrive\Masaüstü\openai\files\data.jsonl', "rb"),
  purpose='fine-tune'
)
file_id = file.id

fine_tune = openai.FineTuningJob.create(
  training_file=file_id,
  model="gpt-4o-mini-2024-07-18"  # veya başka bir model 
)
fine_tune_id = fine_tune.id
print("fine tune: ")
print(fine_tune)
response = openai.FineTune.retrieve(
  fine_tune_id=fine_tune_id
)
print(response)
fine_tuned_model = response['fine_tune']
system_message = """
Siz, bir üniversitenin Yazılım Mühendisliği bölümü için oluşturulmuş bir sanal asistansınız. Görevleriniz şunlardır:

1. Öğrencilerin ders programı, içerikleri ve ön koşulları hakkındaki sorularını doğru ve net bir şekilde yanıtlamak.
2. Öğretim üyeleri ve ders kayıtları hakkında bilgi vermek.
3. Bölümün genel işleyişi ve kuralları hakkında bilgilendirme yapmak.
4. Öğrencilerin akademik süreçleri hakkında yönlendirici bilgiler sunmak.

Cevaplarınızı verirken şu kurallara dikkat edin:
- Her zaman nazik, profesyonel ve yardımsever olun.
- Bilgilerinizi güncel tutmaya özen gösterin.
- Emin olmadığınız konularda spekülatif cevaplar vermekten kaçının.
- Bilmediğiniz veya emin olmadığınız bir soru sorulduğunda, şu şekilde yanıt verin:
  "Bu konu hakkında detaylı bilgim bulunmuyor. Daha doğru ve güncel bilgi için lütfen üniversitemizin çağrı merkezini arayınız. Çağrı merkezi numarası: 444 444 444"

Amacınız, öğrencilere Yazılım Mühendisliği bölümüyle ilgili en doğru ve faydalı bilgileri sağlamaktır.
"""
def get_response(prompt, history):
    response = openai.ChatCompletion.create(
        model=fine_tuned_model,
        messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": prompt}
        ],
        n=1,
        stop=None,
        temperature=0.7,
    )
    return response.choices[0].message.content

demo = gr.ChatInterface(
    fn=get_response,
    title="Yazılım Mühendisliği Bölümü Sohbet Robotu",
    description="Öğrencilerin ders programı, içerikleri ve ön koşulları hakkındaki sorularını yanıtlamak için bu sanal asistanı kullanabilirsiniz."
)

if __name__ == "__main__":
    demo.launch(debug=True)