from flask import Flask, request, flash, url_for, redirect, render_template,jsonify
from flask_sqlalchemy import SQLAlchemy
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pedidos.sqlite3'
app.config['SECRET_KEY'] = "random string"

db = SQLAlchemy(app)

class pedidos(db.Model):
      id = db.Column('pedido_id', db.Integer, primary_key = True)
      cliente_id = db.Column(db.Integer)
      producto_id = db.Column(db.Integer)
      cantidad = db.Column(db.Integer)
      fecha = db.Column(db.String(100))

      def __init__(self, id_cliente,id_producto,cantidad,fecha):
            self.id_cliente = id_cliente
            self.id_producto = id_producto
            self.cantidad = cantidad
            self.fecha = fecha

@app.route("/pedido", methods=["GET","POST"])
def save_pedido():     
      if request.method == 'POST':
          data = request.get_json()
          cliente = data.get("cliente")
          producto = data.get("producto")
          cantidad = data.get("cantidad") 
          fecha = datetime.date.today()
          nuevo_pedido = pedidos(cliente,producto,cantidad,fecha)
          db.session.add(nuevo_pedido)
          db.session.commit()
          return jsonify({"response":"OK"})  
            
if __name__ == "__main__":
      db.create_all()
      app.run(host='0.0.0.0',debug=True)
