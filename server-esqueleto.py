import socket

def server():
    # Obtener el hostname
    host = socket.gethostname()

    # Especificar el puerto para escuchar
    # TO DO

    # Crear un objeto socket
    s = socket.socket()

    # Bindear el socket al host y al puerto
    s.bind((host, port))

    # Escuchar conexiones ingresantes
    # TO DO

    # Aceptar conexiones entrantes
    c, address = s.accept()
    print(f"Connected to: {address}")

    newMsg = True
    while newMsg:
        # Recibir datos del cliente (hasta 1024 bytes)
        data = c.recv(1024).decode()

        # setear en newMsg si hay data nueva (si no, rompe el ciclo)
        newMsg = data:
        print(f"Recibido de cliente: {data}")

        # Obtener el input de usuario y enviar al cliente (usar response.encode())
        response = input("Enter response to send to client: ")
        # TO DO

    # Cerrar la conexión con el cliente
    # TO DO


if __name__ == "__main__":
    # Start the server
    server()
