from tkinter import *
from tkinter import ttk

ventana = Tk()

ventana.geometry('300x200') #ancho por alto
ventana.title("Prueba")
ttk.Button(ventana, text='Salir',command=quit).pack(side=BOTTOM)
ventana.mainloop()
