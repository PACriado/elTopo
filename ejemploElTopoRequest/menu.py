import sys, os, time
from spyder.spyder import spyder
from clasificador.classificator import classificator
from spyderRestCaller.SpyderRestCaller import SpyderRestCaller
from EntidadesRest.SpyderRequest import SpyderRequest
from preProcesador.preProcesator import Preprocesator
from configElTopo.config import config
from spyderRest import spyderRest
from random import randint
from asciimatics.screen import Screen

acciones_menu = {}
acciones_submenu = {}
acciones_submenuConfig = {}
acciones_submenuCrawler = {}
acciones_submenuCrawlerR = {}
boolSpyder = False



def letrasInicio(screen):
    x = 0
    while x<1000:
        screen.print_at('El topo',
                        randint(0, screen.width), randint(0, screen.height),
                        colour=randint(0, screen.colours - 1),
                        bg=randint(0, screen.colours - 1))
        ev = screen.get_key()
        screen.refresh()
        x+=1




def menu_principal():
    os.system('clear')

    Screen.wrapper(letrasInicio)


    print("===============================")
    print(" MENU PRINCIPAL: EL TOPO       ")
    print("===============================")
    print("Seleccione una opción del menu:")
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print("\n")
    print("1. Configuracion")
    print("2. Crawler Local")
    print("3. Crawler Remoto")
    print("4. Clasificador")
    print("\n0. Salir")
    eleccion = input(" >>  ")
    print(eleccion)
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
    return


def sub_menuCrawler():
    os.system('clear')
    print("Menu Crawler Local\n")
    print("1.Iniciar")
    print("9. Volver")
    print("0. Salir")
    eleccion = input(" >>  ")
    exec_submenuCrawler(eleccion)
    return


def sub_menuCrawlerR():
    os.system('clear')
    print("Menu Crawler Remoto\n")
    print("1.Iniciar")
    print("9. Volver")
    print("0. Salir")
    eleccion = input(" >>  ")
    exec_submenuCrawlerR(eleccion)
    return


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
    if ch == '':
        acciones_submenuConfig[ch]()
    else:
        try:
            acciones_submenuConfig[ch]()
        except KeyError:
            print("Opcion no válida.Seleccionar otra opcion.\n")
            acciones_submenuConfig['sub_menuConfig']()


def exec_submenuCrawler(eleccion):
    os.system('clear')
    ch = eleccion.lower()
    if ch == '':
        acciones_submenuCrawler[ch]()
    else:
        try:
            acciones_submenuCrawler[ch]()
        except KeyError:
            print("Opcion no válida.Seleccionar otra opcion.\n")
            acciones_submenuCrawler['sub_menuCrawler']()




def exec_submenuCrawlerR(eleccion):
    os.system('clear')
    ch = eleccion.lower()
    if ch == '':
            acciones_submenuCrawlerR[ch]()
    else:
        try:
                acciones_submenuCrawlerR[ch]()
        except KeyError:
            print("Opcion no válida.Seleccionar otra opcion.\n")
            acciones_submenuCrawlerR['sub_menuCrawlerR']()


def Configuracion():
    print("Menu Configuracion\n")
    print("1.Configurar")
    print("9. Volver")
    print("0. Salir")
    eleccion = input(" >>  ")
    print(eleccion)
    exec_submenuConfig(eleccion)


def CrawlerL():
    print("Menu Crawler Local\n")
    print("1. Iniciar")
    print("9. Volver")
    print("0. Salir")
    eleccion = input(" >>  ")
    exec_submenuCrawler(eleccion)
    return


def CrawlerR():
    print("Menu Crawler Remoto\n")
    print("1. Iniciar Crawler Remoto")
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
    time.sleep(5)
    menu_principal()


def IniciarCrawlerL():
    print("Iniciando crawler local")
    configuracion = config("./configElTopo/config.json")
    theSpyder = spyder(rutaConfig="./configElTopo/config.json")
    rutaSalidaSpyder = theSpyder.launch()
    procesador = Preprocesator(rutaSalidaSpyder + "onLine/", configuracion.getRutaSalidaPreProcesador())
    procesador.process()
    time.sleep(7)
    menu_principal()


def IniciarCrawlerR():
    print("Iniciando crawler remoto")
    caller = SpyderRestCaller()
    paths = caller.callList()
    print(paths)
    time.sleep(15)
    menu_principal()


def Clasificador():
    print("Abrir")
    print("Entrenar")
    # Entrenar


def back():
    acciones_menu['main_menu']()


def exit():
    sys.exit()


acciones_menu = {
    'main_menu': menu_principal,
    '1': Configuracion,
    '2': CrawlerL,
    '3': CrawlerR,
    '4': Clasificador,
    '9': back,
    '0': exit,
}

acciones_submenuConfig = {
    'sub_menuConfig': sub_menuConfig,
    '1': Configurar,
    '9': back,
    '0': exit
}

acciones_submenuCrawler = {
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
