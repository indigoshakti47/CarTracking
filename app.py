from flask import Flask,render_template, url_for, flash, redirect, request, jsonify
from flask_socketio import SocketIO, emit
from send_sms import send_message

# Configuracion basica del servidor en Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = '9f3f918414c3b8f36c904aa6085d019c'
app.debug = True
app.host = '0.0.0.0'
socketio = SocketIO(app)


# Ruta por defecto en http://127.0.0.1:5000/
@app.route("/")
def hello():
   return app.send_static_file('index.html')

# SocketIO: aquí se manejan los mensajes entrantes
# y salientes del servidor, este es el socket que
# recibe las señales del archivo arduino.py
@socketio.on('proximity')
def handle_proximity(proximity):
   print(proximity)

   if proximity["data"] >= 250:
      send_message()

   emit("position_update", {"data": proximity["data"]}, broadcast=True)

if __name__ == '__main__':
   socketio.run(app)