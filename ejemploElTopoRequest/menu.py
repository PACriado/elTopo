import sys, os
from interfazGrafica.VentanaConfig import VentanaConfig
from interfazGrafica.VentanaConfigCrawler import VentanaConfigCrawler
from interfazGrafica.VentanaCrawler import VentanaCrawler
from interfazGrafica.VentanaClasificador import VentanaClasificador
from interfazGrafica.VentanaEntrenamiento import VentanaEntrenamiento

acciones_menu = {}
acciones_submenu = {}

def menu_principal():
    os.system('clear')

    print("===============================")
    print(" MENU PRINCIPAL: EL TOPO       ")
    print("===============================")
    print("Seleccione una opción del menu:")
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print("\n")
    print("1. Configuracion")
    print("2. Crawler")
    print("3. Clasificador")
    print("\n0. Salir")
    eleccion = input(" >>  ")
    exec_menu(eleccion)
    return

def sub_menuConfig():
    os.system('clear')
    print("Menu Configuracion\n")
    print("1.Configurar")
    print("9. Volver")
    print("0. Salir")
    eleccion = input(" >>  ")
    exec_submenuConfig(eleccion)

def sub_menuCrawler():
    os.system('clear')
    print("Menu Crawler Local\n")
    print("1.Iniciar")
    print("9. Volver")
    print("0. Salir")
    eleccion = input(" >>  ")
    exec_submenuCrawler(eleccion)

def sub_menuCrawlerR():
    os.system('clear')
    print("Menu Crawler Remoto\n")
    print("1.Iniciar")
    print("9. Volver")
    print("0. Salir")
    eleccion = input(" >>  ")
    exec_submenuCrawlerR(eleccion)

def exec_menu(eleccion):
    os.system('clear')
    ch = eleccion.lower()
    if ch == '':
        acciones_menu['main_menu']()

    else:
        try:
            acciones_menu[ch]()
        except KeyError:
            print("Opción invalida. Seleccione otra opción.\n")
            acciones_menu['main_menu']()
    return

def exec_submenuConfig(eleccion):
    os.system('clear')
    ch = eleccion.lower()
    print("hey")
    if ch == '':
        acciones_submenuConfig[ch]()
        print("hey2")
    else:
        try:
            acciones_submenuConfig[ch]
            print("hey3")
        except KeyError:
            print("Opcion no válida.Seleccionar otra opcion.\n")
            acciones_submenuConfig['sub_menuConfig']()

def exec_submenuCrawler(eleccion):
    os.system('clear')
    ch = eleccion.lower()
    if ch == '':
        acciones_submenuCrawler

def exec_submenuCrawlerR(eleccion):
    os.system('clear')
    ch = eleccion.lower()
    if ch == '':
        acciones_submenuCrawlerR

def Configuracion():
    print("Menu Configuracion\n")
    print("1.Configurar")
    print("9. Volver")
    print("0. Salir")
    eleccion = input(" >>  ")
    exec_submenuConfig(eleccion)
    return


def Crawler():
    print("Menu Crawler Local\n")
    print("1. Configurar")
    print("2. Abrir")
    print("9. Volver")
    print("0. Salir")
    eleccion = input(" >>  ")
    exec_submenuCrawler(eleccion)
    return

def CrawlerR():
    print("Menu Crawler Remoto\n")
    print("1. Configurar")
    print("2. Abrir")
    print("9. Volver")
    print("0. Salir")
    eleccion = input(" >>  ")
    exec_submenuCrawlerR(eleccion)
    return

def Clasificador():
    print("Menu Clasificador\n")
    print("1. Clasificar")
    print("9. Volver")
    print("0. Salir")
    eleccion = input(" >>  ")
    exec_menu(eleccion)
    return

def Configurar():
    print("Editar el fichero.json")

def IniciarCrawlerL():
    print("Iniciando crawler local")

def IniciarCrawlerR():
    print("Iniciando crawler remoto")

def Clasificador():
    print("Abrir")
    print("Entrenar")
    #Entrenar

def back():
    acciones_menu['main_menu']()

def exit():
    sys.exit()

acciones_menu = {
    'main_menu': menu_principal,
    '1': Configuracion,
    '2': Crawler,
    '3': Clasificador,
    '9': back,
    '0': exit,
}

acciones_submenuConfig = {
    'sub_menuConfig': sub_menuConfig,
    '1': Configurar,
    '9': back,
    '0': exit
}

acciones_submenuCrawler ={
    'sub_menuCrawler': sub_menuCrawler,
    '1': IniciarCrawlerL,
    '9': back,
    '0': exit
}

acciones_submenuCrawlerR = {
    'sub_menuCrawlerR': sub_menuCrawlerR,
    '1': IniciarCrawlerR,
    '9': back,
    '0': exit
}


if __name__ == "__main__":
    menu_principal()
