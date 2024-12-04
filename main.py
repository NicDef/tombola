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
        if result == "Hauptgewinn":
            return f"<h1>Herzlichen Glückwunsch zu einem <b>Hauptgewinn</b>! Bitte zeige deinen QR-Code am Stand der Tombola vor, um den Gewinn zu erhalten."
        elif result == "Gewinn":
            return f"<h1>Herzlichen Glückwunsch zu einem <b>Gewinn</b>! Bitte zeige deinen QR-Code am Stand der Tombola vor, um den Gewinn zu erhalten."
        elif result == "Niete":
            return f"<h1>Leider eine <b>Niete</B>. Aber nicht traurig sein, das gesammelte Geld der Lose wird für einen gemeinnützigen Zweck verwendet."

        return f"{tombola_dict[code]}"
    else:
        return "Ungültiger QR-Code. Melden Sie sich bitte beim Stand der Tombola"


if __name__ == "__main__":
    app.run(debug=True)
