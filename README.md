# YKS Sınav Asistanı
 Yapay Zekâ Destekli Kişisel Deneme Analizi ve Soru Öneri Sistemi;
Bu proje, **BOZ213 Nesne Tabanlı Programlama** dersi final projesi olarak geliştirilmiştir. Python dili kullanılarak hazırlanan uygulama, YKS sürecindeki öğrencilerin sınav sonuçlarını analiz etmelerini ve net takibi yapmalarını sağlayan masaüstü tabanlı bir araçtır.

## Projenin Amacı

Projenin temel amacı, kullanıcıdan alınan sınav verilerini (doğru/yanlış sayıları) işleyerek anlamlı sonuçlar üretmek ve öğrencinin akademik durumunu raporlamaktır. Geliştirme sürecinde sadece kodun çalışmasına değil, **sürdürülebilir ve geliştirilebilir** bir yazılım mimarisine odaklanılmıştır.

## Teknik Altyapı ve Mimari (OOP)

Proje kodlanırken **Nesne Tabanlı Programlama (OOP)** prensiplerine sadık kalınmıştır. Spagetti kod yapısından kaçınılarak modüler bir düzen oluşturulmuştur.

* **Sınıf (Class) Yapısı:** Öğrenci verileri ve sınav işlemleri, birbirinden bağımsız sınıflar içerisinde kapsüllenmiştir (Encapsulation). Bu sayede veri güvenliği ve kod düzeni sağlanmıştır.
* **Algoritma Mantığı:** ÖSYM standartlarına uygun (4 yanlış 1 doğruyu götürür) net hesaplama algoritması kullanılmıştır.
* **Karar Yapıları:** Uygulama, kullanıcının başarı durumuna göre dinamik geri bildirimler veren koşullu yapılara (If-Else blokları) sahiptir.
* **Temiz Kod (Clean Code):** Değişken ve fonksiyon isimlendirmelerinde anlaşılır ve standartlara uygun isimlendirmeler tercih edilmiştir.

## Kurulum (Installation)

Projeyi kendi bilgisayarınızda çalıştırmak için ekstra bir kütüphane kurulumuna (pip install vb.) ihtiyaç yoktur. Python yüklü olması yeterlidir.

1.  Proje dosyalarını **Code > Download ZIP** seçeneği ile indirin.
2.  ZIP dosyasını klasöre çıkartın.
3.  Terminal veya komut satırını açarak proje dizinine gelin.

## Kullanım (Usage)

Uygulamayı başlatmak için terminale aşağıdaki komutu yazmanız yeterlidir:

```bash
python yks.koçu.py
