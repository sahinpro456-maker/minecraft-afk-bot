from pycraft import Connection
import time

# ------------------------------
# Ayarlar
SERVER_IP = "oyna.hanedanmc.com"
SERVER_PORT = 25565
USERNAME = "adam123"
TPA_TARGET = "imparator1"
# ------------------------------

# Bağlantı oluştur
bot = Connection(SERVER_IP, SERVER_PORT, username=USERNAME)

# TPA gönderme fonksiyonu
def send_tpa(target_name):
    cmd = f"/tpa {target_name}"
    print(f"TPA gönderiliyor: {cmd}")
    bot.chat(cmd)

if __name__ == "__main__":
    bot.connect()        # Sunucuya bağlan
    time.sleep(3)        # Bağlantı stabil olsun
    send_tpa(TPA_TARGET) # TPA at
    print("Bot hazır, sadece TPA gönderdi ve hareketsiz duruyor.")

    # Sonsuz bekleme → bot açık kalsın (hareketsiz)
    try:
        while True:
            time.sleep(60)  # Her 60 saniye bir bekle
    except KeyboardInterrupt:
        print("Bot durduruldu.")
