from flask import Flask, request, flash, url_for, redirect, render_template,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clientes.sqlite3'
app.config['SECRET_KEY'] = "random string"

db = SQLAlchemy(app)
ma = Marshmallow(app)

class clientes(db.Model):
      id = db.Column('cliente_id', db.Integer, primary_key = True)
      nombre = db.Column(db.String(100))

      def __init__(self, nombre):
            self.name = name

class clientesSchema(ma.ModelSchema):
      class Meta:
            model = clientes

@app.route("/clientes")
def show_clients():     
      clientelista = clientes.query.all() 
      clientes_schema = clientesSchema(many = True)
      output = clientes_schema.dump(clientelista)
      return jsonify(output)

if __name__ == "__main__":
      db.create_all()
      app.run(host='0.0.0.0',debug=True)
