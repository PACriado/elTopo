from tkinter import *
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk
from interfazGrafica.VentanaConfig import VentanaConfig
from interfazGrafica.VentanaTerminal import VentanaTerminal
from interfazGrafica.VentanaCrawler import VentanaCrawler


class VentanaPrincipal():

    def __init__(self):
        self.ventana = Tk()

        self.ventana.geometry('800x600')
        self.ventana.title('Principal')

        #Imagen
      #  gif = PhotoImage(file="/home/usertfm/gitRepository/ejemploElTopoRequest/interfazGrafica/Imagenes/topo.gif")
        jpg = Image.open("./interfazGrafica/Imagenes/logo3.png")
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

        #MENU TERMINAL
        self.MenuTerminal = Menu(self.menu)
        self.menu.add_cascade(label="Terminal", menu=self.MenuTerminal)
        self.MenuTerminal.add_command(label="Abrir...",command=self.AbrirVentanaTerminal)

        #MENU CRAWLER
        self.MenuCrawler = Menu(self.menu)
        self.menu.add_cascade(label="Crawler",menu=self.MenuCrawler)
        self.MenuCrawler.add_command(label="Abrir...",command=self.AbrirVentanaCrawler)


        #MENU AYUDA
        self.MenuAyuda = Menu(self.menu)
        self.menu.add_cascade(label="Ayuda", menu=self.MenuAyuda)
        self.MenuAyuda.add_command(label="Acerca de...", command=self.About)

        self.ventana.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.ventana.mainloop()

    def on_closing(self):
        sys.exit()
        self.ventana.destroy()


    def NewFile(self):
        print("New File!")

    def OpenFile(self):
        name =  askopenfilename()
        print (name)

    def AbrirVentanaConfiguracion(self):
        ventanaConfig = VentanaConfig()
        print ("Abriendo la ventana de configuracion")

    def AbrirVentanaCrawler(self):
        ventanaCrawler = VentanaCrawler()
        print ("Iniciando el crawler...")

    def AbrirVentanaTerminal(self):
        ventanaTerminal = VentanaTerminal()
        print ("...Abriendo una terminal")


    def About(self):
        print ("Este es nuestro Menu ")
