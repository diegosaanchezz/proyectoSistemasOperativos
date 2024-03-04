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
    procesos = deque(rafagas.items())
    tiemposEspera = {proceso: 0 for proceso in rafagas}
    tiemposFinalizacion = {}
    tiempoActual = 0
    rafagasRestantes = rafagas.copy()
    while procesos:
        procesoActual, rafagaActual = procesos.popleft()
        if rafagaActual <= 0:
            continue
        ejecutado = min(rafagaActual, quantum)
        tiempoActual += ejecutado
        rafagasRestantes[procesoActual] -= ejecutado
        for proceso in procesos:
            if rafagasRestantes[proceso[0]] > 0:
                tiemposEspera[proceso[0]] += ejecutado
        if rafagasRestantes[procesoActual] > 0:
            procesos.append((procesoActual, rafagasRestantes[procesoActual]))
        else:
            tiemposFinalizacion[procesoActual] = tiempoActual
    promedioEspera = sum(tiemposEspera.values()) / len(tiemposEspera)
    promedioFinalizacion = sum(tiemposFinalizacion.values()) / len(tiemposFinalizacion)
    print("\nProceso\t\tRáfaga\tTiempo de Espera\tTiempo de Finalización")
    for proceso, rafaga in rafagas.items():
        print("{}\t\t{}\t\t{}\t\t\t{}".format(proceso, rafaga, tiemposEspera[proceso], tiemposFinalizacion[proceso]))
    print("\nPromedio de Tiempo de Espera: {:.2f}".format(promedioEspera))
    print("Promedio de Tiempo de Finalización: {:.2f}".format(promedioFinalizacion))

def sjf(rafagas, tiemposLlegada):
    tiempoActual = 0
    tiemposEspera = {proceso: 0 for proceso in rafagas}
    tiemposFinalizacion = {}
    procesosListos = {}
    procesosEjecutados = []
    

    while len(procesosEjecutados) < len(rafagas):
        for proceso, tiempoLlegada in tiemposLlegada.items():
            if tiempoLlegada <= tiempoActual and proceso not in procesosEjecutados:
                procesosListos[proceso] = rafagas[proceso]
        
        if not procesosListos:
            tiempoActual += 1
            continue
        
        procesoAEjecutar = min(procesosListos, key=procesosListos.get)
        rafaga = rafagas[procesoAEjecutar]
        
        tiemposEspera[procesoAEjecutar] = tiempoActual - tiemposLlegada[procesoAEjecutar]
        tiempoActual += rafaga
        tiemposFinalizacion[procesoAEjecutar] = tiempoActual
        
        procesosEjecutados.append(procesoAEjecutar)
        del procesosListos[procesoAEjecutar]
    
    promedioEspera = sum(tiemposEspera.values()) / len(tiemposEspera)
    promedioFinalizacion = sum(tiemposFinalizacion.values()) / len(tiemposFinalizacion)
    
    print("\nProceso\t\tRáfaga de CPU\tTiempo de Llegada\tTiempo de Espera\tTiempo de Finalización")
    for proceso in rafagas:
        print("{}\t\t{}\t\t\t{}\t\t\t\t{}\t\t\t\t{}".format(proceso, rafagas[proceso], tiemposLlegada[proceso], tiemposEspera[proceso], tiemposFinalizacion[proceso]))
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
        rafagas, tiemposLlegada = solicitudDeDatos() 
        print('Escogió el Algoritmo RR')
        quantum = int(input('Ingrese el quantum para el algoritmo RR: '))
        rr(rafagas, quantum)
    elif seleccionAlgoritmo == 3:
        rafagas, tiemposLlegada = solicitudDeDatos()
        print('Escogió el Algoritmo SJF')
        sjf(rafagas, tiemposLlegada)
    else: 
        print('No se ingresó una opción válida!!!')

menuAlgoritmoPlanificacion()

