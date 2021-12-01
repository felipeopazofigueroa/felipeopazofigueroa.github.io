#NOTA: El usuario para entrar al programa es MHB y la contraseña hidalgod123.
#NOTA2: Cada vez que termine el ciclo de un punto del programa, se requirá el logeo del usuario y la contraseña para su funcionamiento.
usuario=("MHB", "hidalgod123") #DATOS PARA INGRESAR AL SISTEMA DE LOGIN DEL PROGRAMA ("Usuario, Contraseña") RESPECTIVAMENTE.


#Variables para el punto 3
Disponible = "Disponible"
Arrendado = "Arrendado"
NoDisponible = "No Disponible"
Despreciado = "Despreciado"
Reservado = "Reservado"
listaIngreso = []

print("DELUXE CAR LOGIN")

agregado = []
archivo = open("Laboratorio-10-Flota-de-Vehiculos.txt","r")
for lineas in archivo:
    variable = lineas.split(";")
    agregado.append(variable)

dtiempos = "%Y-%m-%d"
lista1 = []


from datetime import date, timedelta, datetime
now = datetime.now()
cont = 0
while(cont<3):
    U = input("Ingrese usuario: ")
    C = input("Ingrese contraseña: ")
    if (U == usuario[0] and C == usuario[1]):
        print("Acceso confirmado al sistema")
        print("SISTEMA DELUXE CAR\n1. Ingresar vehículos a la flota\n2. Eliminar vehículos de la flota\n3. Mostrar lista de vehículos según su estado\n4. Mostrar información automovil según placa patente\n5. Mostrar vehículos que deben ser renovados\n6. Salir del programa")
        seguir = True
        while (seguir):
            try:
                ingreso = int(input("Ingrese la opción correspondiente desde el 1 al 6: "))
                if (ingreso>=1 and ingreso<=6):
                    seguir = False
            except:
                print("ERROR. Opción invalida.")
        
        if (ingreso == 1):
            archivo = open("Laboratorio-10-Flota-de-Vehiculos.txt","r")
            todasLasLineas = archivo.readlines()
            for i in archivo:
                lista1.append(i.replace("/n","").split(";"))
            archivo.close()
            marca = input("Ingrese marca del vehículo a ingresar: ")
            modelo = input("Ingrese modelo del vehículo a ingresar: ")
            patente = input("Ingrese la placa patente del vehículo a ingresar: ")
            chasis = input("Ingrese número de chasis: ")
            estadoaut = input("Ingrese el estado del auto: ")
            
            cicloKM = True
            while(cicloKM):
                try:
                    km = int(input("Ingrese el kilometraje: "))
                    cicloKM = False
                except ValueError:
                    print("El Kilometraje debe estar marcado en números. Intente nuevamente.")


            cicloFechas = True
            while(cicloFechas):
                try:
                    rev = input("Ingrese fecha de la revisión técnica: ")
                    dtiempos1 = datetime.strptime(rev,dtiempos).date()
                    ultmant = input("Ingrese fecha de mantencion: ")
                    dtiempos2 = datetime.strptime(ultmant,dtiempos).date()
                    proxmant = input("Ingrese fecha de la proxima mantencion: ")
                    dtiempos3 = datetime.strptime(proxmant,dtiempos).date()
                    fechainicioarr = input("Ingrese fecha de inicio del arriendo: ")
                    dtiempos4 = datetime.strptime(fechainicioarr,dtiempos).date()
                    fechafinarr = input("Ingrese fecha del fin del arriendo: ")
                    dtiempos5 = datetime.strptime(fechafinarr,dtiempos).date()
                    if dtiempos4<=dtiempos5:
                        cicloFechas = False
                    else:
                        print("Fecha inicio debe ser anterior a fecha de fin del arriendo. Ingrese los datos nuevamente.")
                except ValueError:
                    print("ValueError: Fecha debe ser ingresada en formato YY-MM-DD")
                    
                    
            datos1 = marca,modelo,patente,chasis,estadoaut,km,rev,ultmant,proxmant,fechainicioarr,fechafinarr
            agregado.append(datos1)
            print("Se ha ingresado el vehículo correctamente al sistema.")

        elif (ingreso == 2):
            cicloEliminar = True
            while(cicloEliminar):
                eliminar = input("Ingrese la placa patente del vehículo que desea eliminar de la flota: ")
                unaVariable = len(agregado)
                try:
                    for i in range (0,len(agregado)):
                        unDato = agregado[i]
                        if ((eliminar in unDato[2])==True):
                            agregado.remove(unDato)
                            print("Se eliminó el vehículo asociado a dicha patente con éxito.")
                            cicloEliminar = False
                
                except:
                     print("\n")
        elif (ingreso == 3):
            FirstConsulta = True
            while(FirstConsulta):
                Consulta = input("Ingrese el estado de vehiculo que desea consultar entre Disponibles/Arrendados/Reservados/Despreciados/No Disponibles: ")
                if (Consulta == "Disponibles" or Consulta == "disponibles"):
                    print("AUTOS DISPONIBLES")
                    print("===============================")
                    for i in range(0,len(agregado)):
                        elemento1 = agregado[i]
                        if (elemento1[4] == Disponible):
                            print(elemento1[0],elemento1[1])
                            print("===============================")
                  
                    FirstConsulta = False
                        
                elif (Consulta == "Arrendados" or Consulta == "arrendados"):
                    print("AUTOS ARRENDADOS")
                    print("===============================")
                    for i in range(0,len(agregado)):
                        elemento1 = agregado[i]
                        if (elemento1[4] == Arrendado):
                            print(elemento1[0],elemento1[1])
                            print("===============================")
                    
                    FirstConsulta = False
                elif (Consulta == "Reservados" or Consulta == "reservados"):
                    print("AUTOS RESERVADOS")
                    print("===============================")
                    for i in range(0,len(agregado)):
                        elemento1 = agregado[i]
                        if (elemento1[4] == Reservado):
                            print(elemento1[0],elemento1[1])
                            print("===============================")
                 
                    FirstConsulta = False
                elif (Consulta == "Despreciados" or Consulta == "despreciados"):
                    print("AUTOS DESPRECIADOS")
                    print("===============================")
                    for i in range(0,len(agregado)):
                        elemento1 = agregado[i]
                        if (elemento1[4] == Despreciado):
                            print(elemento1[0],elemento1[1])
                            print("===============================")
      
                    FirstConsulta = False

                elif (Consulta == "No disponibles" or Consulta == "No Disponibles" or Consulta == "no disponibles"):
                    print("AUTOS NO DISPONIBLES")
                    print("===============================")
                    for i in range(0,len(agregado)):
                        elemento1 = agregado[i]
                        if (elemento1[4] == NoDisponible):
                            print(elemento1[0],elemento1[1])
                            print("===============================")
 
                    FirstConsulta = False
                else:
                    print("No se logró determinar el estado a consultar, intente nuevamente.")
            
        elif (ingreso == 4):
            uncicloWhile = True
            while(uncicloWhile):
                try:
                    InfoVehiculo = input("Ingrese la placa patente del vehículo el cual desea ver sus respectivos datos: ")
                    for i in range(0,len(agregado)):
                        var1 = agregado[i]
                        if(InfoVehiculo == var1[2]):
                            listaIngreso.append(agregado[i])
                    for i in range(0,len(listaIngreso)):
                        var2 = listaIngreso[i]
                    print("\nNombre del vehículo:",var2[0],"\n================","\nModelo:",var2[1],"\n================","\nPatente:",var2[2],"\n================","\nNumero de chasis:",var2[3],"\n================","\nEstado del auto:",var2[4],"\n================","\nKilometraje:",var2[5],"\n================","\nFecha de Última mantención:",var2[6],"\n================","\nFecha de próxima mantención:",var2[7],"\n================","\nFecha de revisión técnica:",var2[8],"\n================","\nFecha de inicio de arriendo:",var2[9],"\n================","\nFecha fin de arriendo:",var2[10])
                    uncicloWhile = False
                except:
                    print("La patente del vehículo a consultar no ha sido encontrada, intente nuevamente.")
        elif (ingreso == 5):
            ciclodeIngreso1 = True
            while(ciclodeIngreso1):
                try:
                    for i in range(0,len(agregado)):
                        onevariable = agregado[i] 
                        fechaR = datetime.datetime.strptime(onevariable[5],"Y-%m-%d").date() + datetime.timedelta(days = 1825)   
                        if(fechaR-datetime.date.today()).days < 1460:
                            print("La lista de vehículos que deben ser renovados es la siguiente:\n",onevariable[0],onevariable[1])
                            print("====================================================")
                            ciclodeIngreso1 = False
                except:
                    print("No se han encontrado vehículos prontos a cumplir su vida útil.")
                    ciclodeIngreso1 = False
              
        elif (ingreso == 6):
            print("Hasta pronto!")
            break
              
            
           
        else:
            print("Debe ingresar la opción correspondiente desde el 1 al 6.")

        

    else:
        print("Los datos ingresados son incorrectos.")
        cont += 1
        if (cont == 3):
            print("Acceso denegado.")









            


            

        
        





    
        
