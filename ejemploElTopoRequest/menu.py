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
from Entidades.leerFicherosWebPageInfo import leerFicherosWebPageInfo

acciones_menu = {}
acciones_submenu = {}
acciones_submenuConfig = {}
acciones_submenuCrawler = {}
acciones_submenuCrawlerR = {}
boolSpyder = False
ruta_fich = ""
ruta_dir = ""

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


# webPageInfoObject = webPageInfo(route='/home/usertfm/SalidaJSON/Preproc/google.es.json')


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


def sub_menuOpcionesClasificador():
    os.system('clear')
    print("Menu Opciones de Clasificación Fich")


def sub_menuOpcionesClasificadorDir():
    os.system('clear')
    print("Menu Opciones de Clasificación Dir")

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


def exec_submenuOpcionesClasificador(eleccion):
    os.system('clear')
    ch = eleccion.lower()
    if ch == '':
        acciones_submenuOpcionesClasificador[ch]()
    else:
        try:
            acciones_submenuOpcionesClasificador[ch]()
        except KeyError:
            print("Opcion no válida.Seleccionar otra opcion.\n")
            acciones_submenuOpcionesClasificador['sub_menuOpcionesClasificador']()


def exec_submenuOpcionesClasificadorDir(eleccion):
    os.system('clear')
    ch = eleccion.lower()
    if ch == '':
        acciones_submenuOpcionesClasificadorDir[ch]()
        print("He entrado bien")

    else:
        try:
            acciones_submenuOpcionesClasificadorDir[ch]()
            print("He entrado bien")
        except KeyError:
            print("Opcion no válida.Seleccionar otra opcion.\n")
            acciones_submenuOpcionesClasificadorDir['sub_menuOpcionesClasificadorDir']()



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
    print("1. Pedir Fichero")
    print("2. Pedir Directorio ")
    print("9. Volver")
    print("0. Salir")
    eleccion = input(" >>  ")

    exec_submenuClasificador(eleccion)
    return


def OpcionesClasificador():
    print("La ruta es: " + ruta_fich)
    print("Seleccione un tipo de clasificación:\n")
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

    exec_submenuOpcionesClasificador(eleccion)
    return


def OpcionesClasificadorDir():
    print("La ruta es: " + ruta_dir)
    print("Seleccione un tipo de clasificación:\n")
    print("1. All data dir")
    print("2. Title data dir ")
    print("3. Span data dir")
    print("4. Meta data dir")
    print("5. Paragraph data dir")
    print("6. Url data dir")
    print("7. Header data dir")
    print("9. Volver")
    print("0. Salir")
    eleccion = input(" >>  ")

    exec_submenuOpcionesClasificadorDir(eleccion)
    print(eleccion)

    return


def Configurar():
    print("Editar el fichero.json")
    input('Pulse Enter para continuar...')
    menu_principal()


def PedirFich():
    global ruta_fich
    ruta_fich = input("Introducir ruta del fichero: ")
    assert os.path.exists(ruta_fich), "No se ha encontrado el fichero en, " + str(ruta_fich)
    print("Funcionando")
    OpcionesClasificador()
    return ruta_fich


def PedirDir():
    global ruta_dir
    ruta_dir = input("Introducir ruta del directorio: ")
    ruta_dir = ruta_dir + "/"
    assert os.path.exists(ruta_dir), "No se ha encontrado el directorio en, " + str(ruta_dir)
    print("Funcionando")
    OpcionesClasificadorDir()
    return ruta_dir


def IniciarCrawlerL():
    print("Iniciando crawler local")
    theSpyder = spyder(rutaConfig="./configElTopo/config.json")
    rutaSalidaSpyder = theSpyder.launch()
    procesador = Preprocesator(rutaSalidaSpyder + "onLine/", configuracion.getRutaSalidaPreProcesador())
    procesador.process()
    input('Pulse Enter para continuar...')
    menu_principal()


def IniciarCrawlerR():
    print("Iniciando crawler remoto")
    caller = SpyderRestCaller()
    paths = caller.callList()
    print(paths)
    input('Pulse Enter para continuar...')
    menu_principal()


