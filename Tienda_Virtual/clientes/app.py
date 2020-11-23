from flask import Flask, request, flash, url_for, redirect, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///DB_Tienda.sqlite3'
app.config['SECRET_KEY'] = "random string"

db = SQLAlchemy(app)

class clientes(db.Model):
   id = db.Column('cliente_id', db.Integer, primary_key = True)
   name = db.Column(db.String(100))

   def __init__(self, name):       
       self.name = name       

@app.route("/clientes")
def show_all():
      list = [
            {'id': 1, 'name': 'Tony Stark'},
            {'id': 2, 'name': 'Steve Rogers'},
            {'id': 3, 'name': 'Bruce Banner'}
            ]
      return jsonify(results = list)

# def clientes():
#     return 

if __name__ == "__main__":
    db.create_all()
    app.run(host='0.0.0.0',debug=True)