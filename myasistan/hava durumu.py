url = "https://havadurumu15gunluk.xyz/havadurumu/630/istanbul-hava-durumu-15-gunluk.html"

import requests
from bs4 import BeautifulSoup


def Hava(intadata):
    url="https://havadurumu15gunluk.xyz/havadurumu/630/istanbul-hava-durumu-15-gunluk.html"

    response=requests.get(url)

    #print(response)

    if response.status_code==200:
        #print("İŞLEM BAŞARILI")
        soup=BeautifulSoup(response.text,"html.parser")
        #print(soup)

        tumVeriler=soup.find_all("tr")[intadata].text
        tumVeriler=tumVeriler.replace("Saatlik","").strip()
        print(tumVeriler)

        gunluk_hava=""
        gunduz_sicaklik=tumVeriler[-6:-4]
        gece_sicaklik=tumVeriler[-3:-1]
        print("Gunduz Sıcaklık: "+gunduz_sicaklik)
        print("Gece Sıcaklık: "+gece_sicaklik)

        tumVeriler=tumVeriler[6:-6].strip()

        gunun_ismi=tumVeriler[:3]


        gunKisaltma=["Sal","Çar","Per","Cum","Cmt","Paz","Pzt"]

        for x in gunKisaltma:
            if x in tumVeriler:
                gunluk_hava=tumVeriler.replace(x,"")

        print("Hava Durumu: "+gunluk_hava)

        gununIsimleri={"Paz":"Pazar","Pzt":"Pazartesi","Sal":"Salı","Çar":"Çarşamba","Per":"Perşembe","Cum":"Cuma","Cmt":"Cumartesi"}
        gunun_ismi=gununIsimleri[gunun_ismi]
        print("Gunun Adı: "+gunun_ismi)

    else:
        print("Hata meydana geldi")

Hava(4)