def Entrenador():
    # Menu de botones
    # print("Iniciando Entrenamiento...")

    classificatorObject = classificator(ficheroParaEntrenamiento,
                                        configuracion.getRutaFicheroEntrenamientoPersistenteHeaderData(),
                                        configuracion.getRutaJSONTraining(),
                                        ficheroParaEntrenamientoGeneradoParaEntrenamiento)
    classificatorObject.generateJsonHeaderData()
    classificatorObject.training()
    classificatorObject = classificator(ficheroParaEntrenamiento,
                                        configuracion.getRutaFicheroEntrenamientoPersistenteUrlData(),
                                        configuracion.getRutaJSONTraining(),
                                        ficheroParaEntrenamientoGeneradoParaEntrenamiento)
    classificatorObject.generateJsonUrlData()
    classificatorObject.training()
    classificatorObject = classificator(ficheroParaEntrenamiento,
                                        configuracion.getRutaFicheroEntrenamientoPersistenteMetaData(),
                                        configuracion.getRutaJSONTraining(),
                                        ficheroParaEntrenamientoGeneradoParaEntrenamiento)
    classificatorObject.generateJsonMetaData()
    classificatorObject.training()
    classificatorObject = classificator(ficheroParaEntrenamiento,
                                        configuracion.getRutaFicheroEntrenamientoPersistenteSpanData(),
                                        configuracion.getRutaJSONTraining(),
                                        ficheroParaEntrenamientoGeneradoParaEntrenamiento)
    classificatorObject.generateJsonSpanData()
    classificatorObject.training()
    classificatorObject = classificator(ficheroParaEntrenamiento,
                                        configuracion.getRutaFicheroEntrenamientoPersistenteTitle(),
                                        configuracion.getRutaJSONTraining(),
                                        ficheroParaEntrenamientoGeneradoParaEntrenamiento)
    classificatorObject.generateJsonTitleData()
    classificatorObject.training()
    classificatorObject = classificator(ficheroParaEntrenamiento,
                                        configuracion.getRutaFicheroEntrenamientoPersistenteParagraphData(),
                                        configuracion.getRutaJSONTraining(),
                                        ficheroParaEntrenamientoGeneradoParaEntrenamiento)
    classificatorObject.generateJsonParagraphData()
    classificatorObject.training()
    classificatorObject = classificator(ficheroParaEntrenamiento,
                                        configuracion.getRutaFicheroEntrenamientoPersistente(),
                                        configuracion.getRutaJSONTraining(),
                                        ficheroParaEntrenamientoGeneradoParaEntrenamiento)
    classificatorObject.generateJsonWithAllData()
    classificatorObject.training()
    input('Pulse Enter para continuar...')
    menu_principal()
    # Llamada al método de entrenamiento


def Alldata():
    # Falta este método por hacer en el main

    # print(miClass.classifyAllHeaders())
    input('Pulse Enter para volver al menu...')
    OpcionesClasificador()


def Titledata():
    classificatorObject = classificator(ficheroParaEntrenamiento,
                                        configuracion.getRutaFicheroEntrenamientoPersistenteTitle(),
                                        configuracion.getRutaJSONTraining(),
                                        ficheroParaEntrenamientoGeneradoParaEntrenamiento)
    print("Cargado Classifier Title...")

    classifier = classificatorObject.getClasifier()
    print("Classifier Cargado")
    webPageInfoObject = webPageInfo(route=ruta_fich)
    clasificator = dataClasificator(webPageInfoObject, classifier)
    estadisticas = clasificator.accuracyAllByCategory("TITLE", configuracion.getRutaFicheroCategorias())
    for estadistica in estadisticas:
        print(estadistica.getcategory())
        print(estadistica.getstatistic())

    input('Pulse Enter para volver al menu...')
    OpcionesClasificador()


def Spandata():
    classificatorObject = classificator(ficheroParaEntrenamiento,
                                        configuracion.getRutaFicheroEntrenamientoPersistenteSpanData(),
                                        configuracion.getRutaJSONTraining(),
                                        ficheroParaEntrenamientoGeneradoParaEntrenamiento)
    print("Cargado Classifier Spans...")

    classifier = classificatorObject.getClasifier()
    print("Classifier Cargado")
    webPageInfoObject = webPageInfo(route=ruta_fich)
    clasificator = dataClasificator(webPageInfoObject, classifier)

    estadisticas = clasificator.accuracyAllByCategory("SPAN", configuracion.getRutaFicheroCategorias())
    for estadistica in estadisticas:
        print(estadistica.getcategory())
        print(estadistica.getstatistic())

    input('Pulse Enter para volver al menu...')
    OpcionesClasificador()


def Metadata():
    classificatorObject = classificator(ficheroParaEntrenamiento,
                                        configuracion.getRutaFicheroEntrenamientoPersistenteMetaData(),
                                        configuracion.getRutaJSONTraining(),
                                        ficheroParaEntrenamientoGeneradoParaEntrenamiento)
    print("Cargado Classifier Meta...")
    classifier = classificatorObject.getClasifier()
    print("Classifier Cargado")
    webPageInfoObject = webPageInfo(route=ruta_fich)
    clasificator = dataClasificator(webPageInfoObject, classifier)
    estadisticas = clasificator.accuracyAllByCategory("META", configuracion.getRutaFicheroCategorias())
    for estadistica in estadisticas:
        print(estadistica.getcategory())
        print(estadistica.getstatistic())

    input('Pulse Enter para volver al menu...')
    OpcionesClasificador()


