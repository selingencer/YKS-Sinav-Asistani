# BOZ213 FINAL – YKS SINAV ASİSTANI (KARAR DESTEK SİSTEMİ)


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

# Yazılım Mimarisi ve OOP Prensipleri

Bu projede Nesne Yönelimli Programlama (OOP) prensipleri etkin şekilde kullanılmıştır.

- **Kapsülleme (Encapsulation):** Öğrenci bilgileri ve sınav verileri sınıf yapıları içinde izole edilmiştir.
- **Kalıtım (Inheritance):** TYT ve AYT sınavları ortak bir sınav yapısından türetilmiştir.
- **Çok Biçimlilik (Polymorphism):** Farklı sınav türleri aynı metot isimleriyle farklı davranışlar sergileyebilir.
- **Soyutlama (Abstraction):** Kullanıcı arayüzü, analiz ve veri işlemleri birbirinden ayrılmıştır.

Bu yapı sayesinde proje okunabilir, sürdürülebilir ve geliştirilebilir bir mimariye sahiptir.



📜 Lisans
Bu proje, Ankara Üniversitesi BOZ213 – Nesne Yönelimli Programlama dersi kapsamında akademik amaçla geliştirilmiştir. Kaynak kodlar eğitim ve inceleme amacıyla açıktır.

© 2026 Selin Gencer. Tüm hakları saklıdır.


