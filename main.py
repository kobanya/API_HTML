from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

termek_lista = [
    {
        "ID": 1,
        "termék neve": "Laptop",
        "leírása": "Hordozható számítógép nagy teljesítménnyel.",
        "ára": 359000
    },
    {
        "ID": 2,
        "termék neve": "Okostelefon",
        "leírása": "Modern okostelefon kiváló kamerával.",
        "ára": 199000
    },
    {
        "ID": 3,
        "termék neve": "Televízió",
        "leírása": "Nagy méretű HD televízió.",
        "ára": 300000
    },
    {
        "ID": 4,
        "termék neve": "Kávéfőző",
        "leírása": "Programozható kávéfőző.",
        "ára": 2300
    },
    {
        "ID": 5,
        "termék neve": "Hűtőszekrény",
        "leírása": "Nagy hűtőszekrény energiahatékonysággal.",
        "ára": 199500
    },
    {
        "ID": 6,
        "termék neve": "Mikrohullámú sütő",
        "leírása": "Mikrohullámú sütő gyors ételkészítéshez.",
        "ára": 60000
    },
    {
        "ID": 7,
        "termék neve": "Fényképezőgép",
        "leírása": "DSLR fényképezőgép professzionális felhasználóknak.",
        "ára": 299000
    },
    {
        "ID": 8,
        "termék neve": "Asztali számítógép",
        "leírása": "Erős asztali számítógép játékhoz és munkához.",
        "ára": 516000
    },
    {
        "ID": 9,
        "termék neve": "Vezeték nélküli egér",
        "leírása": "Kényelmes vezeték nélküli egér használathoz.",
        "ára": 9000
    },
    {
        "ID": 10,
        "termék neve": "Hangszóró rendszer",
        "leírása": "Magas minőségű hangszóró rendszer zenehallgatáshoz.",
        "ára": 99000
    }
]

@app.route('/')
def index():
    return render_template('termek_lista.html', termek_lista=termek_lista)

@app.route('/add_product', methods=['POST'])
def add_product():
    if request.method == 'POST':
        uj_termek_neve = request.form['product_name']
        uj_termek_leirasa = request.form['product_description']
        uj_termek_ara = float(request.form['product_price'])
        ID = termek_lista[-1]['ID'] + 1

        uj_termek = {
            "termék neve": uj_termek_neve,
            "leírása": uj_termek_leirasa,
            "ára": uj_termek_ara,
            "ID": ID
        }

        termek_lista.append(uj_termek)
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()
