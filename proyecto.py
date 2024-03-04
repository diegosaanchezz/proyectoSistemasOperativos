def solicitudDeDatos():
    procesos = {  #Diccionario que guarda los diferentes procesos que el usuario puede seleccionar
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
    #Solicita al usuario el numero de procesos que desea ejecutar
    numeroProcesos = int(input('\nIngrese el número de procesos que desea tener: (1-5):\n'))
    numeroProcesos = max(1, min(numeroProcesos, 5))
    rafagas = {}
    tiemposLlegada = {}
    #Bucle for que recopila la información de cada proceso que se selecciono anteriormente
    for i in range(numeroProcesos):
        print('\n')
        print(procesos)
        print('\n')
        escogerProceso = int(input('Ingrese el número de proceso que desea añadir: '))
        while escogerProceso not in procesos:  #Valida el proceso elegido
            print("Número de proceso no válido. Por favor, intente de nuevo.")
            escogerProceso = int(input('Ingrese el número de proceso que desea añadir: '))
        proceso = procesos[escogerProceso]
        print('\nNOTA!!!\nEl tamaño de ráfaga máximo es de 15\n')
        #Solicita el tamaño de rafaga que tendra el proceso
        escogerTamagnoRafaga = int(input('Ingrese el tamaño de ráfaga del proceso {}: '.format(proceso)))
        escogerTamagnoRafaga = max(1, min(escogerTamagnoRafaga, 15))
        rafagas[proceso] = escogerTamagnoRafaga
        tiemposLlegada[proceso] = i #Asigna el tiempo de llegada basado en el orden de entrada
        print('Lista de Procesos:')
        print(rafagas)
    return rafagas, tiemposLlegada

def fcfs(rafagas, tiemposLlegada): #Funcion que simulara el algoritmo FCFS
    tiempoActual = 0
    tiemposEspera = {}
    tiemposFinalizacion = {}
    #Impresion de los resultados 
    print("\nProceso\t\tRáfaga de CPU\tTiempo de Llegada\tTiempo de Espera\tTiempo de Finalización")
    for proceso, rafaga in rafagas.items():
        tiempoLlegada = tiemposLlegada[proceso]
        tiempoEspera = max(0, tiempoActual - tiempoLlegada)
        tiemposEspera[proceso] = tiempoEspera
        tiempoFinalizacion = tiempoActual + rafaga
        tiemposFinalizacion[proceso] = tiempoFinalizacion
        print("{}\t\t{}\t\t\t{}\t\t\t{}\t\t\t{}".format(proceso, rafaga, tiempoLlegada, tiempoEspera, tiempoFinalizacion))
        tiempoActual += rafaga
        #Calcula e imprime los tiempos de espera y finalizacion 
    promedioEspera = sum(tiemposEspera.values()) / len(tiemposEspera)
    promedioFinalizacion = sum(tiemposFinalizacion.values()) / len(tiemposFinalizacion)
    print("\nPromedio de Tiempo de Espera: {:.2f}".format(promedioEspera))
    print("Promedio de Tiempo de Finalización: {:.2f}".format(promedioFinalizacion))

def rr(rafagas, quantum): #Funcion que simulara el algoritmo RR
    from collections import deque #Importa deque para gestionar la cola de los procesos
    procesos = deque(rafagas.items()) #Es la cola de procesos
    tiemposEspera = {proceso: 0 for proceso in rafagas} #Inicializa los tiempos de espera
    tiemposFinalizacion = {}
    tiempoActual = 0
    rafagasRestantes = rafagas.copy() #Copia el diccionario de rafagas 
    #Ejecuta cada proceso dependiendo del quantum
    while procesos:
        procesoActual, rafagaActual = procesos.popleft()
        if rafagaActual <= 0:
            continue
        ejecutado = min(rafagaActual, quantum)
        tiempoActual += ejecutado
        rafagasRestantes[procesoActual] -= ejecutado #Actualiza las rafagas que quedan
        #Actualiza el tiempo de espera de los otros procesos
        for proceso in procesos:
            if rafagasRestantes[proceso[0]] > 0:
                tiemposEspera[proceso[0]] += ejecutado
        if rafagasRestantes[procesoActual] > 0: #Vuelve a ingresar los procesos a la cola si le quedan rafagas
            procesos.append((procesoActual, rafagasRestantes[procesoActual]))
        
        else:
            tiemposFinalizacion[procesoActual] = tiempoActual
            #Calcula e imprime los tiempos promedios de espera y finalizacion 
    promedioEspera = sum(tiemposEspera.values()) / len(tiemposEspera)
    promedioFinalizacion = sum(tiemposFinalizacion.values()) / len(tiemposFinalizacion)
    print("\nProceso\t\tRáfaga\tTiempo de Espera\tTiempo de Finalización")
    for proceso, rafaga in rafagas.items():
        print("{}\t\t{}\t\t{}\t\t\t{}".format(proceso, rafaga, tiemposEspera[proceso], tiemposFinalizacion[proceso]))
    print("\nPromedio de Tiempo de Espera: {:.2f}".format(promedioEspera))
    print("Promedio de Tiempo de Finalización: {:.2f}".format(promedioFinalizacion))

def sjf(rafagas, tiemposLlegada): #Funcion que simula el algoritmo SJF
    tiempoActual = 0 #Inicializa el tiempo actual en 0 
    tiemposEspera = {proceso: 0 for proceso in rafagas} #Diccionario que almacena los tiempos de espera de cada proceso
    tiemposFinalizacion = {} #Diccionario que almacena los tiempos de finalizacion de cada proceso
    procesosListos = {} #Diccionario que almacena los procesos listos para la ejecucion
    procesosEjecutados = [] #Lista que almacena los procesos que ya se han ejecutado
    
   #Bucle while que se encarga de que todos los procesos hayan sido ejecutados 
    while len(procesosEjecutados) < len(rafagas):
        #Añade los procesos al diccionario listos 
        for proceso, tiempoLlegada in tiemposLlegada.items():
            if tiempoLlegada <= tiempoActual and proceso not in procesosEjecutados:
                procesosListos[proceso] = rafagas[proceso]
         #Si no gay listos el tiempo se incrementa 
        if not procesosListos:
            tiempoActual += 1
            continue
          #Selecciona el proceso con la rafaga mas corta para ejecutar
        procesoAEjecutar = min(procesosListos, key=procesosListos.get)
        rafaga = rafagas[procesoAEjecutar]
        #Calcula el tiempo de espera para el proceso actual y actualiza el tiempo actual de finalizacion 
        tiemposEspera[procesoAEjecutar] = tiempoActual - tiemposLlegada[procesoAEjecutar]
        tiempoActual += rafaga
        tiemposFinalizacion[procesoAEjecutar] = tiempoActual
        #Añade el proceso a la lista de procesos ejecutados y lo elimina de procesos listos 
        procesosEjecutados.append(procesoAEjecutar)
        del procesosListos[procesoAEjecutar]
     #Calcula y muestra al usuario los tiempos promedios de espera y finalizacion 
    promedioEspera = sum(tiemposEspera.values()) / len(tiemposEspera)
    promedioFinalizacion = sum(tiemposFinalizacion.values()) / len(tiemposFinalizacion)
    
    print("\nProceso\t\tRáfaga de CPU\tTiempo de Llegada\tTiempo de Espera\tTiempo de Finalización")
    for proceso in rafagas:
        print("{}\t\t{}\t\t\t{}\t\t\t\t{}\t\t\t\t{}".format(proceso, rafagas[proceso], tiemposLlegada[proceso], tiemposEspera[proceso], tiemposFinalizacion[proceso]))
    print("\nPromedio de Tiempo de Espera: {:.2f}".format(promedioEspera))
    print("Promedio de Tiempo de Finalización: {:.2f}".format(promedioFinalizacion))

def menuAlgoritmoPlanificacion(): #funcion que muestra el menu principal , permite seleccionar un algoritmo 
    titulo = 'Bienvenido a este programa de Algoritmos de planificación'
    print(titulo + '\n' + len(titulo) * '-')
    print('\nFCFS: 1\nRR: 2\nSJF: 3\n')
    seleccionAlgoritmo = int(input('Seleccione el Algoritmo de Planeación que desea usar: '))
    if seleccionAlgoritmo == 1: #ejecuta la funcion correspondiente al algoritmo seleccionado anteriormente 
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

menuAlgoritmoPlanificacion()# LLama al menu principal para comenzar a ejecutar el programa
