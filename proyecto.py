def solicitudDeDatos():
    procesos = {
        1: 'Safari',
        2: 'Apple Music',
        3: 'Visual Studio Code',
        4: 'Discord',
        5: 'Word',
        6: 'Excel',
        7: 'Zoom',
        8: 'VirtualBox',
        9: 'PowerPoint',
        10: 'Notion'
    }
    numeroProcesos = int(input('\nIngrese el número de procesos que desea tener: (1-5):\n'))
    
    numeroProcesos = max(1, min(numeroProcesos, 5))
    
    rafagas = {}
    for _ in range(numeroProcesos):
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
        print('Lista de Procesos:')
        print(rafagas)
    return rafagas

def fcfs(rafagas):
    tiempoEspera = 0
    tiempoTotal = 0
    sumaTiemposEspera = 0
    sumaTiemposFinalizacion = 0
    
    print("\nProceso\t\tRáfaga de CPU\tTiempo de Llegada\tTiempo de Espera\tTiempo de Finalización")
    
    for proceso, rafaga in rafagas.items():
        tiempoTotal = tiempoEspera + rafaga
        print("{}\t\t{}\t\t\t{}\t\t\t{}\t\t\t{}".format(proceso, rafaga, 0, tiempoEspera, tiempoTotal))
        sumaTiemposEspera += tiempoEspera
        sumaTiemposFinalizacion += tiempoTotal
        tiempoEspera += rafaga
    
    promedioEspera = sumaTiemposEspera / len(rafagas)
    promedioFinalizacion = sumaTiemposFinalizacion / len(rafagas)
    print("\nPromedio de Tiempo de Espera: {:.2f}".format(promedioEspera))
    print("Promedio de Tiempo de Finalización: {:.2f}".format(promedioFinalizacion))

def rr(rafagas, quantum):
    from collections import deque

    procesos = deque(sorted(rafagas.items(), key=lambda item: item[0]))
    tiemposEspera = {proceso: 0 for proceso in rafagas}
    tiemposFinalizacion = {}
    ciclos = {proceso: 0 for proceso in rafagas}

    tiempoActual = 0
    while procesos:
        procesoActual, rafagaActual = procesos.popleft()
        ciclos[procesoActual] += 1

        ejecucion = min(rafagaActual, quantum)
        tiempoActual += ejecucion
        rafagaActual -= ejecucion

        for proceso in procesos:
            tiemposEspera[proceso[0]] += ejecucion

        if rafagaActual > 0:
            procesos.append((procesoActual, rafagaActual))
        else:
            tiemposFinalizacion[procesoActual] = tiempoActual

    promedioEspera = sum(tiemposEspera.values()) / len(tiemposEspera)
    promedioFinalizacion = sum(tiemposFinalizacion.values()) / len(tiemposFinalizacion)

    print("\nProceso\t\tRáfaga\tCiclos\tTiempo de Espera\tTiempo de Finalización")
    for proceso in rafagas:
        print("{}\t\t{}\t{}\t\t{}\t\t\t{}".format(proceso, rafagas[proceso], ciclos[proceso], tiemposEspera[proceso], tiemposFinalizacion[proceso]))
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
    
    rafagas = solicitudDeDatos()
    
    if seleccionAlgoritmo == 1:
        print('Escogió el Algoritmo FCFS')
        fcfs(rafagas)
    elif seleccionAlgoritmo == 2:
        print('Escogió el Algoritmo RR')
        quantum = int(input('Ingrese el quantum para el algoritmo RR: '))
        rr(rafagas, quantum)
    elif seleccionAlgoritmo == 3:
        print('Escogió el Algoritmo SJF')
        sjf(rafagas)
    else: 
        print('No se ingresó una opción válida!!!')

menuAlgoritmoPlanificacion()