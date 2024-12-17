import socket
import time
import random

def simulate_time_offset():
    """ Simula un desfase de tiempo para los clientes """
    return time.time() + random.choice([10, -5, 15])  # Desfase de 10, -5, 15 segundos

def main():
    # Conectarse al servidor
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("server", 12345))

    while True:
        message = client_socket.recv(1024).decode()
        if message == "TIME":
            # Simular el tiempo desincronizado
            client_time = simulate_time_offset()
            print(f"Enviando tiempo simulado: {client_time:.2f}")
            client_socket.sendall(str(client_time).encode())
        elif message.startswith("SET"):
            _, adjusted_time = message.split()
            adjusted_time = float(adjusted_time)
            print(f"Tiempo ajustado recibido: {adjusted_time:.2f}")
            break

    client_socket.close()

if __name__ == "__main__":
    main()
