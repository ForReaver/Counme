# @title
import random

print("🌍 Counme'ye Hoşgeldiniz! ")

baskentler = {
     "Türkiye": ["Ankara"],
    "Fransa": ["Paris"],
    "Japonya": ["Tokyo"],
    "Almanya": ["Berlin"],
    "İtalya": ["Roma", "Rome"],
    "Mısır": ["Kahire", "Cairo"],
    "İspanya": ["Madrid"],
    "İngiltere": ["Londra", "London"],
    "Rusya": ["Moskova", "Moscow"],
    "Çin": ["Pekin", "Beijing"],
    "ABD": ["Washington", "Washington DC", "Vaşington"],
    "Kanada": ["Ottava", "Ottawa"],
    "Brezilya": ["Brasilia"],
    "Arjantin": ["Buenos Aires"],
    "Avustralya": ["Kanberra", "Canberra"],
    "Hindistan": ["Yeni Delhi", "New Delhi"],
    "Güney Kore": ["Seul", "Seoul"],
    "Yunanistan": ["Atina", "Athens"],
    "İran": ["Tahran", "Tehran"],
    "Azerbaycan": ["Bakü", "Baku"],
    "Polonya": ["Varşova", "Warsaw"],
    "Portekiz": ["Lizbon", "Lisbon"],
    "Meksika": ["Meksiko", "Mexico City"],
    "Kazakistan": ["Astana"],
    "Suudi Arabistan": ["Riyad", "Riyadh"],
    "İsviçre": ["Bern"],
    "Norveç": ["Oslo"],
    "Avusturya": ["Viyana", "Vienna"],
    "Macaristan": ["Budapeşte", "Budapest"],
    "Pakistan": ["İslamabad", "Islamabad"]                                            
}

def duzelt(yazi):
  return yazi.replace("İ", "I").lower().strip()

sorular = random.sample(list(baskentler), 10)
puan = 0
seri = 0
en_uzun_seri = 0
dogru_sayisi = 0
yanlis_sayisi = 0

kombo_mesajlari = {

    2: "🔥 Isınıyorsun!",
    3: "🧭 Pusula Ustası!",
    4: "🗺️ Harita Senin Elinde!",
    5: "🛂 Pasaport Doldu, Sınır Tanımıyorsun!",
    6: "✈️ Dünya Turu Başladı!",
    7: "🕊️ Büyükelçi Geliyor!"

}

for ulke in sorular:
  dogrular = baskentler[ulke]
  cevap = input(ulke + " Ülkesinin başkenti neresidir? ")

  bildi = False
  for d in dogrular:
    if duzelt(cevap) == duzelt(d):
      bildi = True

  if bildi:
    seri += 1
    puan += 1
    dogru_sayisi += 1
    print("Doğru! 🎉 + 1 puan ")

    if seri > en_uzun_seri:
        en_uzun_seri = seri

    if seri >= 8:
      print("👑 Küresel Güç! Kimse Seni Durduramaz!")
    elif seri in kombo_mesajlari:
      print(kombo_mesajlari[seri])


    if seri >= 3:
      puan += 1
      print("⚡ Kombo bonusu: +1 puan")

  else:
    puan -= 1
    yanlis_sayisi += 1
    print("Yanlış, -1 puan, doğru cevap ", dogrular[0])
    if seri >= 2:
        print("💥 Diplomatik kriz! Seri Sıfırlandı!💥")
    seri = 0

  print("Puan Durumu:", puan, "/", len(sorular))
  print("🔥 Kombo:", seri)
  print("------")

if puan >= 15:
    unvan = "🌍 Dünya Lideri"
elif puan >= 10:
    unvan = "🎖️ Büyükelçi"
elif puan >= 5:
    unvan = "💼 Diplomat Adayı"
elif puan >= 0:
    unvan = "🎒 Turist"
else:
    unvan = "🧳 Pasaportunu Kaybetmiş Gezgin"

print()
print("==============================")
print("       🏁 OYUN BİTTİ 🏁")
print("==============================")
print("✅ Doğru:", dogru_sayisi)
print("❌ Yanlış:", yanlis_sayisi)
print("🔥 En uzun seri:", en_uzun_seri)
print("⭐ Toplam puan:", puan)
print("------------------------------")
print("Unvanın:", unvan)
print("==============================")
