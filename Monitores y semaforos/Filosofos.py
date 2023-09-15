import threading
import time
import random

NUM_FILOSOFOS = 5

# Monitor para controlar el acceso a los tenedores
class TenedorMonitor:
    def __init__(self):
        self.tenedores = [threading.Semaphore(1) for _ in range(NUM_FILOSOFOS)]

    def tomar_tenedores(self, filosofo_id):
        self.tenedores[filosofo_id].acquire()
        self.tenedores[(filosofo_id + 1) % NUM_FILOSOFOS].acquire()

    def dejar_tenedores(self, filosofo_id):
        self.tenedores[filosofo_id].release()
        self.tenedores[(filosofo_id + 1) % NUM_FILOSOFOS].release()

# Monitor para controlar el estado de los filósofos
class FilosofoMonitor:
    def __init__(self):
        self.estados = ["pensando"] * NUM_FILOSOFOS

    def cambiar_estado(self, filosofo_id, nuevo_estado):
        self.estados[filosofo_id] = nuevo_estado

    def obtener_estado(self, filosofo_id):
        return self.estados[filosofo_id]

# Función para simular la acción de pensar
def pensar(filosofo_id, filosofo_monitor):
    while True:
        print(f"Filósofo {filosofo_id} está pensando.")
        time.sleep(random.uniform(0.1, 1.0))
        filosofo_monitor.cambiar_estado(filosofo_id, "hambriento")

# Función para simular la acción de comer
def comer(filosofo_id, filosofo_monitor, tenedor_monitor):
    while True:
        if filosofo_monitor.obtener_estado(filosofo_id) == "hambriento":
            print(f"Filósofo {filosofo_id} está tratando de comer.")
            tenedor_monitor.tomar_tenedores(filosofo_id)
            print(f"Filósofo {filosofo_id} está comiendo.")
            time.sleep(random.uniform(0.1, 1.0))
            tenedor_monitor.dejar_tenedores(filosofo_id)
            filosofo_monitor.cambiar_estado(filosofo_id, "pensando")

# Crear el monitor de tenedores y el monitor de filósofos
tenedor_monitor = TenedorMonitor()
filosofo_monitor = FilosofoMonitor()

# Crear hilos para los filósofos
filosofo_threads = [threading.Thread(target=pensar, args=(i, filosofo_monitor)) for i in range(NUM_FILOSOFOS)]
for i in range(NUM_FILOSOFOS):
    filosofo_threads.append(threading.Thread(target=comer, args=(i, filosofo_monitor, tenedor_monitor)))

# Iniciar los hilos
for thread in filosofo_threads:
    thread.start()

# Esperar a que todos los hilos terminen (esto sería en una aplicación más grande)
for thread in filosofo_threads:
    thread.join()
