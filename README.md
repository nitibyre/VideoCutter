# 🎬 Video Bölücü

Bu basit Python scripti, yerel bir video dosyasını kullanıcı tarafından belirlenen sürelerde küçük parçalara böler ve bu parçaları otomatik olarak bir klasöre kaydeder.

---

## 🚀 Özellikler

- Herhangi bir yerel video dosyasını küçük parçalara böler
- Parça uzunluğunu saniye cinsinden kullanıcı belirler
- Otomatik olarak `<video_adı> bölümleri` adlı bir klasör oluşturur
- MoviePy kütüphanesi ile yaygın video formatlarını destekler (`.mp4`, `.avi`, vb.)

---

## 🧰 Gereksinimler

- Python 3.6 veya üzeri
- [MoviePy](https://zulko.github.io/moviepy/) Python kütüphanesi
- Sisteme kurulu ve PATH'e eklenmiş [FFmpeg](https://ffmpeg.org/)

---

## ⚙️ Kurulum

1. **Python 3.6+ kurun**  
   [Python resmi sitesinden indirin](https://www.python.org/downloads/)  
   veya Komut İstemcisine şu komutu yazın:

```
winget install python
```

2. **MoviePy kütüphanesini yükleyin**  
   Komut İstemcisine şu komutu yazın:

```
pip install moviepy
```

3. **FFmpeg kurulumu**

- [ffmpeg.org](https://ffmpeg.org/) adresinden sisteminize uygun FFmpeg sürümünü indirin.
- Kurulumdan sonra FFmpeg’in PATH'e eklendiğinden emin olun.
- Alternatif olarak aşağıdaki komutu deneyebilirsiniz:

  ```
  pip install imageio-ffmpeg
  ```

---

## 🧪 Kullanım

1. Scripti çalıştırın.
2. İstenen yerel video dosyasının **tam yolunu** girin. Örnek:

- **Windows**: `C:\Users\Kullanıcı\Videolar\ornek.mp4`
- **macOS/Linux**: `/home/kullanici/Videolar/ornek.mp4`

3. Parça uzunluğunu **saniye cinsinden** girin (örneğin `10`).

Script, bulunduğunuz dizinde `<video_adı> bölümleri` adında bir klasör oluşturacak ve bölünmüş parçaları bu klasöre kaydedecektir.

---

## ⚠️ Notlar

- Script **sadece yerel video dosyalarıyla** çalışır.
- YouTube veya benzeri çevrimiçi videoları önce indirip ardından kullanmalısınız.
- Scriptin çalıştığı klasörde dosya okuma/yazma izinlerinizin olması gerekir.

---

## 📬 İletişim

Sorularınız, hata bildirimleriniz veya önerileriniz için lütfen GitHub üzerinden bir **Issue** açın.  
Her türlü katkı ve geri bildirime açığız!

---

## 🪪 Lisans

Bu proje [MIT Lisansı](LICENSE) ile lisanslanmıştır.
