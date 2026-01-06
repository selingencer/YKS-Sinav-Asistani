import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
import pandas as pd
import os
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import datetime
import numpy as np
from sklearn.tree import DecisionTreeClassifier
import random
from abc import ABC, abstractmethod

# --- 1. KONFİGÜRASYON VE SABİTLER (Encapsulation) ---
class UygulamaAyarlari:
    RENKLER = {
        "BG": "#f4f7f6",
        "SIDEBAR": "#2c3e50",
        "HEADER": "#ecf0f1",
        "CARD_BLUE": "#3498db",
        "CARD_RED": "#e74c3c",
        "CARD_PURPLE": "#9b59b6",
        "TEXT": "#2c3e50",
        "ACCENT": "#2980b9",
        "LOGIN_BG": "#34495e" # Giriş ekranı için yeni renk
    }

    KONU_HAVUZU = {
        "TYT": {
            "Matematik": ["Temel Kavramlar", "Sayı Basamakları", "Bölme-Bölünebilme", "EBOB-EKOK", "Rasyonel Sayılar", "Mutlak Değer", "Üslü-Köklü Sayılar", "Çarpanlara Ayırma", "Oran-Orantı", "Problemler", "Kümeler", "Fonksiyonlar", "Polinomlar", "Mantık", "Olasılık"],
            "Geometri": ["Doğruda ve Üçgende Açı", "Özel Üçgenler", "Açıortay-Kenarortay", "Üçgende Alan ve Benzerlik", "Çokgenler", "Dörtgenler", "Çember ve Daire", "Katı Cisimler"],
            "Türkçe": ["Sözcükte Anlam", "Cümlede Anlam", "Paragraf", "Ses Bilgisi", "Yazım Kuralları", "Noktalama İşaretleri", "Sözcükte Yapı", "İsim-Sıfat-Zamir", "Zarf-Edat-Bağlaç", "Fiiller", "Cümlenin Ögeleri"],
            "Fizik": ["Fizik Bilimine Giriş", "Madde ve Özellikleri", "Hareket ve Kuvvet", "İş, Güç ve Enerji", "Isı ve Sıcaklık", "Basınç", "Kaldırma Kuvveti", "Elektrostatik", "Optik", "Dalgalar"],
            "Kimya": ["Kimya Bilimi", "Atom ve Periyodik Sistem", "Türler Arası Etkileşimler", "Maddenin Halleri", "Doğa ve Kimya", "Temel Kanunlar", "Karışımlar", "Asitler, Bazlar ve Tuzlar", "Kimya Her Yerde"],
            "Biyoloji": ["Yaşam Bilimi Biyoloji", "Hücre", "Canlılar Dünyası", "Hücre Bölünmeleri", "Kalıtım", "Ekosistem Ekolojisi"],
            "Tarih": ["Tarih Bilimine Giriş", "İlk Çağ Medeniyetleri", "İslamiyet Öncesi Türk Tarihi", "İslam Tarihi", "Türk-İslam Tarihi", "Osmanlı Kuruluş-Yükselme", "Osmanlı Kültür Medeniyet", "Kurtuluş Savaşı", "Atatürk İlke ve İnkılapları"],
            "Coğrafya": ["Doğa ve İnsan", "Dünyanın Şekli ve Hareketleri", "Harita Bilgisi", "İklim Bilgisi", "İç ve Dış Kuvvetler", "Nüfus ve Yerleşme", "Ekonomik Faaliyetler", "Bölgeler ve Ulaşım", "Doğal Afetler"],
            "Felsefe": ["Felsefeye Giriş", "Bilgi Felsefesi", "Varlık Felsefesi", "Ahlak Felsefesi", "Sanat Felsefesi", "Din Felsefesi", "Siyaset Felsefesi", "Bilim Felsefesi"],
            "Din Kültürü": ["İnanç", "İbadet", "Ahlak ve Değerler", "Hz. Muhammed (S.A.V)", "Vahiy ve Akıl", "Din ve Laiklik"]
        },
        "AYT": {
            "Matematik": ["2. Dereceden Denklemler", "Karmaşık Sayılar", "Parabol", "Eşitsizlikler", "Logaritma", "Diziler", "Limit ve Süreklilik", "Türev Alma Kuralları", "Türev Uygulamaları", "İntegral", "Trigonometri", "Çemberin Analitiği", "Dönüşüm Geometrisi"],
            "Fizik": ["Vektörler", "Bağıl Hareket", "Newton'un Hareket Yasaları", "Atışlar", "İtme ve Momentum", "Tork ve Denge", "Elektrik Alan ve Potansiyel", "Manyetizma", "Alternatif Akım", "Çembersel Hareket", "Basit Harmonik Hareket", "Atom Fiziği", "Modern Fizik"],
            "Kimya": ["Modern Atom Teorisi", "Gazlar", "Sıvı Çözeltiler", "Kimyasal Tepkimelerde Enerji", "Tepkime Hızı", "Kimyasal Denge", "Asit-Baz Dengesi", "Çözünürlük Dengesi", "Kimya ve Elektrik", "Organik Kimya"],
            "Biyoloji": ["Sinir Sistemi", "Endokrin Sistem", "Duyu Organları", "Destek ve Hareket Sistemi", "Sindirim Sistemi", "Dolaşım Sistemi", "Solunum Sistemi", "Üriner Sistem", "Üreme Sistemi", "Komünite ve Popülasyon Ekolojisi", "Genden Proteine", "Canlılarda Enerji Dönüşümleri", "Bitki Biyolojisi"],
            "Edebiyat": ["İslamiyet Öncesi Türk Edb.", "Halk Edebiyatı", "Divan Edebiyatı", "Tanzimat Edebiyatı", "Servet-i Fünun", "Milli Edebiyat", "Cumhuriyet Dönemi Şiir", "Cumhuriyet Dönemi Roman", "Edebi Akımlar"],
            "Tarih-1/2": ["Tarih Bilimi", "İlk Türk Devletleri", "İslam Tarihi", "Türk İslam Devletleri", "Osmanlı Tarihi (Tüm Dönemler)", "Milli Mücadele", "Atatürkçülük ve İnkılaplar", "Çağdaş Türk ve Dünya Tarihi"],
            "Coğrafya-1/2": ["Ekosistem", "Nüfus Politikaları", "Türkiye'nin Ekonomisi", "Küresel Ticaret", "Jeopolitik Konum", "Bölgesel Kalkınma Projeleri", "Çevre ve Toplum"],
            "Felsefe Grubu": ["Psikoloji Bilimine Giriş", "Psikolojide Temel Süreçler", "Sosyolojiye Giriş", "Birey ve Toplum", "Toplumsal Yapı", "Mantığa Giriş", "Klasik Mantık", "Sembolik Mantık"]
        }
    }
    
    MOTIVASYON_SOZLERI = [
        "🚀 Başlamak için mükemmel olmak zorunda değilsin, ama mükemmel olmak için başlamak zorundasın.",
        "💎 Elmas nasıl yontulmadan kusursuz olmazsa, insan da acı çekmeden olgunlaşmaz.",
        "🏆 Şampiyonlar salonlarda değil, içlerindeki tutku ve hayallerde doğar.",
        "⏳ Gelecek, bugün ne yaptığına bağlıdır.",
        "🔥 Vazgeçtiğin an, kaybettiğin andır.",
        "📚 Bir gün değil, her gün çalışan kazanır.",
        "🌟 Hayallerin hedeflerine, hedeflerin gerçeğe dönüşsün."
    ]

