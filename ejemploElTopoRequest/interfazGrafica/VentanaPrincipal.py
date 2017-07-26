from tkinter import *
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk
from interfazGrafica.VentanaConfig import VentanaConfig
from interfazGrafica.VentanaCrawler import VentanaCrawler




class VentanaPrincipal():

    def __init__(self):
        self.ventana = Tk()

        self.ventana.geometry('800x600')
        self.ventana.title('Principal')

        #Imagen
      #  gif = PhotoImage(file="/home/usertfm/gitRepository/ejemploElTopoRequest/interfazGrafica/Imagenes/topo.gif")
        jpg = Image.open("/home/usertfm/gitRepository/ejemploElTopoRequest/interfazGrafica/Imagenes/topo11.png")
        fondo = ImageTk.PhotoImage(jpg)
        LBLFondo = Label(self.ventana,image=fondo).place(x=0,y=0)
      #  LBLImagen = Label(self.ventana,image=gif).place(x=200, y=100)
        self.menu = Menu(self.ventana)
        self.ventana.config(menu=self.menu)
        #MENU ARCHIVO
        self.MenuArchivo = Menu(self.menu)
        self.menu.add_cascade(label="Archivo", menu=self.MenuArchivo)
        self.MenuArchivo.add_command(label="Nuevo", command=self.NewFile)
        self.MenuArchivo.add_command(label="Abrir...", command=self.OpenFile)
        self.MenuArchivo.add_separator()
        self.MenuArchivo.add_command(label="Salir", command=self.ventana.quit)
        #MENU CONFIGURACION
        self.MenuConfiguracion = Menu(self.menu)
        self.menu.add_cascade(label="Configuracion", menu=self.MenuConfiguracion)
        self.MenuConfiguracion.add_command(label="Editar",command=self.AbrirVentanaConfiguracion)

        #MENU CRAWLER
        self.MenuConfiguracion = Menu(self.menu)
        self.menu.add_cascade(label="Crawler", menu=self.MenuConfiguracion)
        self.MenuConfiguracion.add_command(label="Abrir",command=self.AbrirVentanaCrawler)


        #MENU AYUDA
        self.MenuAyuda = Menu(self.menu)
        self.menu.add_cascade(label="Ayuda", menu=self.MenuAyuda)
        self.MenuAyuda.add_command(label="Acerca de...", command=self.About)

        self.ventana.mainloop()

    def NewFile(self):
        print("New File!")

    def OpenFile(self):
        name =  askopenfilename()
        print (name)

    def AbrirVentanaConfiguracion(self):
        ventanaConfig = VentanaConfig()
        print ("AQUI HAY QUE ABRIR LA VENTANA DE CONFIGURACION")

    def AbrirVentanaCrawler(self):
        ventanaCrawler = VentanaCrawler()

    def About(self):
        print ("This is a simple example of a menu")
