# 🛡️ Real-Time Log Analysis & Alerting System

Bu proje, macOS ve Linux sistem loglarını anlık olarak izleyen, kritik güvenlik ihlallerini tespit eden ve yöneticiye saniyeler içinde e-posta uyarısı gönderen bir **SOC (Security Operations Center)** otomasyon çözümüdür.

## 📋 Proje Genel Bakışı
Sistem, yerel log dosyalarını (`.log`) sürekli tarayarak **Brute Force**, **Unauthorized Access (Yetkisiz Erişim)** ve **Privilege Escalation (Yetki Yükseltme)** gibi şüpheli aktiviteleri yakalar. Tespit edilen olaylar hem bir **SIEM (Splunk)** platformuna aktarılmaya hazır hale getirilir hem de **SMTP** protokolü üzerinden anlık bildirim olarak iletilir.

## ✨ Temel Özellikler
- **Gerçek Zamanlı İzleme:** `tail -f` mantığıyla çalışan, gecikmesiz log takibi.
- **Akıllı Filtreleme:** Log gürültüsünü (noise) minimize eden Regex tabanlı anahtar kelime eşleştirme.
- **Anlık Alarm Mekanizması:** Kritik bulgular için otomatik e-posta bildirimleri.
- **Veri Analitiği Hazırlığı:** Splunk entegrasyonu ile dashboard oluşturma ve olay korelasyonu imkanı.

## 🛠️ Teknolojiler ve Protokoller
- **Python:** Log ayrıştırma (parsing) ve otomasyon motoru.
- **Splunk:** Log yönetimi, görselleştirme ve arşivleme.
- **SMTP (Simple Mail Transfer Protocol):** Güvenli alarm iletimi.
- **Regex:** Spesifik saldırı paternlerinin tespiti.

## 🎯 Siber Güvenlik Kazanımları
Bu proje, manuel log inceleme süreçlerini otomitize ederek aşağıdaki metrikleri iyileştirmeyi hedefler:
* **MTTD (Mean Time to Detect):** Tehdidi fark etme süresini saniyelere indirir.
* **MTTR (Mean Time to Respond):** Olay müdahale sürecini hızlandırarak veri sızıntısı riskini azaltır.

## 🚀 Kurulum ve Kullanım
1. Projeyi klonlayın: `git clone https://github.com/kullaniciadi/SOC-Log-Alert-System.git`
2. `logAlert.py` dosyasındaki ilgili alanlara kendi e-posta ve uygulama şifrenizi girin.
3. Scripti çalıştırın: `python3 logAlert.py`
4. Test logları üretmek için terminal üzerinden `echo` veya `printf` komutlarını kullanabilirsiniz.
