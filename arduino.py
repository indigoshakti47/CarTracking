# Aqui se importan las librerias necesarias para el
# funcionamiento del programa, serial se utiliza para
# la conexion con el dispositivo arduino y socketio
# para la conexion con el servidor,
import serial
import socketio
import time

# En esta sección se realiza la conexion con los
# Sockets del servidor remoto
sio = socketio.Client()
sio.connect('http://localhost:5000')

# En esta sección se realiza la conexion con el
# dispositivo arduino
arduino = serial.Serial('/dev/cu.usbmodem14101',9600)
counter = 0
output,output_backup = [],[]


# Aqui se comienza un bucle para recibir constantemente
# las señales producidas por el arduino
while True:
    # rawString son las señales detectadas del arduino,
    # vienen de la forma 'X-X-X-X-X-X-...X' donde X
    # simboliza los bits producidos por la casa inteligente
    rawString = str(arduino.readline(),'utf-8').replace("\n","")
    sio.emit("proximity", {"data": int(rawString)})
    print(int(rawString))
    time.sleep(0.2)
arduino.close()