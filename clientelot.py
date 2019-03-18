import socket

ip = '127.0.0.1'
puerto = 8013

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    cliente.connect((ip, puerto))
    print('Bienvenido al chat!')

    c_abierta = True
    while c_abierta:
        ipn = str.encode(ip)
        cliente.send(ipn)
        a = cliente.recv(1000).decode('utf-8')
        print(a)
        cliente.close()
        break

except KeyboardInterrupt:
    cliente.close()
print('Cerrando el chat...')
