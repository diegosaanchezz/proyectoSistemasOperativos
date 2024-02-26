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
    numeroProcesos = int(input('\nIngrese el número de procesos que desea tener: (1-5): '))
    pilaAlmacenaProcesos = [] # Pila que almacenara la respuesta de procesos que se desean escoger 
    pilaAlmacenaTamagnoRafaga = [] # Pila que almacenara la respuesta de tamaño de rafaga que escogio el usuario para cada proceso
    i = 0 # Contador
    while i < numeroProcesos:
        print(procesos)
        escogerProceso = int(input('Ingrese el número de proceso que deseas añadir: '))
        print('\nNOTA!!!\nEl tamaño de ráfaga máximo es de 15\n')
        escogertamagnoRafaga = int(input('Ingrese el tamaño de ráfaga del proceso ' + str(pilaAlmacenaProcesos) + ': '))
        
        pilaAlmacenaProcesos.append(procesos[escogerProceso])
        pilaAlmacenaTamagnoRafaga.append(procesos[escogertamagnoRafaga])
        i+=1
        print('Lista de Procesos:')
        print(pilaAlmacenaProcesos)

def menuAlgoritmoPlaneacion():
    titulo = 'Bienvenido a este programa de Algoritmos de planeación'
    print(titulo + '\n' + len(titulo) * '-')
    print('\nFCFS: 1\nRR: 2\nSJF: 3\n')
    seleccionAlgoritmo = int(input('Seleccione el Algoritmo de Planeación que desea usar: '))
    if seleccionAlgoritmo == 1:
        solicitudDeDatos()
        pass # hay que anexar el método de FCFS
    elif seleccionAlgoritmo == 2:
        solicitudDeDatos()
        pass # hay que anexar el método de RR
    elif seleccionAlgoritmo == 3:
        solicitudDeDatos()
        pass # hay que anexar el método de SJF
    else: 
        print('No se ingreso una opción válida!!!')
solicitudDeDatos()

# necesito corregir el método solicitudDeDatos() para que se guarde en las listas tanto el nombre de proceso como el tamaño de rafaga que tiene, debo de fijarme que exista una relación entre estos dos para que no haya una pérdida de datos entre el nombre del proceso y el tamaño de rafaga