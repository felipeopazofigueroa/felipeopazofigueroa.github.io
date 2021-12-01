#PROGRAMA DISEÑADO PARA EL CONTROL EFICIENTE DE LAS SALAS DE CLASES / PROGRAMACIÓN PROYECTO SEMESTRAL
#NOTA: Si los datos a ingresar (por el usuario) en algún momento del programa son incorrectos, el ciclo While repetirá el proceso hasta que sean ingresados correctamente.

#Listas a utilizr en el algoritmo
Lunes = []
Martes = []
Miercoles = []
Jueves = []
Viernes = []
Sabado = []
todasLasSalas = []
todasLasCapacidades = []
listaObt = []

cont = 0
archivo = open("BaseDeDatosSalas.txt","r")
todasLasLineas = archivo.readlines()
archivo.close()
for i in range(0,len(todasLasLineas)):
    x = todasLasLineas[i].split(";")
    todasLasSalas.append(x[0])
    todasLasCapacidades.append(x[1])

Ciclo = 1
while(Ciclo>0):
    if (Ciclo == 1):
        print("\nSISTEMA PARA EL CONTROL DE SALAS DE CLASE\n================================================================\n1. Registrar Sala de Clase\n2. Borrar Sala de Clase\n3. Editar capacidad de la sala\n4. Asignar sala\n5. Liberar sala\n6. Consultar disponibilidad de salas por capacidad y horario\n7. Mostrar salas utilizadas por horario\n8. Salir del sistema")
        Control = True
        while(Control):
            try:
                print("================================================================")
                Num = int(input("\nIngrese la opción correspondiente a la función que desea solicitar: "))
                if (Num>=1 and Num<=8):
                    Control = False
                else:
                    print("---------------------------------------------------------------------")
                    print("Opción ingresada no estuvo en el rango definido. Intente nuevamente.")
                    print("---------------------------------------------------------------------")
                    
            except:
                print("-------------------------------------------")
                print("ERROR. No se ingresó una opción numérica.")
                print("-------------------------------------------")
                    

        if (Num == 1): 
            cont = 0
            archivo = open("BaseDeDatosSalas.txt","r")
            todasLasLineas = archivo.readlines()
            archivo.close()
            
            print("======================================================")
            reqSala = input("Ingrese la sala que desea agregar al sistema: ")
            print("======================================================")
            
            cicloCap = True
            while(cicloCap):
                try:
                    reqCap = int(input("Ingrese la capacidad de la sala que agregará: "))
                    print("======================================================")
                    cicloCap = False
                    

                except:
                        print("\n")
                        print("======================================================")
                        print("Ingrese la capacidad de la sala con un valor numérico.")
                        print("======================================================")
                    
            for i in range(0,len(todasLasSalas)):
                if(reqSala != todasLasSalas[i]):
                    cont += 1
            if(cont == len(todasLasSalas)):
               todasLasSalas.append(reqSala)
               todasLasCapacidades.append(int(reqCap))
               archivo = open("BaseDeDatosSalas.txt","r")
               VarDeAddBloc = archivo.readlines()
               VarDeAddBloc.append("\n"+reqSala+";"+str(reqCap))
               archivo.close()
               archivo = open("BaseDeDatosSalas.txt","w+")
               archivo.writelines(VarDeAddBloc)
               archivo.close()
               print("\n")
               print("======================================================")
               print("La sala ha sido ingresada exitosamente en el sistema.")
               print("======================================================")
                
            else:
               print("\n")
               print("==================================================================")
               print("ERROR. La sala ya se encuentra en el sistema. Intente nuevamente.")
               print("==================================================================")
               
               
                          
                    
        elif(Num == 2): 
            cicloBorrar = True
            while(cicloBorrar):
                borrarIdent = input("\nIngrese identificador que desea borrar del sistema: ")
                try:
                    for i in range(0,len(todasLasSalas)):
                        if(borrarIdent in todasLasSalas[i]):
                            todasLasSalas.remove(todasLasSalas[i])
                            todasLasCapacidades.remove(todasLasCapacidades[i])
                            print("\n")
                            print("================================")
                            print("Se eliminó dicha sala con éxito.")
                            print("================================")
                            archivo = open("BaseDeDatosSalas.txt","r")
                            todasLasLineas = archivo.readlines()
                            archivo.close()
                        for i in range(0,len(todasLasLineas)):
                            if (borrarIdent in todasLasLineas[i]):
                                todasLasLineas.pop(i)
                            archivo = open("BaseDeDatosSalas.txt","w+")
                            archivo.writelines(todasLasLineas)
                            archivo.close()
                            cicloBorrar = False

                except:
                    print(" ")
                    
        elif(Num == 3): 
            cicloEditar = True
            while(cicloEditar):
                editarCap = input("\nIngrese el identificador de la sala que desea editarle su respectiva capacidad: ")
                cicloNum = True
                while(cicloNum):
                    try:
                        numCap = int(input("\nIngrese la nueva capacidad de la sala: "))
                        cicloNum = False
                    except:
                        print("\nNo ingresó un valor numérico. Intente nuevamente.")
                lastCiclo = True
                while(lastCiclo):
                    try:
                        for i in range(0,len(todasLasCapacidades)):
                            if(editarCap in todasLasSalas[i]):
                                todasLasCapacidades[i] = numCap
                                print("\n")
                                print("=====================================================")
                                print("Se ha editado la capacidad de la sala correctamente.")
                                print("=====================================================")
                                cicloEditar = False
                                lastCiclo = False
                    except:
                        print("\n")

        elif(Num == 4):
            cicloIdent = True
            while(cicloIdent):
                print("===============================================================================")
                Ident = input("Ingrese el identificador de la sala que desea asignar: ")
                print("===============================================================================")
                Hor = input("Ingrese el día(ej: Lunes, Martes, etc): ")
                print("===============================================================================")
                ciclodelModulo = True
                while(ciclodelModulo):
                    try:
                        Modul = int(input("Ingrese el módulo que necesitará: "))
                        VarUtiliza = Modul
                        ciclodelModulo = False
                    except:
                        print("================================================")
                        print("Debe ingresar un valor numérico para el módulo.")
                        print("================================================")
                        
                for i in range(0,len(todasLasSalas)):
                    if(Ident in todasLasSalas[i]):
                            if(Hor == "Lunes" or Hor == "lunes" or Hor == "LUNES"):
                                VarMod1 = ("["+todasLasSalas[i]+","+str(Modul)+","+todasLasCapacidades[i]+"]")
                                if(VarMod1 in Lunes):
                                    print("==================================================================")
                                    print("El módulo está ocupado. Intente con otro horario para dicha sala.")
                                    print("==================================================================")
                                    
                                else:
                                    Lunes.append("["+todasLasSalas[i]+","+str(Modul)+","+todasLasCapacidades[i]+"]")
                                    print("\n")
                                    print("=============================")
                                    print("Sala asignada correctamente.")
                                    print("=============================")
                                    cicloIdent = False
                            elif(Hor == "Martes" or Hor == "martes" or Hor == "MARTES"):
                                VarMod2 = ("["+todasLasSalas[i]+","+str(Modul)+","+todasLasCapacidades[i]+"]")
                                if(VarMod2 in Martes):
                                    print("==================================================================")
                                    print("El módulo está ocupado. Intente con otro horario para dicha sala.")
                                    print("==================================================================")
                                else:
                                    Martes.append("["+todasLasSalas[i]+","+str(Modul)+","+todasLasCapacidades[i]+"]")
                                    print("\n")
                                    print("=============================")
                                    print("Sala asignada correctamente.")
                                    print("=============================")
                                    cicloIdent = False
                            elif(Hor == "Miercoles" or Hor == " miercoles" or Hor == "MIERCOLES"):
                                VarMod3 = ("["+todasLasSalas[i]+","+str(Modul)+","+todasLasCapacidades[i]+"]")
                                if(VarMod3 in Miercoles):
                                    print("==================================================================")
                                    print("El módulo está ocupado. Intente con otro horario para dicha sala.")
                                    print("==================================================================")
                                else:
                                    Miercoles.append("["+todasLasSalas[i]+","+str(Modul)+","+todasLasCapacidades[i]+"]")
                                    print("\n")
                                    print("=============================")
                                    print("Sala asignada correctamente.")
                                    print("=============================")
                                    cicloIdent = False
                            elif(Hor == "Jueves" or Hor == "jueves" or Hor == "JUEVES"):
                                VarMod4 = ("["+todasLasSalas[i]+","+str(Modul)+","+todasLasCapacidades[i]+"]")
                                if(VarMod4 in Jueves):
                                    print("==================================================================")
                                    print("El módulo está ocupado. Intente con otro horario para dicha sala.")
                                    print("==================================================================")
                                else:
                                    Jueves.append("["+todasLasSalas[i]+","+str(Modul)+","+todasLasCapacidades[i]+"]")
                                    print("\n")
                                    print("=============================")
                                    print("Sala asignada correctamente.")
                                    print("=============================")
                                    cicloIdent = False
                            elif(Hor == "Viernes" or Hor == "viernes" or Hor == "VIERNES"):
                                VarMod5 = ("["+todasLasSalas[i]+","+str(Modul)+","+todasLasCapacidades[i]+"]")
                                if(VarMod5 in Viernes):
                                    print("==================================================================")
                                    print("El módulo está ocupado. Intente con otro horario para dicha sala.")
                                    print("==================================================================")
                                else:
                                    Viernes.append("["+todasLasSalas[i]+","+str(Modul)+","+todasLasCapacidades[i]+"]")
                                    print("\n")
                                    print("=============================")
                                    print("Sala asignada correctamente.")
                                    print("=============================")
                                    cicloIdent = False
                            elif(Hor == "Sabado" or Hor == "sabado" or Hor == "SABADO"):
                                VarMod6 = ("["+todasLasSalas[i]+","+str(Modul)+","+todasLasCapacidades[i]+"]")
                                if(VarMod6 in Sabado):
                                    print("==================================================================")
                                    print("El módulo está ocupado. Intente con otro horario para dicha sala.")
                                    print("==================================================================")
                                else:
                                    Sabado.append("["+todasLasSalas[i]+","+str(Modul)+","+todasLasCapacidades[i]+"]")
                                    print("\n")
                                    print("=============================")
                                    print("Sala asignada correctamente.")
                                    print("=============================")
                                    cicloIdent = False

        elif (Num == 5):
            cicloLiberar = True
            while(cicloLiberar):
                print("===============================================================")
                Ident1 = input("Ingrese el identificador de la sala que desea liberar: ")
                print("===============================================================")
                Hor1 = input("Ingrese el día(ej: Lunes, Martes, etc): ")
                print("===============================================================")
                ciclodelModulo1 = True
                while(ciclodelModulo1):
                    try:
                        ModulUno = int(input("Ingrese el módulo que liberará: "))
                        ciclodelModulo1 = False
                    except:
                        print("================================================")
                        print("Debe ingresar un valor numérico para el módulo.")
                        print("================================================")
                        
                for i in range(0,len(todasLasSalas)):
                    if(Ident1 in todasLasSalas[i]):
                            if(Hor1 == "Lunes" or Hor1 == "lunes" or Hor1 == "LUNES"):
                                VarLib1 = ("["+todasLasSalas[i]+","+str(ModulUno)+","+todasLasCapacidades[i]+"]")
                                if(VarLib1 in Lunes):
                                    Lunes.remove(VarLib1)
                                    print("\n")
                                    print("========================================")
                                    print("La sala ha sido liberada correctamente.")
                                    print("========================================")
                                    cicloLiberar = False
                                else:
                                    print("Sala no existe en el sistema. Intente nuevamente.")
                            if(Hor1 == "Martes" or Hor1 == "martes" or Hor1 == "MARTES"):
                                VarLib2 = ("["+todasLasSalas[i]+","+str(ModulUno)+","+todasLasCapacidades[i]+"]")
                                if(VarLib2 in Martes):
                                    Martes.remove(VarLib2)
                                    print("\n")
                                    print("========================================")
                                    print("La sala ha sido liberada correctamente.")
                                    print("========================================")
                                    cicloLiberar = False
                                else:
                                    print("Sala no existe en el sistema. Intente nuevamente.")
            
                            if(Hor1 == "Miercoles" or Hor1 == "miercoles" or Hor1 == "MIERCOLES"):
                                VarLib3 = ("["+todasLasSalas[i]+","+str(ModulUno)+","+todasLasCapacidades[i]+"]")
                                if(VarLib3 in Miercoles):
                                    Miercoles.remove(VarLib3)
                                    print("\n")
                                    print("========================================")
                                    print("La sala ha sido liberada correctamente.")
                                    print("========================================")
                                    cicloLiberar = False
                                else:
                                    print("Sala no existe en el sistema. Intente nuevamente.")   
                            if(Hor1 == "Jueves" or Hor1 == "jueves" or Hor1 == "JUEVES"):
                                VarLib4 = ("["+todasLasSalas[i]+","+str(ModulUno)+","+todasLasCapacidades[i]+"]")
                                if(VarLib4 in Jueves):
                                    Jueves.remove(VarLib4)
                                    print("\n")
                                    print("========================================")
                                    print("La sala ha sido liberada correctamente.")
                                    print("========================================")
                                    cicloLiberar = False
                                else:
                                    print("Sala no existe en el sistema. Intente nuevamente.")   

                            if(Hor1 == "Viernes" or Hor1 == "viernes" or Hor1 == "VIERNES"):
                                VarLib5 = ("["+todasLasSalas[i]+","+str(ModulUno)+","+todasLasCapacidades[i]+"]")
                                if(VarLib5 in Viernes):
                                    Lunes.remove(VarLib5)
                                    print("\n")
                                    print("========================================")
                                    print("La sala ha sido liberada correctamente.")
                                    print("========================================")
                                    cicloLiberar = False
                                else:
                                    print("Sala no existe en el sistema. Intente nuevamente.")

                            if(Hor1 == "Sabado" or Hor1 == "sabado" or Hor1 == "SABADO"):
                                VarLib6 = ("["+todasLasSalas[i]+","+str(ModulUno)+","+todasLasCapacidades[i]+"]")
                                if(VarLib6 in Sabado):
                                    Lunes.remove(VarLib6)
                                    print("\n")
                                    print("========================================")
                                    print("La sala ha sido liberada correctamente.")
                                    print("========================================")
                                    cicloLiberar = False
                                else:
                                    print("\n")
                                    print("==================================================")
                                    print("Sala no existe en el sistema. Intente nuevamente.")
                                    print("==================================================")
        elif (Num == 6):
            cicloConsultar = True
            while(cicloConsultar):
                print("===============================================================")
                Medum1 = input("Ingrese una capacidad de sala: ")
                print("===============================================================")
                Medum2 = input("Ingrese el día(ej: Lunes, Martes, etc): ")
                print("===============================================================")
                cicloMedum = True
                while(cicloMedum):
                    try:
                        Medum3 = int(input("Ingrese el módulo: "))
                        cicloMedum = False
                        cicloConsultar = False
                    except:
                        print("================================================")
                        print("Debe ingresar un valor numérico para el módulo.")
                        print("================================================")

                if (Medum2 == "Lunes" or Medum2 == "lunes" or Medum2 == "LUNES"):
                    ListaXLunes = []
                    ListaXLunesCap = []
                    try:
                        for i in range(0,len(Lunes)):
                            temporal1 = Lunes[i]
                            VardeTemporal = temporal1[1]+temporal1[2]+temporal1[3]+temporal1[4]
                            for j in range(0,len(todasLasSalas)):
                                temporal2 = todasLasSalas[j]
                                if(VardeTemporal not in todasLasSalas[j]):
                                    ListaXLunes.append(todasLasSalas[j])
                                    
                                    
                                
                        for i in range(0,len(todasLasCapacidades)):
                            if(str(todasLasCapacidades[i])>=Medum1):
                                print("====================================================")
                                print("SALAS DISPONIBLES DIA LUNES\n","SALA: ",ListaXLunes[i]," CAPACIDAD: ",todasLasCapacidades[i])
                                print("====================================================")
                    except:
                        print("\n")
                        
                elif (Medum2 == "Martes" or Medum2 == "martes" or Medum2 == "MARTES"):
                    try:
                        for i in range(0,len(Martes)):
                            if(Martes[i] in todasLasSalas[i]):
                                todasLasSalas.remove(todasLasSalas[i])
                        for i in range(0,len(todasLasCapacidades)):
                            if(str(todasLasCapacidades[i])>=Medum1):
                                print("====================================================")
                                print("SALAS DISPONIBLES DIA MARTES\n","SALA: ",todasLasSalas[i]," CAPACIDAD: ",todasLasCapacidades[i])
                                print("====================================================")
                        todasLasSalas.append(Martes[i])
                    except:
                        print("\n")

                elif (Medum2 == "Miercoles" or Medum2 == "miercoles" or Medum2 == "MIERCOLES"):
                    try:
                        for i in range(0,len(Miercoles)):
                            if(Miercoles[i] in todasLasSalas[i]):
                                todasLasSalas.remove(todasLasSalas[i])
                        for i in range(0,len(todasLasCapacidades)):
                            if(str(todasLasCapacidades[i])>=Medum1):
                                print("====================================================")
                                print("SALAS DISPONIBLES DIA MIERCOLES\n","SALA: ",todasLasSalas[i]," CAPACIDAD: ",todasLasCapacidades[i])
                                print("====================================================")
                        todasLasSalas.append(Miercoles[i])
                    except:
                        print("\n")

                elif (Medum2 == "Jueves" or Medum2 == "jueves" or Medum2 == "JUEVES"):
                    try:
                        for i in range(0,len(Jueves)):
                            if(Jueves[i] in todasLasSalas[i]):
                                todasLasSalas.remove(todasLasSalas[i])
                        for i in range(0,len(todasLasCapacidades)):
                            if(str(todasLasCapacidades[i])>=Medum1):
                                print("====================================================")
                                print("SALAS DISPONIBLES DIA JUEVES\n","SALA: ",todasLasSalas[i]," CAPACIDAD: ",todasLasCapacidades[i])
                                print("====================================================")
                        todasLasSalas.append(Jueves[i])
                    except:
                        print("\n")

                elif (Medum2 == "Viernes" or Medum2 == "viernes" or Medum2 == "VIERNES"):
                    try:
                        for i in range(0,len(Viernes)):
                            if(Viernes[i] in todasLasSalas[i]):
                                todasLasSalas.remove(todasLasSalas[i])
                        for i in range(0,len(todasLasCapacidades)):
                            if(str(todasLasCapacidades[i])>=Medum1):
                                print("====================================================")
                                print("SALAS DISPONIBLES DIA VIERNES\n","SALA: ",todasLasSalas[i]," CAPACIDAD: ",todasLasCapacidades[i])
                                print("====================================================")
                        todasLasSalas.append(Viernes[i])
                    except:
                        print("\n")

                elif (Medum2 == "Sabado" or Medum2 == "sabado" or Medum2 == "SABADO"):
                    try:
                        for i in range(0,len(Sabado)):
                            if(Sabado[i] in todasLasSalas[i]):
                                todasLasSalas.remove(todasLasSalas[i])
                        for i in range(0,len(todasLasCapacidades)):
                            if(str(todasLasCapacidades[i])>=Medum1):
                                print("====================================================")
                                print("SALAS DISPONIBLES DIA SABADO\n","SALA: ",todasLasSalas[i]," CAPACIDAD: ",todasLasCapacidades[i])
                                print("====================================================")
                        todasLasSalas.append(Sabado[i])
                    except:
                        print("\n")
                

        elif (Num == 7):
            for i in range(0,len(Lunes)):
                print("\n    SALAS UTILIZADAS LUNES\n","Identificador/Modulo/Capacidad:"+Lunes[i])
                print("=================================================")
            for i in range(0,len(Martes)):
                print("      SALAS UTILIZADAS MARTES\n","Identificador/Modulo/Capacidad:"+Martes[i])
                print("=================================================")
            for i in range(0,len(Miercoles)):
                print("      SALAS UTILIZADAS MIERCOLES\n","Identificador/Modulo/Capacidad:"+Miercoles[i])
                print("=================================================")
            for i in range(0,len(Jueves)):
                print("      SALAS UTILIZADAS JUEVES\n","Identificador/Modulo/Capacidad:"+Jueves[i])
                print("=================================================")
            for i in range(0,len(Viernes)):
                print("      SALAS UTILIZADAS VIERNES\n","Identificador/Modulo/Capacidad:"+Viernes[i])
                print("=================================================")
            for i in range(0,len(Sabado)):
                print("      SALAS UTILIZADAS SABADO\n","Identificador/Modulo/Capacidad:"+Sabado[i])
                print("=================================================")
                           
                
                    

        elif (Num == 8): 
            print("\n")
            print("===============================================================================")
            print("Gracias por utilizar el sistema de control de salas de la Universidad Finis Terrae.")
            print("===============================================================================")
            break
        


        






























