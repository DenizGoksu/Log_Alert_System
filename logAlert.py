import time
import smtplib
from email.mime.text import MIMEText

# --- GÜVENLİ AYARLAR ---
LOG_PATH = "myLogs.log"  # Log dosyasının yolu
GMAIL_USER = "your_mail_adress@gmail.com"  # Buraya Gmail adresini yaz (Enter your mail adress.)
GMAIL_PASS = "gmail_app_passwd"  # Buraya Gmail uygulama şifresini yaz (Enter your Gmail app password.)
ALICI_MAIL = "alert_mail@example.com"   # Uyarıyı almak istediğin mail (The alert will be sent to this email address.)

def mail_at(log_icerigi):
    msg = MIMEText(f"Sistemde tehlikeli bir hareket yakalandı!\n\nOlay Detayı:\n{log_icerigi}")
    msg['Subject'] = "🚨 MAC GÜVENLİK ALARMI!"
    msg['From'] = GMAIL_USER
    msg['To'] = ALICI_MAIL

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(GMAIL_USER, GMAIL_PASS)
            server.send_message(msg)
            print("📧 Mail başarıyla gönderildi!")
    except Exception as e:
        print(f"❌ Hata oluştu: {e}")

def takip_et():
    # SADECE BU KRİTİK KELİMELER VARSA MAİL GİDECEK
    KRITIK_FILTRE = [
        "SECURITY_ALERT",           
        "auth failed",              
        "Invalid user",             
        "3 incorrect password",      
        "Sudoers",                  
        "denied",
        "root"                    
    ]

    print(f"🛡️ Filtreleme Aktif: Sadece şu kelimeler mail atılacak: {KRITIK_FILTRE}")
    
    with open(LOG_PATH, "r") as f:
        f.seek(0, 2)
        while True:
            satir = f.readline()
            if not satir:
                time.sleep(1)
                continue
            
            # Satırın içindeki kelimeleri kontrol et (büyük/küçük harf duyarsız)
            if any(kelime.lower() in satir.lower() for kelime in KRITIK_FILTRE):
                print(f"🚨 KRİTİK OLAY: {satir.strip()}")
                mail_at(satir)
            else:
                # Önemli olmayan loglar sadece terminalde kalır, mail kutunu kirletmez
                print(f"☁️ Bilgi Logu (Mail Atılmadı): {satir.strip()[:50]}...")

if __name__ == "__main__":
    try:
        takip_et()
    except KeyboardInterrupt:
        print("🛡️ Log takibi durduruldu.")
        exit()