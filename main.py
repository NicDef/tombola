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
        return f"{tombola_dict[code]}"
    else:
        return "Ungültiger QR-Code. Melden Sie sich bitte beim Stand der Tombola"


if __name__ == "__main__":
    app.run(debug=True)
