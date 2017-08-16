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
from clasificador.dataClasificator import dataClasificator
from Entidades.webPageInfo import webPageInfo

acciones_menu = {}
acciones_submenu = {}
acciones_submenuConfig = {}
acciones_submenuCrawler = {}
acciones_submenuCrawlerR = {}
boolSpyder = False
configuracion = config("./configElTopo/config.json")
ficheroParaEntrenamiento = configuracion.getFicheroParaEntrenamiento()
ficheroParaEntrenamientoGeneradoParaEntrenamiento = configuracion.getFicheroParaEntrenamientoGeneradoParaEntrenamiento()
classificatorObject = classificator(ficheroParaEntrenamiento, configuracion.getRutaFicheroEntrenamientoPersistente(),
                                    configuracion.getRutaJSONTraining(),
                                    ficheroParaEntrenamientoGeneradoParaEntrenamiento)
classificatorObject = classificator(ficheroParaEntrenamiento,
                                    configuracion.getRutaFicheroEntrenamientoPersistente(),
                                    configuracion.getRutaSalidaPreProcesador(),
                                    ficheroParaEntrenamientoGeneradoParaEntrenamiento)

classifier = classificatorObject.getClasifier()
webPageInfoObject = webPageInfo(route='/home/usertfm/SalidaJSON/Preproc/google.es.json')
miClass = dataClasificator(webPageInfoObject, classifier)


def letrasInicio(screen):
    x = 0
    while x < 1000:
        screen.print_at('El topo',
                        randint(0, screen.width), randint(0, screen.height),
                        colour=randint(0, screen.colours - 1),
                        bg=randint(0, screen.colours - 1))
        ev = screen.get_key()
        screen.refresh()
        x += 1


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
    print("4. Entrenamiento")
    print("5. Clasificador")
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


def sub_menuClasificador():
    os.system('clear')
    print("Menu Clasificador")


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


def exec_submenuClasificador(eleccion):
    os.system('clear')
    ch = eleccion.lower()
    if ch == '':
        acciones_submenuClasificador[ch]()
    else:
        try:
            acciones_submenuClasificador[ch]()
        except KeyError:
            print("Opcion no válida.Seleccionar otra opcion.\n")
            acciones_submenuClasificador['sub_menuClasificador']()


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
    print("1. All data")
    print("2. Title data ")
    print("3. Span data")
    print("4. Meta data")
    print("5. Paragraph data")
    print("6. Url data")
    print("7. Header data")
    print("9. Volver")
    print("0. Salir")
    eleccion = input(" >>  ")

    exec_submenuClasificador(eleccion)
    return


def Configurar():
    print("Editar el fichero.json")
    time.sleep(5)
    menu_principal()


def IniciarCrawlerL():
    print("Iniciando crawler local")
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


def Entrenador():
    # Menu de botones

    print("Iniciando Entrenamiento...")
    time.sleep(3)
    menu_principal()
    # Llamada al método de entrenamiento


def Alldata():
    print(miClass.classifyAllHeaders())
    time.sleep(3)
    sub_menuClasificador()

def Titledata():
    print(miClass.classifyAllTitles())
    time.sleep(3)
sub_menuClasificador()
def Spandata():
    print(miClass.classifyAllSpan())
    time.sleep(3)
sub_menuClasificador()
def Metadata():
    print(miClass.classifyAllMeta())
    time.sleep(3)
    sub_menuClasificador()

def Paragraphdata():
    print(miClass.classifyAllParrafos())
    time.sleep(3)
sub_menuClasificador()

def Urldata():
    print(miClass.classifyAllUrl())
    time.sleep(3)
sub_menuClasificador()
def Headerdata():
    print(miClass.classifyAllHeaders())
    time.sleep(3)
    sub_menuClasificador()

def back():
    acciones_menu['main_menu']()


def exit():
    sys.exit()


acciones_menu = {
    'main_menu': menu_principal,
    '1': Configuracion,
    '2': CrawlerL,
    '3': CrawlerR,
    '4': Entrenador,
    '5': Clasificador,
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
acciones_submenuClasificador = {
    'sub_menuClasificador': sub_menuClasificador,
    '1': Alldata,
    '2': Titledata,
    '3': Metadata,
    '4': Spandata,
    '5': Urldata,
    '6': Headerdata,
    '9': back,
    '0': exit
}

if __name__ == "__main__":
    menu_principal()
