def solicitudDeDatos():
    procesos = {
        1: 'Fotos',
        2: 'YouTube',
        3: 'Chrome',
        4: 'Xbox',
        5: 'Word',
        6: 'Excel',
        7: 'Zoom',
        8: 'Brave',
        9: 'Slack',
        10: 'Gmail',
    }
    numeroProcesos = int(input('\nIngrese el número de procesos que desea tener: (1-5):\n'))
    
    numeroProcesos = max(1, min(numeroProcesos, 5))
    
    rafagas = {}
    tiemposLlegada = {}
    for i in range(numeroProcesos):
        print('\n')
        print(procesos)
        print('\n')
        escogerProceso = int(input('Ingrese el número de proceso que desea añadir: '))
        
        while escogerProceso not in procesos:
            print("Número de proceso no válido. Por favor, intente de nuevo.")
            escogerProceso = int(input('Ingrese el número de proceso que desea añadir: '))

        proceso = procesos[escogerProceso]

        print('\nNOTA!!!\nEl tamaño de ráfaga máximo es de 15\n')
        escogerTamagnoRafaga = int(input('Ingrese el tamaño de ráfaga del proceso {}: '.format(proceso)))
        
        escogerTamagnoRafaga = max(1, min(escogerTamagnoRafaga, 15))
        
        rafagas[proceso] = escogerTamagnoRafaga
        tiemposLlegada[proceso] = i
        print('Lista de Procesos:')
        print(rafagas)
    return rafagas, tiemposLlegada

def fcfs(rafagas, tiemposLlegada):
    tiempoActual = 0
    tiemposEspera = {}
    tiemposFinalizacion = {}
    
    print("\nProceso\t\tRáfaga de CPU\tTiempo de Llegada\tTiempo de Espera\tTiempo de Finalización")
    
    for proceso, rafaga in rafagas.items():
        tiempoLlegada = tiemposLlegada[proceso]
        tiempoEspera = max(0, tiempoActual - tiempoLlegada)
        tiemposEspera[proceso] = tiempoEspera
        tiempoFinalizacion = tiempoActual + rafaga
        tiemposFinalizacion[proceso] = tiempoFinalizacion
        print("{}\t\t{}\t\t\t{}\t\t\t{}\t\t\t{}".format(proceso, rafaga, tiempoLlegada, tiempoEspera, tiempoFinalizacion))
        tiempoActual += rafaga
    
    promedioEspera = sum(tiemposEspera.values()) / len(tiemposEspera)
    promedioFinalizacion = sum(tiemposFinalizacion.values()) / len(tiemposFinalizacion)
    print("\nPromedio de Tiempo de Espera: {:.2f}".format(promedioEspera))
    print("Promedio de Tiempo de Finalización: {:.2f}".format(promedioFinalizacion))

def rr(rafagas, quantum):
    from collections import deque

    # Preparar las colas y diccionarios necesarios
    procesos = deque(rafagas.items())
    tiemposEspera = {proceso: 0 for proceso in rafagas}  # Tiempo esperado inicialmente en 0
    tiemposFinalizacion = {}  # Para almacenar el tiempo en el que cada proceso termina
    ciclos = {proceso: 0 for proceso in rafagas}  # Contador de ciclos para cada proceso
    tiempoActual = 0
    rafagasRestantes = rafagas.copy()  # Copia para manejar las ráfagas restantes

    # Mientras haya procesos pendientes
    while procesos:
        procesoActual, rafagaActual = procesos.popleft()

        # Si el proceso ya está terminado, saltarlo
        if rafagaActual <= 0:
            continue

        # Contabilizar ciclo
        ciclos[procesoActual] += 1

        # Ejecutar proceso
        ejecutado = min(rafagaActual, quantum)
        tiempoActual += ejecutado
        rafagasRestantes[procesoActual] -= ejecutado

        # Actualizar tiempos de espera para los demás procesos
        for proceso in procesos:
            if rafagasRestantes[proceso[0]] > 0:  # Solo si el proceso no ha terminado
                tiemposEspera[proceso[0]] += ejecutado

        # Si todavía queda ráfaga, volver a encolar
        if rafagasRestantes[procesoActual] > 0:
            procesos.append((procesoActual, rafagasRestantes[procesoActual]))
        else:
            tiemposFinalizacion[procesoActual] = tiempoActual

    # Calcular promedios
    promedioEspera = sum(tiemposEspera.values()) / len(tiemposEspera)
    promedioFinalizacion = sum(tiemposFinalizacion.values()) / len(tiemposFinalizacion)

    # Imprimir resultados
    print("\nProceso\t\tRáfaga\tCiclos\tTiempo de Espera\tTiempo de Finalización")
    for proceso, rafaga in rafagas.items():
        print("{}\t\t{}\t{}\t\t{}\t\t\t{}".format(proceso, rafaga, ciclos[proceso], tiemposEspera[proceso], tiemposFinalizacion[proceso]))
    print("\nPromedio de Tiempo de Espera: {:.2f}".format(promedioEspera))
    print("Promedio de Tiempo de Finalización: {:.2f}".format(promedioFinalizacion))


def sjf(rafagas):
    procesosOrdenados = sorted(rafagas.items(), key=lambda item: item[1])
    
    tiempoActual = 0
    tiemposEspera = {}
    tiemposFinalizacion = {}
    
    for i, (proceso, rafaga) in enumerate(procesosOrdenados, start=1):
        tiemposEspera[proceso] = tiempoActual
        tiempoEjecucion = rafaga
        tiempoActual += tiempoEjecucion
        tiemposFinalizacion[proceso] = tiempoActual
    
    print("\nProceso\t\tRáfaga de CPU\tOrden de Ejecución\tTiempo de Espera\tTiempo de Finalización")
    for i, (proceso, rafaga) in enumerate(procesosOrdenados, start=1):
        print("{}\t\t{}\t\t\t{}\t\t\t\t{}\t\t\t\t{}".format(proceso, rafaga, i, tiemposEspera[proceso], tiemposFinalizacion[proceso]))
    
    promedioEspera = sum(tiemposEspera.values()) / len(tiemposEspera)
    promedioFinalizacion = sum(tiemposFinalizacion.values()) / len(tiemposFinalizacion)
    print("\nPromedio de Tiempo de Espera: {:.2f}".format(promedioEspera))
    print("Promedio de Tiempo de Finalización: {:.2f}".format(promedioFinalizacion))

def menuAlgoritmoPlanificacion():
    titulo = 'Bienvenido a este programa de Algoritmos de planificación'
    print(titulo + '\n' + len(titulo) * '-')
    print('\nFCFS: 1\nRR: 2\nSJF: 3\n')
    seleccionAlgoritmo = int(input('Seleccione el Algoritmo de Planeación que desea usar: '))
    
    if seleccionAlgoritmo == 1:
        rafagas, tiemposLlegada = solicitudDeDatos()
        print('Escogió el Algoritmo FCFS')
        fcfs(rafagas, tiemposLlegada)
    elif seleccionAlgoritmo == 2:
        rafagas, _ = solicitudDeDatos()
        print('Escogió el Algoritmo RR')
        quantum = int(input('Ingrese el quantum para el algoritmo RR: '))
        rr(rafagas, quantum)
    elif seleccionAlgoritmo == 3:
        rafagas, _ = solicitudDeDatos()
        print('Escogió el Algoritmo SJF')
        sjf(rafagas)
    else: 
        print('No se ingresó una opción válida!!!')

menuAlgoritmoPlanificacion()
