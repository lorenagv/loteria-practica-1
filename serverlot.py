import socket
import random
ip = '127.0.0.1'
puerto = 8013
respuestas = 2
aleatorio = random.randrange(10)

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def logicacliente(cliente):

    c_abierta = True
    while c_abierta:
        mensaje = (cliente.recv(1000).decode('utf-8'))
        print("la ip del cliente es",mensaje)
        mns2 = str(loteria(mensaje, aleatorio))
        mns = str.encode(mns2)
        cliente.send(mns)
        cliente.close()
        break


def loteria(numero, aleatorio):
    numero = numero.replace(".","")

    suma= 0
    for element in numero:
        suma += int(element)
        resto = suma% 10
    if resto == aleatorio:
        mns = ("TE HA TOCADO. EL NUMERO ERA ", resto)
    else:
        mns = ("NO TE HA TOCADO. TU NUMERO ERA ", resto)
        return mns

try:
    servidor.bind((ip, puerto))
    servidor.listen(respuestas)
    while True:

        print('Esperando conexion en {ip},{puerto}'.format(ip = ip, puerto = puerto))
        (cliente, direccion) = servidor.accept()
        print('Se ha conectado alguien')
        logicacliente(cliente)


except KeyboardInterrupt:
    cliente.close()
    servidor.close()
print('Cerrando el chat...')
