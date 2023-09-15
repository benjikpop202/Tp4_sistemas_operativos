# Tp 4 "concurrencias"
## participantes:
### Teoria: Gustavo Piriz
### código: Benjamin Sobarzo
1. El problema de la sección crítica es un concepto importante en la programación concurrente y se refiere a la situación en la que múltiples procesos o hilos de ejecución intentan acceder y modificar recursos compartidos de forma simultánea. Cuando varios procesos comparten datos o recursos, como variables globales, archivos, bases de datos o cualquier otro recurso compartido, existe el riesgo de que los resultados sean incoherentes o no deseados debido a la concurrencia. Para evitar este problema, se debe garantizar que solo un proceso pueda acceder y modificar un recurso compartido en un momento dado, creando una sección crítica.

Para resolver el problema de la sección crítica, se utilizan mecanismos de exclusión mutua, como semáforos, mutex (mutual exclusión), o bloqueos, para coordinar el acceso a la sección crítica. *falta seudocódigo.

2.los semáforos son una herramienta fundamental en la programación concurrente para garantizar la sincronización y evitar problemas de concurrencia. Existen 2 tipos de semáforos a) Los semáforos binarios se utilizan para casos simples de exclusión mutua y señalización.
b) los semáforos contadores se emplean en situaciones más complejas donde se deben gestionar múltiples recursos o tareas concurrentes.
Diferencias clave entre los dos tipos de semáforos:

