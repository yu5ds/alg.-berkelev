import socket
import time

# Función de sincronización
def synchronize_time(clients):
    print("\n--- Iniciando sincronización ---")
    server_time = time.time()  # Tiempo del servidor
    differences = []

    # Recolecta tiempos de los clientes
    for client in clients:
        client.sendall(b"TIME")  # Solicitar tiempo del cliente
        client_time = float(client.recv(1024).decode())  # Recibir tiempo del cliente
        print(f"Tiempo recibido del cliente: {client_time:.2f}")
        differences.append(client_time - server_time)

    # Calcular la media de las diferencias
    average_difference = sum(differences) / len(clients)
    adjusted_time = server_time + average_difference
    print(f"\nTiempo promedio ajustado: {adjusted_time:.2f}")

    # Enviar el tiempo ajustado a los clientes
    for client in clients:
        client.sendall(f"SET {adjusted_time}".encode())  # Enviar tiempo ajustado

def main():
    # Crear servidor de sockets
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("0.0.0.0", 12345))
    server_socket.listen(3)
    print("Servidor Berkeley esperando conexiones...\n")

    # Conectar con los clientes
    clients = []
    while len(clients) < 3:
        client_socket, addr = server_socket.accept()
        print(f"Cliente conectado: {addr}")
        clients.append(client_socket)

    # Sincronizar los tiempos
    synchronize_time(clients)

    # Cerrar conexiones
    for client in clients:
        client.close()
    server_socket.close()

if __name__ == "__main__":
    main()
