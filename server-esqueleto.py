import socket

def server():
    # Obtener el hostname
    host = socket.gethostname()

    # Especificar el puerto para escuchar
    port = 1421

    # Crear un objeto socket
    s = socket.socket()

    # Bindear el socket al host y al puerto
    s.bind((host, port))

    # Escuchar conexiones ingresantes
    s.listen(5)

    # Aceptar conexiones entrantes
    c, address = s.accept()
    print(f"Connected to: {address}")

    newMsg = True
    while newMsg:
        # Recibir datos del cliente (hasta 1024 bytes)
        data = c.recv(1024).decode()

        # setear en newMsg si hay data nueva (si no, rompe el ciclo)
        if not data: break
        newMsg = data
        print(f"Recibido de cliente: {data}")

        # Obtener el input de usuario y enviar al cliente (usar response.encode())
        response = input("Enter response to send to client: ")
        c.send(response.encode())

    # Cerrar la conexión con el cliente
    s.close()


if __name__ == "__main__":
    # Start the server
    server()