Un semáforo es un mecanismo de sincronización utilizado en programación concurrente y sistemas operativos para coordinar el acceso a recursos compartidos entre múltiples procesos o hilos de ejecución. Los semáforos se utilizan para evitar problemas de concurrencia, como las condiciones de carrera y la exclusión mutua, garantizando que solo un proceso pueda acceder a una sección crítica en un momento dado.
Existen dos tipos principales de semáforos:
a) Semáforos Binarios (Semaphore Binario): Estos son semáforos que pueden tomar solo dos valores: 0 o 1. Se utilizan principalmente para implementar la exclusión mutua, donde un proceso adquiere el semáforo (lo establece en 1) para entrar en una sección crítica y lo libera (lo establece en 0) al salir de la sección crítica. Los semáforos binarios se pueden usar para controlar la sincronización entre dos procesos o para señalar la disponibilidad de un recurso compartido.
b) Semáforos Contadores (Contador Semaphore): Estos son semáforos que pueden tomar valores enteros no negativos, es decir, pueden ser mayores que 1. Los semáforos contadores se utilizan para controlar el acceso a un número limitado de recursos o para coordinar tareas en sistemas multitarea. Pueden aumentar su valor cuando se libera un recurso y disminuirlo cuando se solicita uno.
Diferencias clave entre los dos tipos de semáforos:
Valores permitidos: Los semáforos binarios solo pueden tomar los valores 0 y 1, mientras que los semáforos contadores pueden tomar valores mayores que 1.
Uso principal: Los semáforos binarios se utilizan principalmente para lograr exclusión mutua y señalar la disponibilidad de recursos compartidos. Los semáforos contadores se usan para gestionar un número limitado de recursos o para coordinar tareas en sistemas multitarea.
Operaciones: En los semáforos binarios, las operaciones principales son wait (espera) y signal (señal). En los semáforos contadores, además de estas operaciones, también hay una operación init para inicializar el valor del semáforo.
Espera bloqueante: Tanto en semáforos binarios como en semáforos contadores, la operación wait bloquea el proceso si el valor del semáforo es 0. Sin embargo, en los semáforos contadores, varios procesos pueden bloquearse antes de que el valor sea 0, lo que permite que múltiples procesos esperen recursos.
Señalización: La operación signal en semáforos binarios establece el valor del semáforo en 1, mientras que en los semáforos contadores puede aumentar el valor en 1 o en un valor especificado.
3.  falta el código.
4. Los monitores son un mecanismo de sincronización utilizado en programación concurrente para gestionar el acceso a recursos compartidos y proteger la integridad de los datos en entornos multi-hilo o multi-proceso se utilizan para resolver problemas de concurrencia de una manera más estructurada y segura que los semáforos. 
Un monitor encapsula datos compartidos que deben ser protegidos, Los procedimientos (o métodos) dentro de un monitor son los únicos medios para acceder a los datos compartidos. permiten la definición de variables de condición, que se utilizan para que los hilos esperen ciertas condiciones antes de continuar su ejecución.
los monitores ofrecen una abstracción de programación más segura y estructurada para gestionar recursos compartidos y sincronización en comparación con los semáforos, que son una herramienta más flexible pero propensa a errores si no se utiliza con precaución.
5. a. Problema del Búfer Limitado: En este problema, tienes un búfer (una especie de caja o almacén) que puede contener un número limitado de elementos, por ejemplo, números o datos. Hay dos tipos de procesos: productores y consumidores. Los productores ponen elementos en el búfer, mientras que los consumidores los sacan. El desafío es asegurarse de que los productores no pongan elementos cuando el búfer está lleno y de que los consumidores no saquen elementos cuando el búfer esté vacío.
b. Problema de los Lectores-Escritores: Este problema involucra un recurso compartido, como una base de datos o un archivo, que puede ser accedido por dos tipos de procesos: lectores y escritores. Los lectores pueden leer el recurso compartido al mismo tiempo, pero los escritores necesitan bloquear el recurso de manera exclusiva para escribir en él. El desafío es permitir que múltiples lectores accedan al recurso simultáneamente mientras garantizas que cuando un escritor está modificando el recurso, ningún lector o escritor más pueda interferir.
c. Problema de los Filósofos Comensales: Imagina que tienes cinco filósofos sentados alrededor de una mesa y cada uno tiene un plato de espaguetis frente a ellos. Entre cada par de filósofos hay un tenedor. Los filósofos tienen dos estados: pensar o comer. Para comer, un filósofo necesita dos tenedores, uno a su izquierda y otro a su derecha. El desafío es diseñar un sistema en el que los filósofos puedan alternar entre pensar y comer, evitando el hambre y los bloqueos mutuos.
*falta el código.
6. Sí, es posible, ya que Los monitores proporcionan una abstracción de programación de más alto nivel que encapsula datos compartidos y operaciones en esos datos, mientras que los semáforos son una herramienta de nivel más bajo para gestionar la sincronización. Combinarlos puede ser útil en situaciones donde necesitas un mayor control o flexibilidad en la sincronización.
*falta ejemplo.
7. Java:
  ofrece un sólido soporte para la concurrencia a través de su API de concurrencia multi-hilo. Algunos de los principales elementos que Java proporciona para gestionar la concurrencia son:
*Hilos (Threads): Java permite la creación de hilos de ejecución (threads) de manera eficiente. Puedes crear hilos utilizando la clase Thread o implementando la interfaz Runnable.
*Clases de Sincronización: Java proporciona clases como synchronized, ReentrantLock, Semaphore, y CountDownLatch para gestionar la sincronización entre hilos. El uso de bloques sincronizados o la anotación synchronized permite garantizar la exclusión mutua en secciones críticas.
*Clases y Métodos Atómicos: Java ofrece clases como AtomicInteger, AtomicBoolean, etc., que permiten operaciones atómicas sin necesidad de sincronización explícita.
*Mecanismos de Espera y Notificación: Java proporciona métodos como wait (), notify (), y notifyAll () para la comunicación entre hilos y la espera activa.
*Executor Framework: Java ofrece un framework de ejecutores que simplifica la gestión de hilos y tareas concurrentes mediante clases como ExecutorService.
               Python:
 también admite programación concurrente y paralela, pero su enfoque es diferente al de Java. Algunos de los mecanismos utilizados en Python incluyen:
