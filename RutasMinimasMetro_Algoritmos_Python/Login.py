import tkinter
from tkinter.constants import BOTTOM, COMMAND 
import tkinter.ttk
import Interactiva

ventana = tkinter.Tk()
ventana.title("Inicio de Sesión")
ventana.geometry("360x300")
ventana.resizable(width=False, height=False)

logUsuario = tkinter.Label(ventana, text="Ingrese su usuario: ")
logUsuario.pack()

usuario = tkinter.StringVar()
usuario_Entry = tkinter.Entry(ventana, width=30, textvariable=usuario)
usuario_Entry.pack()

logContra = tkinter.Label(ventana, text= "Ingrese su contraseña: ")
logContra.pack()

contra = tkinter.StringVar()
logContra_entry = tkinter.Entry(ventana,width=30, show="*", textvariable=contra)
logContra_entry.pack()

def Ingreso():
    if usuario.get()=="asd1" and contra.get()=="algo1":
        ventana.destroy()
        Interactiva.VentanaInteractiva()

    else:
        ventana.title("Incorrecto. Intente Nuevamente")

botonAcceso = tkinter.Button(ventana, text="Ingresar", command=Ingreso)
botonAcceso.pack(side=BOTTOM)

ventana.mainloop()