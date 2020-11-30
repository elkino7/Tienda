from flask import Flask, request, flash, url_for, redirect, render_template,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inventario.sqlite3'
app.config['SECRET_KEY'] = "random string"

db = SQLAlchemy(app)
ma = Marshmallow(app)

class inventario(db.Model):
      id = db.Column('producto_id', db.Integer, primary_key = True)
      nombre = db.Column(db.String(100))
      precio = db.Column(db.Integer)
      cantidad = db.Column(db.Integer)

      def __init__(self, nombre,precio,cantidad):
            self.name = name

class inventarioSchema(ma.ModelSchema):
      class Meta:
            model = inventario

@app.route("/inventario")
def show_inv():     
      productoslista = inventario.query.all() 
      inventario_schema = inventarioSchema(many = True)
      output = inventario_schema.dump(productoslista)
      return jsonify(output)

if __name__ == "__main__":
      db.create_all()
      app.run(host='0.0.0.0',debug=True)
