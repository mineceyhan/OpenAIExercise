import os
from dotenv import load_dotenv
import openai

# isim = input("Lütfen tam adınızı yazınız:")
# adres = input("Lütfen tam adresinizi yazınız:")
# telefon = input("Lütfen telefon numaranızı yazınız:")
# tarih = input("Lütfen dilekçe tarihini yazınız (GG/AA/YYYY):")
# konu = input("Lütfen dilekçe konusunu yazınız:")
# icerik = input("Lütfen dilekçe içeriğini yazınız:")
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

prompt ="Kimlik Doğrulama: Kullanıcı kendine ait bir hesap oluşturarak oturum açabilmeli. Dil Seçimi: Kullanıcının çeviri yapmak istediği kaynak ve hedef dilleri kolayca seçebilmesini sağlayan bir arayüz.Metin Girişi: Kullanıcının çeviri yapılacak metni yazabileceği bir alan.Sesli Giriş: Kullanıcının metin yerine sesli komutlarla çeviri yapmasına olanak tanıyan bir özellik.Çeviri Butonu: Tek bir tıklama ile çeviri işlemini başlatan bir düğme.Çeviri Sonucu Ekranı: Çeviri yapılan metnin hedef dilde görüntülendiği bir alan.Kopyalama Özelliği: Çeviri metnini kopyalamaya olanak tanıyan bir seçenek.Tarihçe: Daha önce yapılan çevirilerin kaydedildiği ve kolayca erişilebildiği bir bölüm.flutter da böyle bir uygulama geliştirilecektir. Backend kısmında flask apı yazılacaktır. Flutter da gereken tüm dosyaları ve dizinleri oluştur . "
print(prompt)
def get_user_input(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "You are a helpful assistant."},
                  {"role": "user", "content": prompt}],
    top_p = 0.3, #   (Nucleus Sampling)(float):
    #max_tokens = 50,  #(integer):
    temperature = 0.3, #temperature (float):
    n= 1, # (integer):
    presence_penalty = 0.5, #(float):
    frequency_penalty = 0.5, # (float):
    stop=None, #(list or string):
    )
    
    return  response
    
print(get_user_input(prompt))