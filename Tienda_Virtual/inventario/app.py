from flask import Flask,jsonify

app = Flask(__name__)

@app.route("/inventario")
def show_all():
      list = [
            {'id': 1, 'name': 'Libro 1','price':500000,'quantity':2},
            {'id': 1, 'name': 'Libro 2','price':21000,'quantity':5666},
            {'id': 1, 'name': 'Libro 3','price':60000,'quantity':100},
            {'id': 1, 'name': 'Libro 4','price':251000,'quantity':18},
            {'id': 1, 'name': 'Libro 5','price':10000,'quantity':147},
            ]
      return jsonify(results = list)


if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)