# --- 2. VERİTABANI KATMANI (Data Access Layer) ---
class VeriTabaniYoneticisi:
    def __init__(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(base_dir, 'yks_asistani_MAIN.db')
        
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self.cursor = self.conn.cursor()
        self._tablo_olustur()
        self._hedef_tablosu_olustur()

    def _tablo_olustur(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS denemeler
                             (id INTEGER PRIMARY KEY, deneme_adi TEXT, tarih TEXT, eksik_konular TEXT, 
                              tyt_turk_d INT, tyt_turk_y INT, tyt_turk_b INT,
                              tyt_mat_d INT, tyt_mat_y INT, tyt_mat_b INT,
                              tyt_sos_d INT, tyt_sos_y INT, tyt_sos_b INT,
                              tyt_fen_d INT, tyt_fen_y INT, tyt_fen_b INT,
                              ayt_mat_d INT, ayt_mat_y INT, ayt_mat_b INT,
                              ayt_fiz_d INT, ayt_fiz_y INT, ayt_fiz_b INT,
                              ayt_kim_d INT, ayt_kim_y INT, ayt_kim_b INT,
                              ayt_biyo_d INT, ayt_biyo_y INT, ayt_biyo_b INT,
                              ayt_edeb_d INT, ayt_edeb_y INT, ayt_edeb_b INT,
                              ayt_tar1_d INT, ayt_tar1_y INT, ayt_tar1_b INT,
                              ayt_cog1_d INT, ayt_cog1_y INT, ayt_cog1_b INT,
                              ayt_tar2_d INT, ayt_tar2_y INT, ayt_tar2_b INT,
                              ayt_cog2_d INT, ayt_cog2_y INT, ayt_cog2_b INT,
                              ayt_fel_d INT, ayt_fel_y INT, ayt_fel_b INT,
                              ayt_din_d INT, ayt_din_y INT, ayt_din_b INT)''')
        self.conn.commit()

    def _hedef_tablosu_olustur(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS hedefler
                             (id INTEGER PRIMARY KEY, tyt_hedef REAL, ayt_hedef REAL)''')
        self.conn.commit()
        self.cursor.execute("SELECT count(*) FROM hedefler")
        if self.cursor.fetchone()[0] == 0:
            self.cursor.execute("INSERT INTO hedefler VALUES (1, 80.0, 50.0)")
            self.conn.commit()

    def veri_ekle(self, veriler):
        placeholders = ",".join(["?"] * len(veriler))
        self.cursor.execute(f"INSERT INTO denemeler VALUES (NULL, {placeholders})", veriler)
        self.conn.commit()

    def tum_verileri_al(self):
        return pd.read_sql_query("SELECT * FROM denemeler", self.conn)

# --- 3. İŞ MANTIĞI VE ANALİZ KATMANI (Business Logic & OOP) ---
class AnalizMotoru(ABC):
    @abstractmethod
    def analiz_yap(self, *args, **kwargs):
        pass

class DersAnalizcisi(AnalizMotoru):
    def analiz_yap(self, ders_adi, net, soru_sayisi):
        try:
            s = soru_sayisi
            if s == 0: return "Veri yok"
            
            basari_yuzdesi = (net / s) * 100
            
            if basari_yuzdesi < 25: seviye = 0
            elif basari_yuzdesi < 55: seviye = 1
            elif basari_yuzdesi < 80: seviye = 2
            else: seviye = 3
            
            yorumlar = {
                "TYT Türkçe": {
                    0: ["🔴 Paragraf rutinin yok gibi duruyor, acil başla.", "🔴 Türkçede zaman kaybediyorsun, her gün 20 soru şart.", "🔴 Dil bilgisi eksiklerin netlerini törpülüyor."],
                    1: ["🟡 30 net barajına takılmışsın, dil bilgisi tekrarı yap.", "🟡 Paragrafta hızlanman lazım, odak sorunu yaşıyorsun.", "🟡 Yanlışların genelde 'dikkat' kaynaklı olabilir, analiz et."],
                    2: ["🟢 Gayet iyisin! 35 üstü için ALES sorularına bak.", "🟢 Hızın iyi ama 1-2 fire veriyorsun, deneme çöz.", "🟢 Türkçe senin kalen olmuş, sadece formunu koru."],
                    3: ["🔥 Türkçe makine gibi! Nazar değmesin.", "🔥 Fullemeye en yakın olduğun ders bu.", "🔥 Buradan zaman kazanıp Matematiğe aktarabilirsin."]
                },
                "TYT Matematik": {
                    0: ["🔴 İşlem hatası mı, konu eksiği mi? Temel kampına dön.", "🔴 Matematiğe küsme, 'Antrenmanlarla Mat' serisine bak.", "🔴 Yeni nesil sorulardan önce klasikleri hallet."],
                    1: ["🟡 Problemler seni yavaşlatıyor, fasikül bitir.", "🟡 Geometriye bakmıyorsan netlerin burada tıkanır.", "🟡 İlk 15 soruyu daha hızlı geçmen lazım."],
                    2: ["🟢 25-30 bandındasın, branş denemesiyle hızlan.", "🟢 Geometri netlerini artırırsan 35'i görürsün.", "🟢 Zor kaynaklara (Orijinal, 3D) geçiş yap."],
                    3: ["🔥 Derece öğrencisi netleri bunlar.", "🔥 Olimpiyat sorularıyla ufkunu aç.", "🔥 Artık şov yapıyorsun, hız rekoru dene."]
                },
                "TYT Fen": {
                    0: ["🔴 Fen ihmale gelmez, özet videolarla başla.", "🔴 Fizik zor geliyorsa Biyoloji ve Kimya'ya yüklen.", "🔴 En kolay net artışı Fenden gelir, kaçırma."],
                    1: ["🟡 Fizik kanunlarını tekrar etmelisin.", "🟡 Kimya'da mol ve organik temeline dikkat.", "🟡 Biyoloji ezberlerini unutmuş olabilirsin."],
                    2: ["🟢 Fen netlerin çok dengeli, deneme ile koru.", "🟢 Sadece dikkat hatası yapıyorsun, konun tam.", "🟢 AYT Fen için harika bir temel atmışsın."],
                    3: ["🔥 Fen dersinde profesör gibisin!", "🔥 Buradan soru kaçırmaman büyük avantaj.", "🔥 20'de 20 hedefi senin için hayal değil."]
                },
                "TYT Sosyal": {
                    0: ["🔴 'Nasılsa yaparım' deme, kavram çalış.", "🔴 Coğrafya harita bilgisi şart.", "🔴 Felsefe terimlerine göz at."],
                    1: ["🟡 Tarih kronolojisi kafanı karıştırıyor olabilir.", "🟡 Din Kültürü kavramlarını (Tevhid, İhlas) öğren.", "🟡 Yorum gücün iyi ama bilgi eksiğin var."],
                    2: ["🟢 Sosyalden aldığın puan seni öne atıyor.", "🟢 Bilgi sorularını kaçırmıyorsun, tebrikler.", "🟢 Genel kültürün gayet iyi seviyede."],
                    3: ["🔥 Sosyal senin için çerez niyetine.", "🔥 Burayı en hızlı şekilde bitirip turlamaya geç.", "🔥 Hatasız kul olmaz ama senin Sosyal hatasız."]
                }
            }
            
            ders_havuzu = yorumlar.get(ders_adi, yorumlar.get("TYT Matematik")) 
            secilen_yorum = random.choice(ders_havuzu[seviye]) 
            
            return secilen_yorum
        except:
            return "Veri hatası."

class ProgramOlusturucu(AnalizMotoru):
    def analiz_yap(self, seviye_id, eksik_konular_str):
        gunler = ["Pazartesi", "Salı", "Çarşamba", "Perşembe", "Cuma", "Cumartesi", "Pazar"]
        
        if eksik_konular_str and isinstance(eksik_konular_str, str):
            eksik_listesi = [k.strip() for k in eksik_konular_str.split(",")]
            eksik_listesi = [k for k in eksik_listesi if k]
        else:
            eksik_listesi = []
        
        if not eksik_listesi:
            eksik_listesi = ["TYT Mat", "AYT Fizik", "AYT Kimya", "Geometri", "TYT Türkçe", "Tarih", "Coğrafya"]

        sabah_rutinleri = {
            0: "🌅 20 Paragraf + 10 Problem (Süresiz)",
            1: "🌅 20 Paragraf + 15 Problem + Geo Testi",
            2: "🌅 30 Paragraf (Süreli) + 20 Problem",
            3: "🌅 TYT Türkçe Branş Denemesi",
            4: "🌅 TYT Matematik Branş Denemesi"
        }

        ogle_stratejisi = {
            0: "📹 Konu Anlatımı + 2 Kolay Test",
            1: "📚 MEB Kitabı Oku + 3 Test",
            2: "🔥 Eksik Konudan 4 Test Çöz",
            3: "⚡ Çıkmış Sorular + Zor Test",
            4: "🏆 Olimpiyat/Zor Soru Taraması"
        }

        aksam_rutin_listeleri = {
            0: ["🌙 Günlük Tekrar", "🌙 Formül Tekrarı", "🌙 Harita Çalışması", "🌙 Rehberlik Videosu", "🌙 Not Düzenle", "🌙 Kitap Oku", "🌙 Planlama"],
            1: ["🌙 Video Çözüm İzle", "🌙 Sosyal Not Okuma", "🌙 Biyoloji Haritası", "🌙 Geometri Testi", "🌙 Paragraf Taktik", "🌙 Hata Analizi", "🌙 Motivasyon"],
            2: ["🌙 Fen Branş Deneme", "🌙 Sosyal Branş Deneme", "🌙 Geo Tarama (20 Soru)", "🌙 Mat Deneme Analiz", "🌙 MEB Okuması", "🌙 Kesilen Sorular", "🌙 Dinlenme"],
            3: ["🌙 AYT Fen Branş", "🌙 AYT Mat Branş", "🌙 Zor Soru Defteri", "🌙 Genel Deneme Analiz", "🌙 Turlama Pratiği", "🌙 Zaman Yönetimi", "🌙 Strateji"],
            4: ["🌙 Şampiyonlar Ligi Deneme", "🌙 Akademik Okuma", "🌙 Derece Analizi", "🌙 MSÜ Taraması", "🌙 ALES Türkçesi", "🌙 Mental Antrenman", "🌙 Tam Dinlenme"]
        }

        program = []
        random.shuffle(eksik_listesi) 
        
        secilen_sabah = sabah_rutinleri.get(seviye_id, sabah_rutinleri[0])
        secilen_ogle_yontemi = ogle_stratejisi.get(seviye_id, ogle_stratejisi[0])
        secilen_aksam_listesi = aksam_rutin_listeleri.get(seviye_id, aksam_rutin_listeleri[0])

        for i, gun in enumerate(gunler):
            if gun == "Pazar":
                program.append(("Pazar", "🛌 GEÇ KAHVALTI", "☕ HAFTALIK GENEL TEKRAR", "🎬 MOTİVASYON"))
                continue
                
            gunun_konusu = eksik_listesi[i % len(eksik_listesi)]
            ogle_blogu = f"🎯 {gunun_konusu}\n({secilen_ogle_yontemi})"
            aksam_gorevi = secilen_aksam_listesi[i % len(secilen_aksam_listesi)]
            program.append((gun, secilen_sabah, ogle_blogu, aksam_gorevi))
            
        return program

class KararDestekSistemi(AnalizMotoru):
    def __init__(self):
        self.ders_analizcisi = DersAnalizcisi()
        self.program_olusturucu = ProgramOlusturucu()

    def analiz_yap(self, tyt_net, ayt_net, eksik_konular_str, turk_net, mat_net, fen_net, sos_net):
        try:
            X_train = [[20, 5], [45, 15], [65, 30], [85, 50], [105, 70]]
            y_train = [0, 1, 2, 3, 4] 
            clf = DecisionTreeClassifier()
            clf.fit(X_train, y_train)
            sinif_id = clf.predict([[tyt_net, ayt_net]])[0]
            
            hedef_net = tyt_net + 5.5 
            
            yorum_turkce = self.ders_analizcisi.analiz_yap("TYT Türkçe", turk_net, 40)
            yorum_mat = self.ders_analizcisi.analiz_yap("TYT Matematik", mat_net, 40)
            yorum_fen = self.ders_analizcisi.analiz_yap("TYT Fen", fen_net, 20)
            yorum_sos = self.ders_analizcisi.analiz_yap("TYT Sosyal", sos_net, 20)

            ozel_uyari = ""
            if tyt_net > ayt_net + 30:
                ozel_uyari = "⚠️ UYARI: TYT'n çok iyi ama AYT geride kalmış. Odağını %70 AYT'ye kaydır!"
            elif mat_net < turk_net - 10:
                ozel_uyari = "⚠️ DENGESİZLİK: Sözelin çok güçlü ama Sayısal seni aşağı çekiyor."
            elif fen_net < 5:
                 ozel_uyari = "⚠️ FIRSAT: Fen netin çok düşük, buradaki kolay netleri toplarsan puanın uçar."

            motivasyonlar = [
                "💡 'Zafer, zafer benimdir diyebilenindir.' - M.K. Atatürk",
                "💡 Unutma, şu an çözdüğün her zor soru, sınavda sana kolaylık olarak dönecek.",
                "💡 Rakiplerin uyurken senin çalışman fark yaratacak.",
                "💡 Disiplin, yapmak istemediğin şeyi, yapmak zorunda olduğun için yapmaktır."
            ]
            secilen_motivasyon = random.choice(motivasyonlar)

            zengin_yorumlar = {
                0: {"baslik": "BAŞLANGIÇ SEVİYESİ", "analiz": f"Henüz yolun başındayız. Toplam {tyt_net} net ile temel atma dönemindesin.", "hedef": f"🎯 HEDEF: {hedef_net:.1f} NET", "strateji_baslik": "Temel Kampı", "strateji_detay": "• Youtube'dan 0'dan Matematik kamplarını bitir.\n• Günde en az 4 saat masa başında kalmalısın."},
                1: {"baslik": "GELİŞİME AÇIK", "analiz": f"Netlerin ({tyt_net} TYT) dalgalı bir seyir izliyor. Konu eksiğinden ziyade pratik eksiğin var.", "hedef": f"🎯 HEDEF: {hedef_net:.1f} NET", "strateji_baslik": "Soru Bankası Tarama", "strateji_detay": f"• {ozel_uyari if ozel_uyari else 'Haftada 2 farklı yayından deneme çöz.'}\n• Yapamadığın soruları kesip 'Hata Defteri' oluştur."},
                2: {"baslik": "ORTA - İYİ SEVİYE", "analiz": f"Güzel! {tyt_net} net bandına oturdun. Artık 'bilmiyorum' dediğin konu azdır, 'dikkat etmedim' dediğin soru çoktur.", "hedef": f"🎯 HEDEF: {hedef_net:.1f} NET", "strateji_baslik": "Branş Denemeleri", "strateji_detay": f"• {ozel_uyari if ozel_uyari else 'Süre tutarak branş denemesi çöz (Türkçe 40dk, Mat 60dk).'}"},
                3: {"baslik": "ÇOK İYİ (HIZ VE DİKKAT)", "analiz": f"Tebrikler! {tyt_net} net ile üst dilimdesin. Senin ilacın artık konu çalışmak değil, 'Sınav Yönetimi'.", "hedef": f"🎯 HEDEF: {hedef_net + 2:.1f} NET", "strateji_baslik": "Turlama Taktiği", "strateji_detay": f"• {ozel_uyari if ozel_uyari else 'Turlama taktiğini mutlaka uygula.'}\n• Zor kaynaklara (Apotsmi, 3D) geçiş yap."},
                4: {"baslik": "DERECE ÖĞRENCİSİ", "analiz": f"Mükemmel ({tyt_net} TYT). Artık rakiplerinle değil, kendinle yarışıyorsun.", "hedef": f"🎯 HEDEF: FULLEMEK", "strateji_baslik": "Nokta Atışı", "strateji_detay": "• MEB kitaplarındaki 'kıyıda köşede kalmış' detayları oku.\n• Günde 1 tane 'Zor Genel Deneme' çöz."}
            }
            
            analiz_veri = zengin_yorumlar.get(sinif_id, zengin_yorumlar[0])
            analiz_veri["psikoloji"] = secilen_motivasyon
            
            ek_rapor = "\n\n--- 🧠 DERS BAZLI AI ANALİZİ ---\n"
            ek_rapor += f"📚 Türkçe: {yorum_turkce}\n"
            ek_rapor += f"📐 Matematik: {yorum_mat}\n"
            ek_rapor += f"🧪 Fen: {yorum_fen}\n"
            ek_rapor += f"🌍 Sosyal: {yorum_sos}\n"
            
            if ozel_uyari:
                ek_rapor += f"\n🔥 KRİTİK TESPİT: {ozel_uyari}\n"

            analiz_veri['strateji_detay'] += ek_rapor

            haftalik_program = self.program_olusturucu.analiz_yap(sinif_id, eksik_konular_str)
            return analiz_veri, haftalik_program

        except Exception as e:
            print(f"Hata oluştu: {e}")
            return (None, [])

# --- 4. KULLANICI ARAYÜZÜ (Presentation Layer) ---
class YKSAsistaniUI:
    def __init__(self, root):
        self.root = root
        self.root.title("TÜBİTAK 2209-A | Kişisel Sınav Asistanı")
        self.root.geometry("1400x900")
        self.root.configure(bg=UygulamaAyarlari.RENKLER["BG"])
        
        self.db_yoneticisi = VeriTabaniYoneticisi()
        self.karar_sistemi = KararDestekSistemi()
        
        # Kullanıcı Adı değişkeni
        self.kullanici_adi = "Öğrenci" 

        self._stil_ayarla()
        # Uygulama açılışında direkt Giriş Ekranını çağırıyoruz
        self._giris_ekrani_olustur()

    def _giris_ekrani_olustur(self):
        """Uygulama açılışında gelen karşılama ekranı."""
        self.giris_frame = tk.Frame(self.root, bg=UygulamaAyarlari.RENKLER["LOGIN_BG"])
        self.giris_frame.pack(fill="both", expand=True)

        # Orta Alan
        center_frame = tk.Frame(self.giris_frame, bg=UygulamaAyarlari.RENKLER["LOGIN_BG"])
        center_frame.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(center_frame, text="YKS ANALİZ ASİSTANI", font=("Segoe UI", 30, "bold"), fg="white", bg=UygulamaAyarlari.RENKLER["LOGIN_BG"]).pack(pady=20)

        # Rastgele Motivasyon Sözü
        soz = random.choice(UygulamaAyarlari.MOTIVASYON_SOZLERI)
        tk.Label(center_frame, text=f"\"{soz}\"", font=("Segoe UI", 12, "italic"), fg="#ecf0f1", bg=UygulamaAyarlari.RENKLER["LOGIN_BG"], wraplength=600).pack(pady=(0, 40))

        # İsim Giriş Alanı
        tk.Label(center_frame, text="Adınız ve Soyadınız:", font=("Segoe UI", 11), fg="#bdc3c7", bg=UygulamaAyarlari.RENKLER["LOGIN_BG"]).pack(anchor="w", padx=45)
        
        self.ent_ad_soyad = tk.Entry(center_frame, font=("Segoe UI", 14), width=25, justify="center")
        self.ent_ad_soyad.pack(pady=5, ipady=5)
        self.ent_ad_soyad.bind("<Return>", lambda event: self._giris_yap()) # Enter tuşu ile giriş

        btn_giris = tk.Button(center_frame, text="🚀 BAŞLA", font=("Segoe UI", 12, "bold"), bg="#27ae60", fg="white", activebackground="#2ecc71", activeforeground="white", relief="flat", cursor="hand2", command=self._giris_yap)
        btn_giris.pack(pady=20, fill="x", padx=40, ipady=5)

    def _giris_yap(self):
        """Giriş butonuna basılınca çalışır."""
        isim = self.ent_ad_soyad.get().strip()
        if not isim:
            messagebox.showwarning("Eksik Bilgi", "Lütfen adınızı giriniz, size nasıl hitap edeceğimi bilmeliyim! 🙂")
            return
        
        self.kullanici_adi = isim.title()
        self.giris_frame.destroy() # Giriş ekranını yok et
        self._arayuz_olustur() # Ana arayüzü kur
        self.sayfa_analiz(None)

    def _arayuz_olustur(self):
        self.main_container = tk.Frame(self.root, bg=UygulamaAyarlari.RENKLER["BG"])
        self.main_container.pack(fill="both", expand=True)

        self.sidebar = tk.Frame(self.main_container, bg=UygulamaAyarlari.RENKLER["SIDEBAR"], width=250)
        self.sidebar.pack(side="left", fill="y")
        
        # Kullanıcıya özel hitap
        tk.Label(self.sidebar, text=f"Merhaba,\n{self.kullanici_adi}", bg=UygulamaAyarlari.RENKLER["SIDEBAR"], fg="#f1c40f", font=("Segoe UI", 14, "bold")).pack(pady=(40, 5))
        tk.Label(self.sidebar, text="YKS ASİSTANI", bg=UygulamaAyarlari.RENKLER["SIDEBAR"], fg="white", font=("Segoe UI", 10)).pack(pady=(0, 30))
        
        self.btn_yeni = tk.Button(self.sidebar, text="📝 YENİ DENEME", bg="#34495e", fg="white", font=("Segoe UI", 11), relief="flat", command=self.sayfa_yeni_giris)
        self.btn_yeni.pack(fill="x", pady=5, padx=10)
        
        self.btn_analiz = tk.Button(self.sidebar, text="📊 ANALİZ PANELİ", bg="#34495e", fg="white", font=("Segoe UI", 11), relief="flat", command=lambda: self.sayfa_analiz(None))
        self.btn_analiz.pack(fill="x", pady=5, padx=10)

        self.content_area = tk.Frame(self.main_container, bg=UygulamaAyarlari.RENKLER["BG"])
        self.content_area.pack(side="right", fill="both", expand=True, padx=20, pady=20)

    def _stil_ayarla(self):
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("TNotebook", background=UygulamaAyarlari.RENKLER["BG"], borderwidth=0)
        style.configure("TNotebook.Tab", font=("Segoe UI", 10, "bold"), padding=[15, 5])
        style.configure("Treeview", font=("Segoe UI", 9), rowheight=40) 
        style.configure("Treeview.Heading", font=("Segoe UI", 10, "bold"), background="#ecf0f1")

    def temizle_content(self):
        for widget in self.content_area.winfo_children():
            widget.destroy()

    def sayfa_yeni_giris(self):
        self.temizle_content()
        
        lbl_baslik = tk.Label(self.content_area, text="YENİ DENEME GİRİŞİ", font=("Segoe UI", 24, "bold"), bg=UygulamaAyarlari.RENKLER["BG"], fg=UygulamaAyarlari.RENKLER["TEXT"])
        lbl_baslik.pack(anchor="w", pady=(0, 20))

        fr_ust = tk.Frame(self.content_area, bg=UygulamaAyarlari.RENKLER["BG"])
        fr_ust.pack(fill="x", pady=10)
        
        tk.Label(fr_ust, text="Deneme Adı:", bg=UygulamaAyarlari.RENKLER["BG"], font=("Segoe UI", 10)).pack(side="left")
        self.ent_deneme = ttk.Entry(fr_ust, width=30)
        self.ent_deneme.pack(side="left", padx=10)
        
        tk.Label(fr_ust, text="Tarih:", bg=UygulamaAyarlari.RENKLER["BG"], font=("Segoe UI", 10)).pack(side="left", padx=10)
        self.ent_tarih = ttk.Entry(fr_ust, width=15)
        self.ent_tarih.insert(0, str(datetime.date.today()))
        self.ent_tarih.pack(side="left")

        notebook = ttk.Notebook(self.content_area)
        notebook.pack(fill="both", expand=True, pady=10)

        self.tab_netler = tk.Frame(notebook, bg="white")
        self.tab_konular = tk.Frame(notebook, bg="white")
        
        notebook.add(self.tab_netler, text="  Net Girişi  ")
        notebook.add(self.tab_konular, text="  Konu Eksikleri  ")

        dersler = [
            ("TYT Türkçe (40 Soru)", "tyt_turk"), 
            ("TYT Matematik (40 Soru)", "tyt_mat"), 
            ("TYT Sosyal (20 Soru)", "tyt_sos"), 
            ("TYT Fen (20 Soru)", "tyt_fen"),
            ("AYT Matematik (40 Soru)", "ayt_mat"), 
            ("AYT Fizik (14 Soru)", "ayt_fiz"), 
            ("AYT Kimya (13 Soru)", "ayt_kim"), 
            ("AYT Biyoloji (13 Soru)", "ayt_biyo"),
            ("AYT Edebiyat (24 Soru)", "ayt_edeb"), 
            ("AYT Tarih-1 (10 Soru)", "ayt_tar1"), 
            ("AYT Coğrafya-1 (6 Soru)", "ayt_cog1"), 
            ("AYT Tarih-2 (11 Soru)", "ayt_tar2"),
            ("AYT Coğrafya-2 (11 Soru)", "ayt_cog2"), 
            ("AYT Felsefe (12 Soru)", "ayt_fel"), 
            ("AYT Din Kültürü (6 Soru)", "ayt_din")
        ]
        
        self.entry_dict = {}
        tk.Label(self.tab_netler, text="Ders", font=("Segoe UI", 10, "bold"), bg="white").grid(row=0, column=0, padx=20, pady=10, sticky="w")
        tk.Label(self.tab_netler, text="Doğru", font=("Segoe UI", 10, "bold"), bg="white", fg="green").grid(row=0, column=1)
        tk.Label(self.tab_netler, text="Yanlış", font=("Segoe UI", 10, "bold"), bg="white", fg="red").grid(row=0, column=2)
        tk.Label(self.tab_netler, text="Boş", font=("Segoe UI", 10, "bold"), bg="white", fg="gray").grid(row=0, column=3)

        for i, (ad, kod) in enumerate(dersler):
            tk.Label(self.tab_netler, text=ad, bg="white", font=("Segoe UI", 10)).grid(row=i+1, column=0, padx=20, pady=5, sticky="w")
            e_d = ttk.Entry(self.tab_netler, width=7)
            e_d.grid(row=i+1, column=1, padx=5)
            e_y = ttk.Entry(self.tab_netler, width=7)
            e_y.grid(row=i+1, column=2, padx=5)
            e_b = ttk.Entry(self.tab_netler, width=7)
            e_b.grid(row=i+1, column=3, padx=5)
            self.entry_dict[f"{kod}_d"] = e_d
            self.entry_dict[f"{kod}_y"] = e_y
            self.entry_dict[f"{kod}_b"] = e_b

        nb_konular = ttk.Notebook(self.tab_konular)
        nb_konular.pack(fill="both", expand=True, padx=10, pady=10)

        self.tab_tyt_konu = tk.Frame(nb_konular, bg="#ecf0f1")
        self.tab_ayt_konu = tk.Frame(nb_konular, bg="#ecf0f1")
        
        nb_konular.add(self.tab_tyt_konu, text="  TYT Konuları  ")
        nb_konular.add(self.tab_ayt_konu, text="  AYT Konuları  ")
        
        self.check_vars = {}

        self._create_scrollable_area(self.tab_tyt_konu, UygulamaAyarlari.KONU_HAVUZU["TYT"])
        self._create_scrollable_area(self.tab_ayt_konu, UygulamaAyarlari.KONU_HAVUZU["AYT"])

        btn_kaydet = tk.Button(self.content_area, text="SONUÇLARI KAYDET", bg=UygulamaAyarlari.RENKLER["CARD_BLUE"], fg="white", font=("Segoe UI", 12, "bold"), command=self.verileri_kaydet)
        btn_kaydet.pack(fill="x", pady=10)

    def _create_scrollable_area(self, parent_tab, konu_data):
        canvas = tk.Canvas(parent_tab, bg="#ecf0f1")
        scrollbar = ttk.Scrollbar(parent_tab, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg="#ecf0f1")
        scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        col_counter = 0
        row_counter = 0
        for ders_adi, konular in konu_data.items():
            fr_ders = tk.LabelFrame(scrollable_frame, text=ders_adi, bg="white", font=("Segoe UI", 10, "bold"), padx=10, pady=10)
            fr_ders.grid(row=row_counter, column=col_counter, padx=10, pady=10, sticky="nw")
            for konu in konular:
                var = tk.IntVar()
                cb = tk.Checkbutton(fr_ders, text=konu, variable=var, bg="white", anchor="w")
                cb.pack(fill="x")
                self.check_vars[konu] = var
            col_counter += 1
            if col_counter > 2:
                col_counter = 0
                row_counter += 1

    def verileri_kaydet(self):
        try:
            ad = self.ent_deneme.get()
            tarih = self.ent_tarih.get()
            secilen_konular = [k for k, v in self.check_vars.items() if v.get() == 1]
            eksik_str = ", ".join(secilen_konular)
            
            veriler = [ad, tarih, eksik_str]
            ders_kodlari = [
                "tyt_turk", "tyt_mat", "tyt_sos", "tyt_fen", "ayt_mat", "ayt_fiz", "ayt_kim", "ayt_biyo",
                "ayt_edeb", "ayt_tar1", "ayt_cog1", "ayt_tar2", "ayt_cog2", "ayt_fel", "ayt_din"
            ]
            for kod in ders_kodlari:
                d = self.entry_dict[f"{kod}_d"].get()
                y = self.entry_dict[f"{kod}_y"].get()
                b = self.entry_dict[f"{kod}_b"].get()
                d_val = int(d) if d else 0
                y_val = int(y) if y else 0
                b_val = int(b) if b else 0
                veriler.extend([d_val, y_val, b_val])
            
            if len(veriler) != 48:
                messagebox.showerror("Hata", f"Sütun sayısı tutmuyor! Beklenen: 48, Olan: {len(veriler)}")
                return

            self.db_yoneticisi.veri_ekle(tuple(veriler))
            messagebox.showinfo("Başarılı", "Deneme başarıyla kaydedildi!")
            self.sayfa_analiz(None)
        except ValueError:
            messagebox.showerror("Hata", "Lütfen sayısal değerler giriniz.")
        except Exception as e:
            messagebox.showerror("Kritik Hata", str(e))

    def sayfa_analiz(self, secilen_indeks=None):
        self.temizle_content()
        
        df = self.db_yoneticisi.tum_verileri_al()
        if df.empty:
            tk.Label(self.content_area, text="Henüz veri yok. Önce 'Yeni Deneme' kısmından giriş yapın.", font=("Segoe UI", 14), bg=UygulamaAyarlari.RENKLER["BG"]).pack(pady=50)
            return

        fr_secim = tk.Frame(self.content_area, bg=UygulamaAyarlari.RENKLER["BG"])
        fr_secim.pack(fill="x", pady=(0, 20))
        
        tk.Label(fr_secim, text="İncelenecek Deneme:", bg=UygulamaAyarlari.RENKLER["BG"], font=("Segoe UI", 10, "bold")).pack(side="left", padx=(0, 10))
        
        deneme_listesi = [f"{row['deneme_adi']} ({row['tarih']})" for index, row in df.iterrows()]
        
        combo_denemeler = ttk.Combobox(fr_secim, values=deneme_listesi, width=40, state="readonly")
        combo_denemeler.pack(side="left")
        
        aktif_indeks = len(df) - 1 if secilen_indeks is None else secilen_indeks
        combo_denemeler.current(aktif_indeks)

        def deneme_degisti(event):
            self.sayfa_analiz(combo_denemeler.current())
        combo_denemeler.bind("<<ComboboxSelected>>", deneme_degisti)

        secilen_deneme = df.iloc[aktif_indeks]
        
        def net_hesapla(row, prefix): return row[f'{prefix}_d'] - (row[f'{prefix}_y'] / 4)
        
        tyt_net = sum([net_hesapla(secilen_deneme, k) for k in ["tyt_turk", "tyt_mat", "tyt_sos", "tyt_fen"]])
        ayt_net = sum([net_hesapla(secilen_deneme, k) for k in ["ayt_mat", "ayt_fiz", "ayt_kim", "ayt_biyo"]])
        
        turk_net = net_hesapla(secilen_deneme, "tyt_turk")
        mat_net = net_hesapla(secilen_deneme, "tyt_mat")
        fen_net = net_hesapla(secilen_deneme, "tyt_fen")
        sos_net = net_hesapla(secilen_deneme, "tyt_sos")
        
        tyt_puan = 100 + (tyt_net * 3.3)
        sayisal_puan = 100 + (tyt_net * 1.32) + (ayt_net * 3.0)

        fr_dashboard = tk.Frame(self.content_area, bg=UygulamaAyarlari.RENKLER["BG"])
        fr_dashboard.pack(fill="x", pady=10)
        
        self._create_card(fr_dashboard, "TYT NET", tyt_net, UygulamaAyarlari.RENKLER["CARD_BLUE"], 0)
        self._create_card(fr_dashboard, "AYT NET", ayt_net, UygulamaAyarlari.RENKLER["CARD_RED"], 1)
        self._create_card(fr_dashboard, "TYT PUAN", tyt_puan, UygulamaAyarlari.RENKLER["CARD_PURPLE"], 2)
        self._create_card(fr_dashboard, "SAYISAL PUAN", sayisal_puan, UygulamaAyarlari.RENKLER["CARD_PURPLE"], 3)

        fr_alt = tk.Frame(self.content_area, bg=UygulamaAyarlari.RENKLER["BG"])
        fr_alt.pack(fill="both", expand=True)

        analiz_veri, haftalik_program = self.karar_sistemi.analiz_yap(
            tyt_net, ayt_net, secilen_deneme['eksik_konular'], turk_net, mat_net, fen_net, sos_net
        )
        
        fr_ai = tk.LabelFrame(fr_alt, text="🤖 DETAYLI ANALİZ RAPORU", bg="white", font=("Segoe UI", 10, "bold"))
        fr_ai.pack(side="left", fill="both", expand=True, padx=(0, 10))
        
        txt_rapor = tk.Text(fr_ai, font=("Segoe UI", 10), bg="#fdfefe", fg="#2c3e50", relief="flat", padx=10, pady=10, wrap="word", height=10, width=40)
        txt_rapor.pack(fill="both", expand=True)
        txt_rapor.tag_configure("baslik", font=("Segoe UI", 12, "bold"), foreground="#d35400")
        txt_rapor.tag_configure("strateji", font=("Segoe UI", 11, "bold"), foreground="#2980b9")
        txt_rapor.tag_configure("hedef", font=("Segoe UI", 10, "bold"), foreground="#27ae60")
        txt_rapor.tag_configure("psikoloji", font=("Segoe UI", 9, "italic"), foreground="#7f8c8d")
        
        if analiz_veri:
            txt_rapor.insert("end", f"⚠️ DURUM: {analiz_veri['baslik']}\n", "baslik")
            txt_rapor.insert("end", f"{analiz_veri['analiz']}\n\n")
            txt_rapor.insert("end", f"{analiz_veri['hedef']}\n\n", "hedef")
            txt_rapor.insert("end", f"🎯 STRATEJİ: '{analiz_veri['strateji_baslik']}'\n", "strateji")
            txt_rapor.insert("end", f"{analiz_veri['strateji_detay']}\n\n")
            txt_rapor.insert("end", f"{analiz_veri['psikoloji']}", "psikoloji")
        else:
            txt_rapor.insert("end", "Analiz verisi oluşturulamadı.")
            
        txt_rapor.config(state="disabled")

        fr_program = tk.LabelFrame(fr_alt, text="📅 HAFTALIK AKILLI PROGRAM", bg="white", font=("Segoe UI", 10, "bold"))
        fr_program.pack(side="left", fill="both", expand=True, padx=(0, 10))

        cols = ("Gün", "Sabah (Rutin)", "Öğle (Odak)", "Akşam (Kapanış)")
        tree = ttk.Treeview(fr_program, columns=cols, show="headings", height=8)
        
        tree.heading("Gün", text="Gün")
        tree.heading("Sabah (Rutin)", text="🌅 Sabah Rutini")
        tree.heading("Öğle (Odak)", text="☀️ Ana Çalışma")
        tree.heading("Akşam (Kapanış)", text="🌙 Akşam Tekrarı")
        
        tree.column("Gün", width=70, anchor="center")
        tree.column("Sabah (Rutin)", width=130)
        tree.column("Öğle (Odak)", width=180)
        tree.column("Akşam (Kapanış)", width=150)
        
        for gun, sabah, ogle, aksam in haftalik_program:
            tree.insert("", "end", values=(gun, sabah, ogle, aksam))
            
        scrollbar = ttk.Scrollbar(fr_program, orient="vertical", command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side="right", fill="y")
        tree.pack(side="left", fill="both", expand=True, padx=5, pady=5)

        fr_grafik = tk.LabelFrame(fr_alt, text="NET GELİŞİMİ", bg="white", font=("Segoe UI", 10, "bold"))
        fr_grafik.pack(side="right", fill="both", expand=True)

        fig, ax = plt.subplots(figsize=(4, 3))
        df['tyt_genel'] = (df['tyt_turk_d'] - df['tyt_turk_y']/4) + (df['tyt_mat_d'] - df['tyt_mat_y']/4) + \
                          (df['tyt_sos_d'] - df['tyt_sos_y']/4) + (df['tyt_fen_d'] - df['tyt_fen_y']/4)
        
        ax.plot(df['deneme_adi'], df['tyt_genel'], marker='o', color='#e67e22', linewidth=2)
        ax.plot(secilen_deneme['deneme_adi'], tyt_net, marker='o', color='red', markersize=8)
        
        ax.set_title("TYT Net İlerlemesi", fontsize=8)
        ax.grid(True, alpha=0.3)
        
        canvas = FigureCanvasTkAgg(fig, master=fr_grafik)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True, padx=5, pady=5)

    def _create_card(self, parent, title, value, color, col_idx):
        fr = tk.Frame(parent, bg=color, width=250, height=100)
        fr.grid(row=0, column=col_idx, padx=10, sticky="ew")
        fr.pack_propagate(False)
        tk.Label(fr, text=title, bg=color, fg="white", font=("Segoe UI", 10, "bold")).pack(pady=(20, 5))
        tk.Label(fr, text=f"{value:.2f}", bg=color, fg="white", font=("Segoe UI", 20, "bold")).pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = YKSAsistaniUI(root)
    root.mainloop()
