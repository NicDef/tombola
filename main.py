from flask import Flask, request
import csv

app = Flask(__name__)

# Lade Tombola-Daten (UUIDS und Gewinne)
with open("tombola_data.csv", "r") as f:
    tombola_dict = dict(csv.reader(f))


@app.route("/redeem")
def redeem():
    code = request.args.get("code")
    if code in tombola_dict:
        result = str(tombola_dict[code])  # Hauptgewinn / Gewinn / Niete
        if result == "Hauptgewinn Nr. 1":
            return f"<h1>Herzlichen Glückwunsch! Du erhälst <b>Hauptgewinn Nr. 1</b>. Bitte zeige deinen QR-Code am Stand der Tombola vor, um den Gewinn zu erhalten."
        if result == "Hauptgewinn Nr. 2":
            return f"<h1>Herzlichen Glückwunsch! Du erhälst <b>Hauptgewinn Nr. 2</b>. Bitte zeige deinen QR-Code am Stand der Tombola vor, um den Gewinn zu erhalten."
        if result == "Hauptgewinn Nr. 3":
            return f"<h1>Herzlichen Glückwunsch! Du erhälst <b>Hauptgewinn Nr. 3</b>. Bitte zeige deinen QR-Code am Stand der Tombola vor, um den Gewinn zu erhalten."
        if result == "Hauptgewinn Nr. 4":
            return f"<h1>Herzlichen Glückwunsch! Du erhälst <b>Hauptgewinn Nr. 4</b>. Bitte zeige deinen QR-Code am Stand der Tombola vor, um den Gewinn zu erhalten."
        if result == "Hauptgewinn Nr. 5":
            return f"<h1>Herzlichen Glückwunsch! Du erhälst <b>Hauptgewinn Nr. 5</b>. Bitte zeige deinen QR-Code am Stand der Tombola vor, um den Gewinn zu erhalten."
        elif result == "Gewinn":
            return f"<h1>Herzlichen Glückwunsch zu einem <b>Gewinn</b>! Bitte zeige deinen QR-Code am Stand der Tombola vor, um den Gewinn zu erhalten."
        elif result == "Niete":
            return f"<h1>Leider eine <b>Niete</B>. Aber nicht traurig sein, das gesammelte Geld der Lose wird für einen gemeinnützigen Zweck verwendet."
    else:
        return "Ungültiger QR-Code. Melden Sie sich bitte beim Stand der Tombola"


@app.route("/")
def home():
    return f"<h1>Tombola am Ludwigsgymnasium</h1>"


if __name__ == "__main__":
    app.run(debug=True)
