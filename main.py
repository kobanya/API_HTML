from flask import Flask, render_template, request, redirect
import json

app = Flask(__name__)

# Az alkalmazás indításakor olvasd be az adatokat a JSON fájlból
def load_data():
    try:
        with open('termek_lista.json', 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
        return data
    except FileNotFoundError:
        return []

termek_lista = load_data()

# Főoldal, a terméklista megjelenítése
@app.route('/')
def index():
    return render_template('termek_lista.html', termek_lista=termek_lista)

# Új termék hozzáadása
@app.route('/add_product', methods=['POST'])
def add_product():
    if request.method == 'POST':
        # Új termék adatainak lekérése a formból
        uj_termek_neve = request.form['termék_neve']
        uj_termek_leirasa = request.form['leírás']
        uj_termek_ara = request.form['ára']

        # Az új termék objektum létrehozása
        ID = len(termek_lista) + 1
        uj_termek = {
            "ID": ID,
            "termék neve": uj_termek_neve,
            "leírás": uj_termek_leirasa,
            "ára": uj_termek_ara
        }

        # Az új termék hozzáadása a termek_lista-hoz
        termek_lista.append(uj_termek)

        # Az új termék mentése JSON fájlba
        with open('termek_lista.json', 'w', encoding='utf-8') as json_file:
            json.dump(termek_lista, json_file, ensure_ascii=False, indent=4)

        return redirect('/')




if __name__ == '__main__':
    app.run()