def Paragraphdata():
    classificatorObject = classificator(ficheroParaEntrenamiento,
                                        configuracion.getRutaFicheroEntrenamientoPersistenteParagraphData(),
                                        configuracion.getRutaJSONTraining(),
                                        ficheroParaEntrenamientoGeneradoParaEntrenamiento)
    print("Cargado Classifier Paragraph...")
    classifier = classificatorObject.getClasifier()
    print("Classifier Cargado")
    webPageInfoObject = webPageInfo(route=ruta_fich)
    clasificator = dataClasificator(webPageInfoObject, classifier)
    estadisticas = clasificator.accuracyAllByCategory("PARRAFO", configuracion.getRutaFicheroCategorias())
    for estadistica in estadisticas:
        print(estadistica.getcategory())
        print(estadistica.getstatistic())

    input('Pulse Enter para volver al menu...')
    OpcionesClasificador()


def Urldata():
    classificatorObject = classificator(ficheroParaEntrenamiento,
                                        configuracion.getRutaFicheroEntrenamientoPersistenteUrlData(),
                                        configuracion.getRutaJSONTraining(),
                                        ficheroParaEntrenamientoGeneradoParaEntrenamiento)
    print("Cargado Classifier URL...")
    classifier = classificatorObject.getClasifier()
    print("Classifier Cargado")
    webPageInfoObject = webPageInfo(route=ruta_fich)
    clasificator = dataClasificator(webPageInfoObject, classifier)
    estadisticas = clasificator.accuracyAllByCategory("URL", configuracion.getRutaFicheroCategorias())
    for estadistica in estadisticas:
        print(estadistica.getcategory())
        print(estadistica.getstatistic())

    input('Pulse Enter para volver al menu...')
    OpcionesClasificador()


def Headerdata():

    classificatorObject = classificator(ficheroParaEntrenamiento,
                                        configuracion.getRutaFicheroEntrenamientoPersistenteHeaderData(),
                                        configuracion.getRutaJSONTraining(),
                                        ficheroParaEntrenamientoGeneradoParaEntrenamiento)

    print("Cargado Classifier Header...")
    classifier = classificatorObject.getClasifier()
    print("Classifier Cargado")
    print("Funcionando")
    webPageInfoObject = webPageInfo(route=ruta_fich)
    clasificator = dataClasificator(webPageInfoObject, classifier)
    estadisticas = clasificator.accuracyAllByCategory("HEADER", configuracion.getRutaFicheroCategorias())
    for estadistica in estadisticas:
        print(estadistica.getcategory())
        print(estadistica.getstatistic())

    input('Pulse Enter para volver al menu...')
    OpcionesClasificador()


# ************************Opciones Directorio*****************************************

def AlldataDir():
    # Falta este método por hacer en el main

    # print(miClass.classifyAllHeaders())
    input('Pulse Enter para volver al menu...')
    OpcionesClasificador()


def TitledataDir():
    classificatorObject = classificator(ficheroParaEntrenamiento,
                                        configuracion.getRutaFicheroEntrenamientoPersistenteTitle(),
                                        configuracion.getRutaJSONTraining(),
                                        ficheroParaEntrenamientoGeneradoParaEntrenamiento)
    print("Cargado Classifier Title...")

    classifier = classificatorObject.getClasifier()
    print("Classifier Cargado")
    webPageInfoObject = webPageInfo(route=ruta_fich)
    clasificator = dataClasificator(webPageInfoObject, classifier)
    estadisticas = clasificator.accuracyAllByCategory("TITLE", configuracion.getRutaFicheroCategorias())
    for estadistica in estadisticas:
        print(estadistica.getcategory())
        print(estadistica.getstatistic())

    input('Pulse Enter para volver al menu...')
    OpcionesClasificador()


def SpandataDir():
    classificatorObject = classificator(ficheroParaEntrenamiento,
                                        configuracion.getRutaFicheroEntrenamientoPersistenteSpanData(),
                                        configuracion.getRutaJSONTraining(),
                                        ficheroParaEntrenamientoGeneradoParaEntrenamiento)
    print("Cargado Classifier Spans...")

    classifier = classificatorObject.getClasifier()
    print("Classifier Cargado")
    webPageInfoObject = webPageInfo(route=ruta_fich)
    clasificator = dataClasificator(webPageInfoObject, classifier)

    estadisticas = clasificator.accuracyAllByCategory("SPAN", configuracion.getRutaFicheroCategorias())
    for estadistica in estadisticas:
        print(estadistica.getcategory())
        print(estadistica.getstatistic())

    input('Pulse Enter para volver al menu...')
    OpcionesClasificador()


