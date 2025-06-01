#C:\Users\serha\Desktop\Yeni klasör\pano.mp4
import os
from moviepy.video.io.VideoFileClip import VideoFileClip

# Geçerli bir video dosyası yolu alınana kadar sor
while True:
    video_path = input("Video dosyasının tam yolunu ve adını yazınız (örn: C:\\Users\\AAAaa\\Desktop\\Yeni klasör\\pano.mp4): ").strip()
    if os.path.isfile(video_path):
        break
    else:
        print("Girdiğiniz dosya bulunamadı. Lütfen doğru ve tam yolu yazınız.")

# Parça süresini al
while True:
    try:
        parca_suresi = float(input("Videonun kaç saniyelik parçalara bölünmesini istersiniz? (örn: 10): "))
        if parca_suresi <= 0:
            print("Lütfen pozitif bir sayı giriniz.")
            continue
        break
    except ValueError:
        print("Lütfen geçerli bir sayı giriniz.")

clip = VideoFileClip(video_path)
video_suresi = clip.duration

# Video ismini dosya uzantısından ayır (örnek: pano.mp4 -> pano)
video_ismi = os.path.splitext(os.path.basename(video_path))[0]

# Klasör adı oluştur
klasor_adi = f"{video_ismi} bölümleri"

# Klasör yoksa oluştur
if not os.path.exists(klasor_adi):
    os.makedirs(klasor_adi)

parca_sayisi = int(video_suresi // parca_suresi)
if video_suresi % parca_suresi != 0:
    parca_sayisi += 1

print(f"Video {video_suresi:.2f} saniye, toplam {parca_sayisi} parça olarak kaydedilecek.\n")

for i in range(parca_sayisi):
    baslangic = i * parca_suresi
    bitis = min((i + 1) * parca_suresi, video_suresi)
    parca = clip.subclipped(baslangic, bitis)  # senin kodundaki gibi bıraktım
    dosya_adi = os.path.join(klasor_adi, f"parca_{i+1}.mp4")
    print(f"{dosya_adi} kaydediliyor... ({baslangic:.2f}-{bitis:.2f} saniye)")
    parca.write_videofile(dosya_adi, codec="libx264")

clip.close()
print("Bütün parçalar başarıyla kaydedildi!")