*Módulo threading y multiprocessing: El módulo threading permite trabajar con hilos, mientras que multiprocessing permite trabajar con procesos. Python utiliza el concepto de GIL (Global Interpreter Lock), que restringe la ejecución de código Python a un solo hilo, incluso en sistemas multi-núcleo. Esto puede limitar la eficiencia de los hilos para ciertas tareas de concurrencia en Python debido a la presencia del GIL.
*Módulo asyncio (Python 3.5+): Para la programación asíncrona y la concurrencia basada en eventos, Python ofrece el módulo asyncio. Permite la creación de aplicaciones asincrónicas eficientes utilizando palabras clave como async y await.
*Locks y Semáforos: Python proporciona módulos como threading. Lock y multiprocessing. Semaphore para gestionar la exclusión mutua y la sincronización entre hilos y procesos.
PHP:
PHP, originalmente diseñado para la programación web, no tiene un soporte nativo para la concurrencia en el mismo sentido que Java o Python. Sin embargo, existen extensiones y bibliotecas de terceros que permiten abordar problemas de concurrencia en PHP:

*Extensión pthreads: La extensión pthreads permite la creación y gestión de hilos en PHP. Sin embargo, no es tan común ni tan utilizado como los mecanismos de concurrencia en Java o Python.

*Programación Asíncrona: PHP puede utilizar bibliotecas como ReactPHP o Swoole para habilitar la programación asíncrona y la concurrencia basada en eventos, lo que es especialmente útil en aplicaciones web.
8. El "pasaje de mensajes entre procesos" se refiere a la comunicación entre dos o más procesos en un sistema concurrente o distribuido mediante el intercambio de mensajes. En lugar de compartir directamente datos o variables, los procesos se envían mensajes para intercambiar información y coordinar su ejecución.
Ejemplo:
Supongamos que tienes dos procesos A y B en un sistema distribuido. Para que A envíe un mensaje a B, podría incluir un mensaje en una cola de mensajes compartida. B, por su parte, verificaría periódicamente esa cola y, cuando encuentre un mensaje de A, lo procesaría según sea necesario. Esto permite que los procesos se comuniquen sin acceder directamente a las variables o recursos del otro proceso, lo que puede ayudar a evitar problemas de concurrencia.
9. El interbloqueo, también conocido como bloqueo mutuo o "deadlock" en inglés, es una situación en la programación concurrente en la que dos o más procesos o hilos de ejecución quedan atrapados en un estado en el que ninguno de ellos puede avanzar. Cada proceso está esperando que ocurra algo que solo puede ser provocado por otro proceso, lo que resulta en un estancamiento permanente de la ejecución.
Ejemplo:
Imagina dos procesos, A y B, que necesitan acceder a dos recursos, X e Y, para completar sus tareas. A obtiene acceso a X y luego espera para adquirir Y antes de continuar. Al mismo tiempo, B obtiene acceso a Y y espera para adquirir X antes de continuar. Ninguno de los dos puede avanzar porque están bloqueados esperando el recurso que el otro tiene, lo que resulta en un interbloqueo. En esta situación, ambos procesos quedan atrapados indefinidamente.
10. La principal diferencia entre LiveLock y DeadLock es que, en un DeadLock, los procesos están completamente bloqueados y no pueden avanzar, mientras que, en un LiveLock, los procesos están activos pero no hacen progreso real debido a su interacción continua.
Ejemplo de DeadLock: 
Dos personas están caminando hacia el otro en un pasillo estrecho y, en lugar de moverse de lado para dejar pasar al otro, ambos se mantienen inmóviles, bloqueando el camino. Ninguno de los dos puede avanzar, y están completamente atascados.
Ejemplo de LiveLock:
 Imagina dos personas que se encuentran en un pasillo y se mueven de lado para dejar pasar al otro. Sin embargo, cada vez que una persona se mueve, la otra también se mueve en la misma dirección para evitar el bloqueo, lo que resulta en un patrón constante de moverse de un lado a otro sin hacer un progreso real. Ambas personas están activas, pero no avanzan debido a su interacción continua.

