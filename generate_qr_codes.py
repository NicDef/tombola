import uuid
import random
import qrcode
import csv

# Gewinne und Nieten erstellen
prizes = (
    ["Hauptgewinn Nr. 1"]
    + ["Hauptgewinn Nr. 2"]
    + ["Hauptgewinn Nr. 3"]
    + ["Hauptgewinn Nr. 4"]
    + ["Hauptgewinn Nr. 5"]
    + ["Gewinn"] * 3
    + ["Niete"] * 3
)
random.shuffle(prizes)

# Generiere UUIDS
uuids = [str(uuid.uuid4()) for _ in range(len(prizes))]

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
