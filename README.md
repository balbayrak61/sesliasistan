# Asistanım - Sesli Asistan Projesi

Asistanım, sesli komutlarla çalışan bir dijital asistandır. Kullanıcıdan gelen sesli komutları algılar, belirli görevleri yerine getirir ve gerektiğinde yanıtlar verir.

## Özellikler
- **Sesli Komut Algılama**: Kullanıcının söylediklerini algılar ve ilgili komutları çalıştırır.
- **Metin Seslendirme**: gTTS (Google Text-to-Speech) kullanarak sesli yanıtlar verir.
- **YouTube Video Açma**: Kullanıcının istediği videoyu açabilir.
- **Google Arama Yapma**: Kullanıcının istediği terimleri Google'da arayabilir.
- **Hava Durumu Sorgulama**: Belirtilen şehir için hava durumunu getirir.

## Kurulum

### 1. Gerekli Bağımlılıkları Yükleyin

Proje için aşağıdaki bağımlılıkları yükleyin:
```bash
pip install gtts playsound speechrecognition pyaudio selenium beautifulsoup4 requests
```

### 2. Selenium için WebDriver Kurulumu

Eğer Selenium kullanacaksanız, ChromeDriver'ı [buradan](https://chromedriver.chromium.org/downloads) indirip sisteminize uygun şekilde kurmalısınız.

### 3. Projeyi Çalıştırma

```bash
python asistanım.py
```

## Kullanılan Teknolojiler
- **Python** (Ana dil)
- **gTTS** (Metin seslendirme)
- **SpeechRecognition** (Ses tanıma)
- **Selenium** (Web tarayıcı kontrolü)
- **BeautifulSoup** (Web scraping)
- **Requests** (HTTP istekleri)

## Katkıda Bulunma
1. Depoyu forklayın.
2. Yeni bir dal açın (`git checkout -b yeni-ozellik`).
3. Değişiklikleri yapıp commitleyin (`git commit -m 'Yeni özellik eklendi'`).
4. Değişiklikleri push edin (`git push origin yeni-ozellik`).
5. Pull request gönderin.

## Lisans
Bu proje MIT Lisansı ile lisanslanmıştır. Daha fazla bilgi için `LICENSE` dosyasına göz atabilirsiniz.
## 👤 İletişim

Büşra Albayrak
- LinkedIn: [Büşra Albayrak](https://www.linkedin.com/in/büşra-albayrak-59b62a252/)
- Instagram: [@busra.cyber](https://www.instagram.com/busra.cyber/)
