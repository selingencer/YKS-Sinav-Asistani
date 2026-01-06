# BOZ213 FINAL – YKS SINAV ASİSTANI (AI DESTEKLİ)

**Ders:** BOZ213 – Nesne Yönelimli Programlama (OOP)

**Proje Türü:** Final Projesi

**Geliştirici:** Selin Gencer

**Üniversite:** Ankara Üniversitesi



---

## 📖 Proje Hakkında

Bu proje, YKS (Yükseköğretim Kurumları Sınavı) sürecindeki öğrencilerin deneme sınavı sonuçlarını kaydedebilecekleri, gelişimlerini **grafiksel** olarak takip edebilecekleri ve **Karar Ağacı (Decision Tree)** algoritmalarıyla kişiselleştirilmiş çalışma programı önerileri alabilecekleri masaüstü tabanlı bir eğitim aracıdır.

**Projenin Temel Farkı:** Mevcut sınav takip uygulamalarının çoğu sadece veri saklarken, **YKS Sınav Asistanı** veriyi işleyerek öğrenciye anlamlı geri bildirimler sunmayı ve "nokta atışı" konu önerileri yapmayı hedefler.

---

## ✨ Temel Özellikler

* 📝 **Detaylı Sınav Kaydı:** TYT ve AYT deneme sonuçlarının düzenli kaydı.
* 📊 **Veri Görselleştirme:** Başarı grafiklerini (net artış/azalış) görsel olarak takip etme.
* 🧠 **Akıllı Analiz (AI):** Öğrencinin eksik olduğu konuları tespit edip nokta atışı öneriler sunan Karar Destek Sistemi.
* 📅 **Dinamik Planlama:** Eksiklere göre otomatik haftalık ders programı oluşturma.
* 🏗️ **Sürdürülebilir Mimari:** Spagetti koddan uzak, modüler OOP yapısı.

---

## 🛠 Kullanılan Teknolojiler ve Kütüphaneler

| Teknoloji / Kütüphane | Kullanım Amacı |
| :--- | :--- |
| **Python** | Projenin ana programlama dili |
| **Tkinter** | Grafik Kullanıcı Arayüzü (GUI) tasarımı |
| **SQLite** | Öğrenci verileri ve sınav sonuçlarının saklanması |
| **Matplotlib** | Başarı ve gelişim grafiklerinin çizilmesi |
| **Scikit-learn** | Karar Ağacı (Decision Tree) ile konu analizi |
| **OOP** | Modüler ve geliştirilebilir sistem mimarisi |

---

## ⚙️ Kurulum ve Çalıştırma

Projeyi bilgisayarınızda çalıştırmak için aşağıdaki adımları izleyebilirsiniz:

**1. Repoyu Klonlayın**
```bash
git clone [https://github.com/selingencer/YKS-Sinav-Asistani.git](https://github.com/selingencer/YKS-Sinav-Asistani.git)
cd YKS-Sinav-Asistani
```
2. Gerekli Kütüphaneleri Yükleyin
  ```python
pip install matplotlib scikit-learn
# Tkinter ve SQLite Python ile yüklü gelir.

```

3. Uygulamayı Başlatın
```python
python main.py
```

🏗️ Yazılım Mimarisi ve OOP Prensipler
Bu proje, Temiz Kod (Clean Code) prensipleri ve Nesne Yönelimli Programlama (OOP) yaklaşımı ile, bakımı kolay ve modüler bir yapıda tasarlanmıştır.
```
```
🔒 Kapsülleme (Encapsulation)
Sınav sonuçları ve öğrenci bilgileri gibi kritik veriler doğrudan erişime kapatılmıştır. Veri güvenliği için getter ve setter metotları kullanılır.
```python
class Ogrenci:
    def __init__(self, ad, hedef):
        self.__ad = ad            # Private değişken
        self.__net_listesi = []   # Dışarıdan doğrudan değiştirilemez

    def sinav_ekle(self, sonuc):
        # Veri doğrulama burada yapılır
        if sonuc > 0:
            self.__net_listesi.append(sonuc)
```
🧩 Soyutlama (Abstraction)
Veritabanı işlemleri veya analiz algoritmaları arka planda çalışır; kullanıcı sadece basit arayüz fonksiyonlarını görür.
```python
class AnalizYoneticisi:
    def analiz_et(self, veriler):
        # Karar ağacı algoritmaları burada çalışır
        # Kullanıcı detayları bilmek zorunda değildir
        pass
```
🧬 Kalıtım (Inheritance)
Genel bir sınav yapısı oluşturulmuş, TYT ve AYT sınavları bu yapıdan türetilmiştir. Kod tekrarı önlenmiştir.


```python
class Sinav:
    def __init__(self, tarih, net):
        self.tarih = tarih
        self.net = net

class TytSinavi(Sinav):
    def __init__(self, tarih, net, turkce_net):
        super().__init__(tarih, net)
        self.turkce_net = turkce_net
```
🔄 Çok Biçimlilik (Polymorphism)

Farklı sınav türleri (TYT/AYT) için puan hesaplama veya analiz fonksiyonları aynı isimle çağrılır ancak farklı davranır.

Her sınav türü kendi hesaplama yöntemini kullanır
```python
sinav1.puan_hesapla()  # TYT katsayılarına göre

sinav2.puan_hesapla()  # AYT katsayılarına göre
```
📂 Veri Yapıları ve Algoritmalar

Veri Yapıları: Sınav verilerini tutmak için Listeler, konu eşleştirmeleri için Sözlük (Dictionary) yapıları kullanılmıştır.

Algoritma: Öğrencinin başarısız olduğu konuları belirlemek için Karar Ağacı (Decision Tree) mantığına dayalı kural tabanlı bir algoritma geliştirilmiştir.

📜 Lisans
Bu proje, Ankara Üniversitesi BOZ213 – Nesne Yönelimli Programlama dersi kapsamında akademik amaçla geliştirilmiştir. Kaynak kodlar eğitim ve inceleme amacıyla açıktır.

© 2026 Selin Gencer. Tüm hakları saklıdır.


