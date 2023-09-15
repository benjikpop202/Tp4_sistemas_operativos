import threading
import time
import random

# Monitor para controlar el acceso al recurso compartido
class RWMonitor:
    def __init__(self):
        self.readers = 0  # Número de lectores leyendo actualmente
        self.resource = 0  # El recurso compartido
        self.lock = threading.Lock()  # Lock para controlar el acceso al monitor
        self.reader_sem = threading.Semaphore(1)  # Semáforo para sincronizar lectores

    def read(self, reader_id):
        with self.lock:
            self.readers += 1
            if self.readers == 1:
                self.reader_sem.acquire()  # Bloquear a los escritores si hay lectores

        # Leyendo el recurso compartido
        print(f"Lector {reader_id} está leyendo el recurso: {self.resource}")
        time.sleep(random.uniform(0.1, 0.5))

        with self.lock:
            self.readers -= 1
            if self.readers == 0:
                self.reader_sem.release()  # Liberar el semáforo si no hay más lectores

    def write(self, writer_id):
        self.reader_sem.acquire()  # Bloquear a los lectores
        # Escribiendo en el recurso compartido
        new_value = random.randint(1, 100)
        print(f"Escritor {writer_id} está escribiendo en el recurso: {new_value}")
        self.resource = new_value
        time.sleep(random.uniform(0.1, 0.5))
        self.reader_sem.release()  # Liberar a los lectores

# Función para simular un lector
def lector(reader_id, monitor):
    while True:
        monitor.read(reader_id)
        time.sleep(random.uniform(0.1, 0.5))

# Función para simular un escritor
def escritor(writer_id, monitor):
    while True:
        monitor.write(writer_id)
        time.sleep(random.uniform(0.1, 0.5))

# Crear el monitor y los hilos de lectores y escritores
monitor = RWMonitor()
num_lectores = 3
num_escritores = 2

lector_threads = [threading.Thread(target=lector, args=(i, monitor)) for i in range(num_lectores)]
escritor_threads = [threading.Thread(target=escritor, args=(i, monitor)) for i in range(num_escritores)]

# Iniciar los hilos
for thread in lector_threads + escritor_threads:
    thread.start()

# Esperar a que todos los hilos terminen (esto sería en una aplicación más grande)
for thread in lector_threads + escritor_threads:
    thread.join()