def MetadataDir():
    classificatorObject = classificator(ficheroParaEntrenamiento,
                                        configuracion.getRutaFicheroEntrenamientoPersistenteMetaData(),
                                        configuracion.getRutaJSONTraining(),
                                        ficheroParaEntrenamientoGeneradoParaEntrenamiento)
    print("Cargado Classifier Meta...")
    classifier = classificatorObject.getClasifier()
    print("Classifier Cargado")
    webPageInfoObject = webPageInfo(route=ruta_fich)
    clasificator = dataClasificator(webPageInfoObject, classifier)
    estadisticas = clasificator.accuracyAllByCategory("META", configuracion.getRutaFicheroCategorias())
    for estadistica in estadisticas:
        print(estadistica.getcategory())
        print(estadistica.getstatistic())

    input('Pulse Enter para volver al menu...')
    OpcionesClasificador()


def ParagraphdataDir():
    classificatorObject = classificator(ficheroParaEntrenamiento,
                                        configuracion.getRutaFicheroEntrenamientoPersistenteParagraphData(),
                                        configuracion.getRutaJSONTraining(),
                                        ficheroParaEntrenamientoGeneradoParaEntrenamiento)
    print("Cargado Classifier Paragraph...")
    classifier = classificatorObject.getClasifier()
    print("Classifier Cargado")
    webPageInfoObject = webPageInfo(route=ruta_fich)
    clasificator = dataClasificator(webPageInfoObject, classifier)
    estadisticas = clasificator.accuracyAllByCategory("PARRAFO", configuracion.getRutaFicheroCategorias())
    for estadistica in estadisticas:
        print(estadistica.getcategory())
        print(estadistica.getstatistic())

    input('Pulse Enter para volver al menu...')
    OpcionesClasificador()


def UrldataDir():
    classificatorObject = classificator(ficheroParaEntrenamiento,
                                        configuracion.getRutaFicheroEntrenamientoPersistenteUrlData(),
                                        configuracion.getRutaJSONTraining(),
                                        ficheroParaEntrenamientoGeneradoParaEntrenamiento)
    print("Cargado Classifier URL...")
    classifier = classificatorObject.getClasifier()
    print("Classifier Cargado")
    webPageInfoObject = webPageInfo(route=ruta_fich)
    clasificator = dataClasificator(webPageInfoObject, classifier)
    estadisticas = clasificator.accuracyAllByCategory("URL", configuracion.getRutaFicheroCategorias())
    for estadistica in estadisticas:
        print(estadistica.getcategory())
        print(estadistica.getstatistic())

    input('Pulse Enter para volver al menu...')
    OpcionesClasificador()


def HeaderdataDir():

    print("Entro aquiiiiii")
    allObjects = leerFicherosWebPageInfo.readAllFilesInDirectory(ruta_dir)
    for webPageInfoObject in allObjects:
        classificatorObject = classificator(ficheroParaEntrenamiento,
                                            configuracion.getRutaFicheroEntrenamientoPersistenteHeaderData(),
                                            configuracion.getRutaJSONTraining(),
                                            ficheroParaEntrenamientoGeneradoParaEntrenamiento)

        print("Cargado Classifier Headers...")
        classifier = classificatorObject.getClasifier()
        print("Classifier Cargado")
        clasificator = dataClasificator(webPageInfoObject, classifier)
        # print(clasificator.classifyAllHeaders())
        # print(clasificator.accuracyAll("HEADER", "Armas"))
        estadisticasResultado = clasificator.accuracyAllByCategory("HEADER",
                                                                   configuracion.getRutaFicheroCategorias(),
                                                                   URL=webPageInfoObject.getUrl())
        print("Clasificada la URL {0} ".format(webPageInfoObject.getUrl()))
        for estadistica in estadisticasResultado:
            print(estadistica.getcategory())
            print(estadistica.getstatistic())

    input('Pulse Enter para volver al menu...')
    OpcionesClasificadorDir()


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
    '1': PedirFich,
    '2': PedirDir,
    '9': back,
    '0': exit
}
acciones_submenuOpcionesClasificador = {
    'sub_menuOpcionesClasificador': sub_menuOpcionesClasificador,
    '1': Alldata,
    '2': Titledata,
    '3': Spandata,
    '4': Metadata,
    '5': Paragraphdata,
    '6': Urldata,
    '7': Headerdata,
    '9': back,
    '0': exit
}

acciones_submenuOpcionesClasificadorDir = {

    'sub_menuOpcionesClasificadorDir': sub_menuOpcionesClasificadorDir,
    '1': AlldataDir,
    '2': TitledataDir,
    '3': SpandataDir,
    '4': MetadataDir,
    '5': ParagraphdataDir,
    '6': UrldataDir,
    '7': HeaderdataDir,
    '9': back,
    '0': exit
}
if __name__ == "__main__":
    os.system('clear')
    # Screen.wrapper(letrasInicio)
    menu_principal()
