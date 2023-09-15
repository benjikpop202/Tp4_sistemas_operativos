import threading
import time
import random

# Creamos un monitor simple usando un Lock de threading
monitor = threading.Lock()

# Creamos un búfer compartido con una lista
buffer = []
MAX_BUFFER_SIZE = 5

# Función del productor
def productor():
    while True:
        item = random.randint(1, 100)
        with monitor:
            if len(buffer) < MAX_BUFFER_SIZE:
                buffer.append(item)
                print(f"Productor produjo {item}. Búfer: {buffer}")
        time.sleep(random.uniform(0.1, 0.5))

# Función del consumidor
def consumidor():
    while True:
        with monitor:
            if len(buffer) > 0:
                item = buffer.pop(0)
                print(f"Consumidor consumió {item}. Búfer: {buffer}")
        time.sleep(random.uniform(0.1, 0.5))

# Creamos varios hilos productores y consumidores
num_productores = 2
num_consumidores = 2

productor_threads = [threading.Thread(target=productor) for _ in range(num_productores)]
consumidor_threads = [threading.Thread(target=consumidor) for _ in range(num_consumidores)]

# Iniciamos los hilos
for thread in productor_threads + consumidor_threads:
    thread.start()

# Esperamos a que todos los hilos terminen (esto sería en una aplicación más grande)
for thread in productor_threads + consumidor_threads:
    thread.join()
