import threading
import time
import random

class Cajero:
    def __init__(self):
        self.semaphore = threading.Semaphore(1)

    def usar_cajero(self, cliente):
        with self.semaphore:
            print(f"Cliente {cliente.nombre} está usando el cajero.")
            #los clientes tardaran un tiempo aleatorio con un maximo de 10 segundos
            tiempo_aleatorio = random.uniform(0, 10)
            time.sleep(tiempo_aleatorio)
            # Simulación de una operación en el cajero
            print(f"Cliente {cliente.nombre} ha completado su transacción.")
            #que espere un segundo antes de salir
            time.sleep(1)
        print(f"Cliente {cliente.nombre} ha dejado el cajero y está libre.")

class Cliente:
    def __init__(self, nombre, cajero):
        self.nombre = nombre
        self.cajero = cajero

    def usar_cajero(self):
        self.cajero.usar_cajero(self)


cajero = Cajero()


clientes = []

clientes.append(Cliente("Lucas", cajero))
clientes.append(Cliente("Benja", cajero))
clientes.append(Cliente("Gustavo",cajero))
clientes.append(Cliente("Mariano", cajero))
clientes.append(Cliente("Ricardo", cajero))


# Iniciar los hilos de los clientes para usar el cajero
threads_clientes = [threading.Thread(target=cliente.usar_cajero) for cliente in clientes] 

# Iniciar los hilos de los clientes
for thread_cliente in threads_clientes:
    thread_cliente.start()

# Esperar a que todos los clientes terminen
for thread_cliente in threads_clientes:
    thread_cliente.join()

print("Todos los clientes han terminado.")
