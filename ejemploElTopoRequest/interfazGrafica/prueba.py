from tkinter import *
from tkinter import ttk
import json




class Prueba():
    def __init__(self):
        self.ventana = Tk()
        self.ventana.geometry('300x200')
        self.ventana.title('Prueba3')
        self.tinfo = Text(self.ventana, width=40, height = 10)
        self.tinfo.pack(side=TOP)
        self.botoninfo = ttk.Button(self.ventana, text = 'Info', command = self.verinfo)
        self.botoninfo.pack(side = LEFT)
        self.botonsalir =ttk.Button(self.ventana, text='Salir',command=self.ventana.destroy)
        self.botonsalir.pack(side=RIGHT)

        #Resaltamos el borde del botoninfo
        self.botoninfo.focus_set()
        self.ventana.mainloop()


    def verinfo(self):
        #Borrar contenido de la caja de texto
        self.tinfo.delete("1.0",END)
        #Obtenemos informacion de la ventana creada

        inf1 = self.ventana.winfo_class()
        inf2 = self.ventana.winfo_geometry()
        inf3 = str(self.ventana.winfo_width())
        inf4 = str(self.ventana.winfo_height())
        inf5 = str(self.ventana.winfo_rootx())
        inf6 = str(self.ventana.winfo_rooty())
        inf7 = str(self.ventana.winfo_id())
        inf8 = self.ventana.winfo_name()
        inf9 = self.ventana.winfo_manager()

        #Contruimos una cadena de texto con toda la info y la insertamos en la cadena de texto creada


        texto_info = "Clase de 'ventana' :" + inf1 + "\n"
        texto_info += "Resolucion y posicion:" + inf2 + "\n"
        texto_info += "Anchura Ventana:" + inf3 + "\n"
        texto_info += "Altura Ventana:" + inf4 + "\n"
        texto_info += "Posicion Ventana X:" + inf5 + "\n"
        texto_info += "Posicion Ventana Y:" + inf6 + "\n"
        texto_info += "Id de la 'ventana' :" + inf7 + "\n"
        texto_info += "Nombre del objeto:" + inf8 + "\n"
        texto_info += "Gestor de ventanas:" + inf9 + "\n"

        self.tinfo.insert("1.0",texto_info)




def main():
    app = Prueba()



if __name__ == '__main__':
    main()
