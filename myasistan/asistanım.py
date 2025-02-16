import time

from gtts import gTTS
from playsound import playsound
import speech_recognition as sr
import pyaudio
import random
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup

r=sr.Recognizer()
class SesliAsistan:

    def seslendirme(self,metin):
        metin_seslendirme=gTTS(text=metin, lang="tr")
        dosya=str(random.randint(0,987238378299))+".mp3"
        metin_seslendirme.save(dosya)
        playsound(dosya)

        os.remove(dosya)
    def mikrofon(self):
        with sr.Microphone() as kaynak:
            print("sizi dinliyorum...")
            listen = r.listen(kaynak)
            ses=""

            try:
                 ses=r.recognize_google(listen,language="tr-Tr")
            except sr.UnknownValueError:

                 self.seslendirme("Ne söylediğinizi anlayamadım. Lütfen tekrar edermisiniz")

            return ses
    def ses_karsilik(self,gelen_ses):
        if(gelen_ses in "merhaba"):
            self.seslendirme("merhaba")
        elif (gelen_ses in "nasılsın"):
            self.seslendirme("iyiyim sizler nasılsınız.")
        elif (gelen_ses in "müzik aç" or gelen_ses in "video aç"):
            self.seslendirme("ne açmamı istersiniz.")
            cevap=self.mikrofon()

            url="https://www.youtube.com/results?search_query="+ cevap
            tarayici=webdriver.Chrome()
            tarayici.get(url)
            ilk_video=tarayici.find_element(By.XPATH,"//*[@id='video-title']/yt-formatted-string").click()
            time.sleep(240)
            tarayici.quit()
        elif (gelen_ses in "google aç"  or gelen_ses in "arama yap"):
            self.seslendirme("ne aramamı istersin")
            cevap=self.mikrofon()

            url="https://www.google.com/search?q="+cevap
            self.seslendirme("{}  ile ilgili bulduğum içerikler bunlardır.".format(cevap))
            tarayici=webdriver.Chrome()
            tarayici.get(url)

            site=tarayici.find_element(By.XPATH,"//*[@id='rso']/div[1]/div/div/div/div/div/div/div/div[1]/div/span/a/h3").click()
            time.sleep(10)
            tarayici.quit()

        elif (gelen_ses in "hava durumu" or gelen_ses in " bugün hava nasıl"):

            self.seslendirme("Hangi şehrin hava durumunu istersiniz")
            cevap = self.mikrofon()
            print(cevap)

            def HavaRaporlari(gununIndexi):

                url = "https://havadurumu15gunluk.xyz/havadurumu/630/{}-hava-durumu-15-gunluk.html".format(cevap)

                response = requests.get(url)

                if response.status_code == 200:
                    # print("İŞLEM BAŞARILI")
                    soup = BeautifulSoup(response.text, "html.parser")
                    # print(soup)

                    tumVeriler = soup.find_all("tr")[gununIndexi].text
                    tumVeriler = tumVeriler.replace("Saatlik", "").strip()
                    print(tumVeriler)

                    gunluk_hava = ""
                    gunduz_sicaklik = tumVeriler[-6:-4]
                    gece_sicaklik = tumVeriler[-3:-1]
                    print("Gunduz Sıcaklık: " + gunduz_sicaklik)
                    print("Gece Sıcaklık: " + gece_sicaklik)

                    tumVeriler = tumVeriler[6:-6].strip()

                    gunun_ismi = tumVeriler[:3]

                    gunKisaltma = ["Sal", "Çar", "Per", "Cum", "Cmt", "Paz", "Pzt"]

                    for x in gunKisaltma:
                        if x in tumVeriler:
                            gunluk_hava = tumVeriler.replace(x, "")

                    print("Hava Durumu: " + gunluk_hava)

                    gununIsimleri = {"Paz": "Pazartesi", "Pzt": "Pazartesi", "Sal": "Salı", "Çar": "Çarşamba",
                                     "Per": "Perşembe", "Cum": "Cuma", "Cmt": "Cumartesi"}
                    gunun_ismi = gununIsimleri[gunun_ismi]
                    print("Gunun Adı: " + gunun_ismi)

                    return "{} için {} günün hava raporları şu şekilde: Hava: {} Gündüz Sıcaklığı: {} derece Gece Sıcaklığı: {} derece". \
                        format(cevap, gunun_ismi, gunluk_hava, gunduz_sicaklik, gece_sicaklik)

                else:
                    print("Hata meydana geldi")

            self.seslendirme("{} şehir için yarının mı yoksa 5 günlük raporlarını mı istersiniz".format(cevap))
            cevap2 = self.mikrofon().lower()
            print(cevap2)

            if (cevap2 in "yarının"):

                self.seslendirme(HavaRaporlari(2))
            else:
                sayac = 1

                while sayac < 6:
                    self.seslendirme(HavaRaporlari(sayac))
                    sayac += 1
    def uyandirma_fonsiyonu(self,gelen_ses):
        if(gelen_ses in "asistan"):
           self.seslendirme("sana nasıl yardımcı olabilirim..")
           ses=self.mikrofon()
           if(ses!=""):
                 self.ses_karsilik(ses)



asistan=SesliAsistan()

while True:

    gelen_ses = asistan.mikrofon().lower()
    if(gelen_ses != '' ):
        print(gelen_ses)
        asistan.uyandirma_fonsiyonu(gelen_ses)
