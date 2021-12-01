import tkinter
from tkinter.constants import CENTER, X
import FuncionDijkstra
from FuncionDijkstra import VentanaPrincipal

def VentanaInteractiva():
    ventana = tkinter.Tk()
    ventana.title("Rutas Minimas Metro de Santiago")
    ventana.geometry("720x480")
    eti = tkinter.Label(ventana, text = "Nombre: Felipe Opazo Figueroa\nCurso: Algoritmos / Universidad Finis Terrae\n'Sistema de Rutas Mínimas Metro de Santiago de Chile'", bg = "CadetBlue", fg="white",font = "fixed")
    eti.pack(fill = tkinter.X)

    eti2 = tkinter.Label(ventana, text="Seleccione la opción de Traslado deseada:")
    eti2.pack(fill = tkinter.X)

    def cerrarEjecutar():
        ventana.destroy()
        FuncionDijkstra.VentanaPrincipal()

    def cerrarEjecutar2():
        ventana.destroy()
        FuncionDijkstra.VentanaSecundaria()

    boton11 = tkinter.Button(text="Traslado 1:1",command=cerrarEjecutar, height=7,width=10)
    boton11.pack(anchor=CENTER)
    
    ventana.mainloop()
