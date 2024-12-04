import uuid
import random
import qrcode
import csv

# Generiere 150 UUIDS
uuids = [str(uuid.uuid4()) for _ in range(150)]

# Gewinne und Nieten erstellen
prizes = ["Hauptgewinn"] * 5 + ["Gewinn"] * 45 + ["Niete"] * 100
random.shuffle(prizes)

# UUIDs und Gewinne verknüpfen
tombola_data = list(zip(uuids, prizes))

# Url erstellen
base_url = "https://tombola-xp22.onrender.com/redeem"
urls = [f"{base_url}?code={uid}" for uid, _ in tombola_data]

# QR-Codes erstellen und speichern
for i, url in enumerate(urls):
    qr = qrcode.make(url)
    qr.save(f"qr_code_{i+1}.png")

# Daten in CSV speichern
with open("tombola_data.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["UUID", "Gewinn"])
    writer.writerows(tombola_data)
