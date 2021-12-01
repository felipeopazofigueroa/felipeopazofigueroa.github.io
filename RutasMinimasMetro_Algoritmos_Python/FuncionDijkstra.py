from collections import defaultdict
from tkinter import font, ttk
from tkinter import *
import tkinter
from numpy import void
import pandas as pd
import Interactiva

l1 = pd.read_excel("MatrizDistancias.xlsx")

la = l1.columns.size - 1

asd1 = l1.columns.array
Distancias_menores = []

xx = []

for j in asd1:
    xx.append(j)

grafo = []
for k in xx:
    t1 = l1[k]
    t2 = []
    for j in t1:
        t2.append(j)
    grafo.append(t2)

xx.remove("Unnamed: 0")

opciones = []
for i in range(0,len(xx)):
    opciones.append(xx[i])
    
class Grafo:
    def minDistancia(self,dist,cola):
        min = float("Inf")
        minIndice = -1
        
        for i in range(len(dist)):
            if dist[i] < min and i in cola:
                min = dist[i]
                minIndice = i
        return minIndice

    def getIndice(self,arregloEst,estacion):
        for i in range(0,len(arregloEst)):
            if(estacion == arregloEst[i]):
                valor = arregloEst.index(arregloEst[i]) 
        return valor


    def getRecorrido(self, padre, j):
        if padre[j] == -1 :
            Label_Camino.insert(END,selecInicio.get())
            return

        self.getRecorrido(padre , padre[j])
        for i in range(0,len(arregloEst)):
            if(arregloEst.index(arregloEst[i]) == j):
                Label_Camino.insert(END,u"\u2193",arregloEst[i])


    def getDatos(self, dist, padre):
        for i in range(0, len(dist)):
            for x in range(0,len(arregloEst)):
                if((arregloEst.index(arregloEst[x]) == i) and (v == i)):
                    global distancia
                    distancia = IntVar()
                    distancia.set(dist[i])
                    self.getRecorrido(padre,i)
                    Label_Distancia.config(text="Distancia Minima: "+str(distancia.get())+" metros")
                    break
                else:
                    continue

    def Dijkstra(self, grafo, src):
        fila = len(grafo)
        col = len(grafo[0])

        dist = [float("Inf")] * fila

        padre = [-1] * fila

        dist[src] = 0
    
        cola = []
        for i in range(fila):
            cola.append(i)

            
        while cola:
            u = self.minDistancia(dist,cola)
            cola.remove(u)

            for i in range(col):
                if grafo[u][i] and i in cola:
                    if dist[u] + grafo[u][i] < dist[i]:
                        dist[i] = dist[u] + grafo[u][i]
                        padre[i] = u

        self.getDatos(dist,padre)

                
    def CalcularDijkstra(): 
        g = Grafo()
        for i in range (0,len(xx)):
            if(xx[i] == selecDestino.get()):
                for j in range(0,len(grafo)):
                    if(grafo[0][j] == selecInicio.get()):
                        global arregloEst
                        arregloEst = grafo[0]
                        global v
                        v = g.getIndice(arregloEst,selecDestino.get())
                        grafo.pop(0)
                        g.Dijkstra(grafo,j)
                        break

                    else:
                        continue

    def CalcularTraslado():
        g = Grafo()
        for j in range(0,len(grafo)):
            if(grafo[0][j] == selecInicio.get()):
                global arregloEst
                arregloEst = grafo[0]
                global v
                v = g.getIndice(arregloEst,selecInicio.get())
                grafo.pop(0)
                g.DijkstraTraslados(grafo,j)
                break

            else:
                continue

def VentanaPrincipal():
    ventana = tkinter.Tk()
    ventana.title("Rutas Minimas Metro de Santiago")
    ventana.geometry("1024x720")
    eti = tkinter.Label(ventana, text = "Nombre: Felipe Opazo Figueroa\nCurso: Algoritmos / Universidad Finis Terrae\n'Sistema de Rutas Mínimas Metro de Santiago de Chile'", bg = "CadetBlue", fg="white",font = "fixed")
    eti.pack(fill = tkinter.X)

    def cerrarEjecutar():
        ventana.destroy()
        Interactiva.VentanaInteractiva()

    global selecInicio
    selecInicio = StringVar()
    selecInicio.set(opciones[0])

    global selecDestino
    selecDestino = StringVar()
    selecDestino.set(opciones[0])

    boton_Volver = tkinter.Button(text="Volver <-",command=cerrarEjecutar)
    boton_Volver.pack(anchor=NW)

    eti2 = tkinter.Label(ventana, text = "Seleccione el local de inicio", bg = "white", font = "fixed")
    eti2.pack(anchor=CENTER)

    menu = OptionMenu(ventana, selecInicio, *opciones)
    menu.pack(pady=20)

    eti3 = tkinter.Label(ventana, text = "Seleccione el local de destino", bg="white", font="fixed")
    eti3.pack(anchor=CENTER)

    menu2 = OptionMenu(ventana, selecDestino, *opciones)
    menu2.pack(pady=20)
    
    boton = ttk.Button(text = "Calcular",command= Grafo.CalcularDijkstra)
    boton.pack(anchor=CENTER)
    
    global Label_Distancia
    Label_Distancia = tkinter.Label(ventana, text="Distancia Minima: ", bg="white", font="fixed")
    Label_Distancia.pack(fill = tkinter.X)

    Label_Recorrido = tkinter.Label(ventana, text="Locales Intermediarios:\n",bg="white",font="fixed")
    Label_Recorrido.pack(fill = tkinter.X)

    barraScroll = Scrollbar(ventana)
    barraScroll.pack(side="right",fill="y")

    global Label_Camino
    Label_Camino = tkinter.Listbox(ventana, bg = "CadetBlue", fg="white", font="fixed",borderwidth=2,relief="solid",yscrollcommand=Scrollbar.set)
    Label_Camino.pack()

    barraScroll.config(command=Label_Camino.yview)
    

    ventana.mainloop()


