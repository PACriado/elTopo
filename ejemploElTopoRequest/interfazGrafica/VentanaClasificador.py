from tkinter import *
from tkinter import ttk
import sys
from tkinter.filedialog import askdirectory
from tkinter.filedialog import askopenfilename
from configElTopo.config import config
from clasificador.classificator import classificator
from clasificador.dataClasificator import dataClasificator
from Entidades.webPageInfo import webPageInfo
from Entidades.leerFicherosWebPageInfo import leerFicherosWebPageInfo
from interfazGrafica.grafico_barras import grafico_barras


class VentanaClasificador():
    def __init__(self):
        self.ventana = Tk()
        self.ventana.title('Clasificador')
        self.estadisticasResultado=[]

        # self.toolbar = Frame(self.ventana)
        # self.toolbar.pack(side="top", fill="x")

        #self.marco = ttk.Frame(self.ventana, borderwidth=1)
        #self.marco.grid(row=0, column=0)

        self.configuracion = config("./configElTopo/config.json")

        self.ficheroParaEntrenamiento = self.configuracion.getFicheroParaEntrenamiento()
        self.ficheroParaEntrenamientoGeneradoParaEntrenamiento = self.configuracion.getFicheroParaEntrenamientoGeneradoParaEntrenamiento()

        self.BTN_Abrirdir = ttk.Button(self.ventana, text="Abrir directorio", command=self.ruta_text,width=30)
        self.BTN_Header = ttk.Button(self.ventana, text="Header data", command=self.classificator_header_directory)
        self.BTN_Url = ttk.Button(self.ventana, text="Url data", command=self.classificator_url_directory)
        self.BTN_Paragraph = ttk.Button(self.ventana, text="Paragraph data",
                                        command=self.classificator_paragraph_directory)
        self.BTN_Metadata = ttk.Button(self.ventana, text="Meta data", command=self.classificator_metadata_directory)
        self.BTN_Span = ttk.Button(self.ventana, text="Span data", command=self.classificator_span_directory)
        self.BTN_Title = ttk.Button(self.ventana, text="Title data", command=self.classificator_title_directory)
        self.BTN_All = ttk.Button(self.ventana, text="All data", command=self.classificator_alldata_directory)
        self.url = ttk.Entry(self.ventana, width=80)
        self.BTN_VerUltimosResultados = ttk.Button(self.ventana, text="Ver ultimos resultados", command=self.mostrarVentanaDatos)

        self.BTN_Abrirfich = ttk.Button(self.ventana, text="Abrir fichero", command=self.ruta_textfich,width=30)
        self.BTN_Headerfich = ttk.Button(self.ventana, text="Header data", command=self.classificator_header)
        self.BTN_Urlfich = ttk.Button(self.ventana, text="Url data", command=self.classificator_url)
        self.BTN_Paragraphfich = ttk.Button(self.ventana, text="Paragraph data", command=self.classificator_paragraph)
        self.BTN_Metadatafich = ttk.Button(self.ventana, text="Meta data", command=self.classificator_metadata)
        self.BTN_Spanfich = ttk.Button(self.ventana, text="Span data", command=self.classificator_span)
        self.BTN_Titlefich = ttk.Button(self.ventana, text="Title data", command=self.classificator_title)
        self.BTN_Allfich = ttk.Button(self.ventana, text="All data", command=self.classificator_alldata)
        self.urlfich = ttk.Entry(self.ventana, width=80)

        self.BTN_Header.config(state="disabled")
        self.BTN_Url.config(state="disabled")
        self.BTN_Paragraph.config(state="disabled")
        self.BTN_Metadata.config(state="disabled")
        self.BTN_Span.config(state="disabled")
        self.BTN_Title.config(state="disabled")
        self.BTN_All.config(state="disabled")

        self.BTN_Headerfich.config(state="disabled")
        self.BTN_Urlfich.config(state="disabled")
        self.BTN_Paragraphfich.config(state="disabled")
        self.BTN_Metadatafich.config(state="disabled")
        self.BTN_Spanfich.config(state="disabled")
        self.BTN_Titlefich.config(state="disabled")
        self.BTN_Allfich.config(state="disabled")
        self.BTN_VerUltimosResultados.config(state="disabled")

        # Fila 1 :

        self.BTN_Abrirdir.grid(row=0, column=0)
        self.url.grid(row=0, column=1)

        # Filas 2-8 :
        self.BTN_Header.grid(row=1, column=1,sticky=S+N+E+W)
        self.BTN_Paragraph.grid(row=2, column=1,sticky=S+N+E+W)
        self.BTN_Span.grid(row=3, column=1,sticky=S+N+E+W)
        self.BTN_Url.grid(row=4, column=1,sticky=S+N+E+W)
        self.BTN_Title.grid(row=5, column=1,sticky=S+N+E+W)
        self.BTN_Metadata.grid(row=6, column=1, sticky=S+N+E+W)
        self.BTN_All.grid(row=7, column=1,sticky=S+N+E+W)

        # Fila 10 :

        self.BTN_Abrirfich.grid(row=9, column=0,sticky=NW)
        self.urlfich.grid(row=9, column=1)

        # Filas 11-17 :
        self.BTN_Headerfich.grid(row=10, column=1,sticky=S+N+E+W)
        self.BTN_Paragraphfich.grid(row=11, column=1,sticky=S+N+E+W)
        self.BTN_Spanfich.grid(row=12, column=1,sticky=S+N+E+W)
        self.BTN_Urlfich.grid(row=13, column=1,sticky=S+N+E+W)
        self.BTN_Titlefich.grid(row=14, column=1,sticky=S+N+E+W)
        self.BTN_Allfich.grid(row=15, column=1,sticky=S+N+E+W)
        self.BTN_Metadatafich.grid(row=16, column=1,sticky=S+N+E+W)

        # Fila 18:
        self.text = Text(self.ventana, wrap="word")
        # self.text.pack(side="top", fill="both", expand=True)
        self.text.grid(row=17, column=1)
        self.text.tag_configure("stderr", foreground="#b22222")
        sys.stdout = TextRedirector(self.text, "stdout")

        self.separador1 = ttk.Separator(self.ventana, orient=HORIZONTAL)
        self.separador1.grid(row=17, column=0)

        # Fila 13

        self.BTN_VerUltimosResultados.grid(row=19, column=1)

        '''BTN_ClasificarFich = ttk.Button(self.marco, text="Clasificar fichero", command=self.ruta_textfich)
        BTN_ClasificarDir = ttk.Button(self.marco, text="Clasificar directorio", command=self.classificator_header)
        BTN_ClasificarDir.grid(row=12,column=0)
        BTN_ClasificarFich.grid(row=12,column=1)'''





        # BTN_Iniciar.pack(in_=self.toolbar, side="left")
        # BTN_Abrirdir.(in_=self.toolbar, side="left")
        # self.url.pack(in_=self.toolbar, side="left")
        # BTN_Header.pack(in_=self.toolbar, side="bottom")
        # BTN_Url.pack(in_=self.toolbar, side="bottom")
        # BTN_Paragraph.pack(in_=self.toolbar, side="bottom")
        # BTN_Metadata.pack(in_=self.toolbar, side="bottom")
        # BTN_Span.pack(in_=self.toolbar, side="bottom")
        # BTN_Title.pack(in_=self.toolbar, side="bottom")
        # BTN_All.pack(in_=self.toolbar, side="bottom")

    '''def print_stdout(self):
        # configuracion = config("./configElTopo/config.json")
        # ficheroParaEntrenamiento = self.configuracion.getFicheroParaEntrenamiento()
        # ficheroParaEntrenamientoGeneradoParaEntrenamiento = self.configuracion.getFicheroParaEntrenamientoGeneradoParaEntrenamiento()
        # casificatorObject = classificator(ficheroParaEntrenamiento, self.configuracion.getRutaFicheroEntrenamientoPersistente(), self.configuracion.getRutaSalidaPreProcesador(), ficheroParaEntrenamientoGeneradoParaEntrenamiento)

        print("AQUI SI QUE ENTRA")

        # print(classifier.classify("tumadre"))'''

    def mostrarVentanaDatos(self):
        for dominio in self.estadisticasResultado:
            grafico_barras(dominio)



    def ruta_text(self):
        result = askdirectory()
        self.url.delete(0, 'end')
        self.url.insert(0, result)
        # self.url.pack(in_=self.marco, side="left")
        self.url.grid(row=0, column=1)
        self.BTN_Header.config(state="normal")
        self.BTN_Url.config(state="normal")
        self.BTN_Paragraph.config(state="normal")
        self.BTN_Metadata.config(state="normal")
        self.BTN_Span.config(state="normal")
        self.BTN_Title.config(state="normal")
        self.BTN_All.config(state="normal")
        self.BTN_VerUltimosResultados.config(state="normal")

        self.BTN_Headerfich.config(state="disabled")
        self.BTN_Urlfich.config(state="disabled")
        self.BTN_Paragraphfich.config(state="disabled")
        self.BTN_Metadatafich.config(state="disabled")
        self.BTN_Spanfich.config(state="disabled")
        self.BTN_Titlefich.config(state="disabled")
        self.BTN_Allfich.config(state="disabled")


    def ruta_textfich(self):
        result = askopenfilename()
        self.urlfich.delete(0, 'end')
        self.urlfich.insert(0, result)
        # self.url.pack(in_=self.marco, side="left")
        self.urlfich.grid(row=9, column=1,sticky=NW)
        self.BTN_Header.config(state="disabled")
        self.BTN_Url.config(state="disabled")
        self.BTN_Paragraph.config(state="disabled")
        self.BTN_Metadata.config(state="disabled")
        self.BTN_Span.config(state="disabled")
        self.BTN_Title.config(state="disabled")
        self.BTN_All.config(state="disabled")

        self.BTN_Headerfich.config(state="normal")
        self.BTN_Urlfich.config(state="normal")
        self.BTN_Paragraphfich.config(state="normal")
        self.BTN_Metadatafich.config(state="normal")
        self.BTN_Spanfich.config(state="normal")
        self.BTN_Titlefich.config(state="normal")
        self.BTN_Allfich.config(state="normal")
        self.BTN_VerUltimosResultados.config(state="normal")



    #  FICHERO

    def classificator_header(self):
        self.estadisticasResultado=[]
        webPageInfoObject = webPageInfo(route=self.urlfich.get())
        classificatorObject = classificator(self.ficheroParaEntrenamiento,
                                            self.configuracion.getRutaFicheroEntrenamientoPersistenteHeaderData(),
                                            self.configuracion.getRutaJSONTraining(),
                                            self.ficheroParaEntrenamientoGeneradoParaEntrenamiento)
        print("Cargado Classifier Headers...")
        classifier = classificatorObject.getClasifier()
        print("Classifier Cargado")
        clasificator = dataClasificator(webPageInfoObject, classifier)
        # print(clasificator.classifyAllHeaders())
        # print(clasificator.accuracyAll("HEADER", "Armas"))
        estadisticasResultado = clasificator.accuracyAllByCategory("HEADER", self.configuracion.getRutaFicheroCategorias(),
                                                          URL=webPageInfoObject.getUrl())
        print("Clasificada la URL {0} ".format(webPageInfoObject.getUrl()))
        self.estadisticasResultado.append(estadisticasResultado)
        for estadistica in estadisticasResultado:
            print(estadistica.getcategory())
            print(estadistica.getstatistic())
        self.dibujarSeparador()

    def classificator_url(self):
        self.estadisticasResultado=[]
        webPageInfoObject = webPageInfo(route=self.urlfich.get())
        classificatorObject = classificator(self.ficheroParaEntrenamiento,
                                            self.configuracion.getRutaFicheroEntrenamientoPersistenteUrlData(),
                                            self.configuracion.getRutaJSONTraining(),
                                            self.ficheroParaEntrenamientoGeneradoParaEntrenamiento)
        print("Cargado Classifier URL...")
        classifier = classificatorObject.getClasifier()
        print("Classifier Cargado")
        clasificator = dataClasificator(webPageInfoObject, classifier)
        # print(clasificator.classifyAllUrl())
        # print(clasificator.accuracyAll("URL", "Armas"))
        estadisticasResultado = clasificator.accuracyAllByCategory("URL", self.configuracion.getRutaFicheroCategorias(),
                                                          URL=webPageInfoObject.getUrl())
        print("Clasificada la URL {0} ".format(webPageInfoObject.getUrl()))
        self.estadisticasResultado.append(estadisticasResultado)
        for estadistica in estadisticasResultado:
            print(estadistica.getcategory())
            print(estadistica.getstatistic())
        self.dibujarSeparador()

    def classificator_alldata(self):
        self.estadisticasResultado=[]
        webPageInfoObject = webPageInfo(route=self.urlfich.get())
        classificatorObject = classificator(self.ficheroParaEntrenamiento,
                                            self.configuracion.getRutaFicheroEntrenamientoPersistente(),
                                            self.configuracion.getRutaJSONTraining(),
                                            self.ficheroParaEntrenamientoGeneradoParaEntrenamiento)
        print("Cargado Classifier All data...")
        classifier = classificatorObject.getClasifier()
        print("Classifier Cargado")
        clasificator = dataClasificator(webPageInfoObject, classifier)
        # print(clasificator.classifyAllUrl())
        # print(clasificator.accuracyAll("URL", "Armas"))
        estadisticasResultado = clasificator.accuracyAllByCategory("PARRAFO", self.configuracion.getRutaFicheroCategorias(),
                                                          URL=webPageInfoObject.getUrl())
        print("Clasificada la URL {0} ".format(webPageInfoObject.getUrl()))
        self.estadisticasResultado.append(estadisticasResultado)
        for estadistica in estadisticasResultado:
            print(estadistica.getcategory())
            print(estadistica.getstatistic())
        self.dibujarSeparador()

    def classificator_paragraph(self):
        self.estadisticasResultado=[]
        webPageInfoObject = webPageInfo(route=self.urlfich.get())
        classificatorObject = classificator(self.ficheroParaEntrenamiento,
                                            self.configuracion.getRutaFicheroEntrenamientoPersistenteParagraphData(),
                                            self.configuracion.getRutaJSONTraining(),
                                            self.ficheroParaEntrenamientoGeneradoParaEntrenamiento)
        print("Cargado Classifier Parragraph...")
        classifier = classificatorObject.getClasifier()
        print("Classifier Cargado")
        clasificator = dataClasificator(webPageInfoObject, classifier)
        # print(clasificator.classifyAllParrafos())
        # print(clasificator.accuracyAll("PARRAFO", "Armas"))
        estadisticasResultado = clasificator.accuracyAllByCategory("PARRAFO", self.configuracion.getRutaFicheroCategorias(),
                                                          URL=webPageInfoObject.getUrl())
        print("Clasificada la URL {0} ".format(webPageInfoObject.getUrl()))
        self.estadisticasResultado.append(estadisticasResultado)
        for estadistica in estadisticasResultado:
            print(estadistica.getcategory())
            print(estadistica.getstatistic())
        self.dibujarSeparador()

    def classificator_metadata(self):
        self.estadisticasResultado=[]
        webPageInfoObject = webPageInfo(route=self.urlfich.get())
        classificatorObject = classificator(self.ficheroParaEntrenamiento,
                                            self.configuracion.getRutaFicheroEntrenamientoPersistenteMetaData(),
                                            self.configuracion.getRutaJSONTraining(),
                                            self.ficheroParaEntrenamientoGeneradoParaEntrenamiento)
        print("Cargado Classifier Meta...")
        classifier = classificatorObject.getClasifier()
        print("Classifier Cargado")
        clasificator = dataClasificator(webPageInfoObject, classifier)
        # print(clasificator.classifyAllMeta())
        # print(clasificator.accuracyAll("META", "Armas"))
        estadisticasResultado = clasificator.accuracyAllByCategory("META", self.configuracion.getRutaFicheroCategorias(),
                                                          URL=webPageInfoObject.getUrl())
        print("Clasificada la URL {0} ".format(webPageInfoObject.getUrl()))
        self.estadisticasResultado.append(estadisticasResultado)
        for estadistica in estadisticasResultado:
            print(estadistica.getcategory())
            print(estadistica.getstatistic())
        self.dibujarSeparador()

    def classificator_span(self):
        self.estadisticasResultado=[]
        webPageInfoObject = webPageInfo(route=self.urlfich.get())
        classificatorObject = classificator(self.ficheroParaEntrenamiento,
                                            self.configuracion.getRutaFicheroEntrenamientoPersistenteSpanData(),
                                            self.configuracion.getRutaJSONTraining(),
                                            self.ficheroParaEntrenamientoGeneradoParaEntrenamiento)
        print("Cargado Classifier Spans...")
        classifier = classificatorObject.getClasifier()
        print("Classifier Cargado")
        clasificator = dataClasificator(webPageInfoObject, classifier)
        # allClasifyElements = clasificator.classifyAllSpan()
        # allClasifyElementsUnique = list(set(allClasifyElements)) #ESTO ELIMINA LOS ELEMENTOS DUPLICADOS EN EL ARRAY
        # print(allClasifyElements)
        # print(allClasifyElementsUnique)
        # print(clasificator.accuracyAll("SPAN", "Armas"))
        estadisticasResultado = clasificator.accuracyAllByCategory("SPAN", self.configuracion.getRutaFicheroCategorias(),
                                                          URL=webPageInfoObject.getUrl())
        print("Clasificada la URL {0} ".format(webPageInfoObject.getUrl()))
        self.estadisticasResultado.append(estadisticasResultado)
        for estadistica in estadisticasResultado:
            print(estadistica.getcategory())
            print(estadistica.getstatistic())
        self.dibujarSeparador()

    def classificator_title(self):
        self.estadisticasResultado=[]
        webPageInfoObject = webPageInfo(route=self.urlfich.get())
        classificatorObject = classificator(self.ficheroParaEntrenamiento,
                                            self.configuracion.getRutaFicheroEntrenamientoPersistenteTitle(),
                                            self.configuracion.getRutaJSONTraining(),
                                            self.ficheroParaEntrenamientoGeneradoParaEntrenamiento)
        print("Cargado Classifier Title...")
        classifier = classificatorObject.getClasifier()
        print("Classifier Cargado")
        clasificator = dataClasificator(webPageInfoObject, classifier)
        # print(clasificator.classifyAllTitles())
        # print(clasificator.accuracyAll("TITLE", "Armas"))
        estadisticasResultado = clasificator.accuracyAllByCategory("TITLE", self.configuracion.getRutaFicheroCategorias(),
                                                          URL=webPageInfoObject.getUrl())
        print("Clasificada la URL {0} ".format(webPageInfoObject.getUrl()))
        self.estadisticasResultado.append(estadisticasResultado)
        for estadistica in estadisticasResultado:
            print(estadistica.getcategory())
            print(estadistica.getstatistic())
        self.dibujarSeparador()

    #  DIRECTORIO

    def classificator_header_directory(self):
        self.estadisticasResultado=[]
        path = self.url.get()
        allObjects = leerFicherosWebPageInfo.readAllFilesInDirectory(path + "/")
        for webPageInfoObject in allObjects:
            classificatorObject = classificator(self.ficheroParaEntrenamiento,
                                                self.configuracion.getRutaFicheroEntrenamientoPersistenteHeaderData(),
                                                self.configuracion.getRutaJSONTraining(),
                                                self.ficheroParaEntrenamientoGeneradoParaEntrenamiento)
            print("Cargado Classifier Headers...")
            classifier = classificatorObject.getClasifier()
            print("Classifier Cargado")
            clasificator = dataClasificator(webPageInfoObject, classifier)
            # print(clasificator.classifyAllHeaders())
            # print(clasificator.accuracyAll("HEADER", "Armas"))
            estadisticasResultado = clasificator.accuracyAllByCategory("HEADER", self.configuracion.getRutaFicheroCategorias(),
                                                              URL=webPageInfoObject.getUrl())
            print("Clasificada la URL {0} ".format(webPageInfoObject.getUrl()))
            self.estadisticasResultado.append(estadisticasResultado)
            for estadistica in estadisticasResultado:
                print(estadistica.getcategory())
                print(estadistica.getstatistic())
        self.dibujarSeparador()

    def classificator_url_directory(self):
        self.estadisticasResultado=[]
        path = self.url.get()
        allObjects = leerFicherosWebPageInfo.readAllFilesInDirectory(path + "/")
        for webPageInfoObject in allObjects:
            classificatorObject = classificator(self.ficheroParaEntrenamiento,
                                                self.configuracion.getRutaFicheroEntrenamientoPersistenteUrlData(),
                                                self.configuracion.getRutaJSONTraining(),
                                                self.ficheroParaEntrenamientoGeneradoParaEntrenamiento)
            print("Cargado Classifier URL...")
            classifier = classificatorObject.getClasifier()
            print("Classifier Cargado")
            clasificator = dataClasificator(webPageInfoObject, classifier)
            # print(clasificator.classifyAllUrl())
            # print(clasificator.accuracyAll("URL", "Armas"))
            estadisticasResultado = clasificator.accuracyAllByCategory("URL", self.configuracion.getRutaFicheroCategorias(),
                                                              URL=webPageInfoObject.getUrl())
            print("Clasificada la URL {0} ".format(webPageInfoObject.getUrl()))
            self.estadisticasResultado.append(estadisticasResultado)
            for estadistica in estadisticasResultado:
                print(estadistica.getcategory())
                print(estadistica.getstatistic())
        self.dibujarSeparador()

    def classificator_alldata_directory(self):
        self.estadisticasResultado=[]
        path = self.url.get()
        allObjects = leerFicherosWebPageInfo.readAllFilesInDirectory(path + "/")
        for webPageInfoObject in allObjects:
            classificatorObject = classificator(self.ficheroParaEntrenamiento,
                                                self.configuracion.getRutaFicheroEntrenamientoPersistente(),
                                                self.configuracion.getRutaJSONTraining(),
                                                self.ficheroParaEntrenamientoGeneradoParaEntrenamiento)
            print("Cargado Classifier All data...")
            classifier = classificatorObject.getClasifier()
            print("Classifier Cargado")
            clasificator = dataClasificator(webPageInfoObject, classifier)
            # print(clasificator.classifyAllUrl())
            # print(clasificator.accuracyAll("URL", "Armas"))
            estadisticasResultado = clasificator.accuracyAllByCategory("All data", self.configuracion.getRutaFicheroCategorias(),
                                                              URL=webPageInfoObject.getUrl())
            print("Clasificada la URL {0} ".format(webPageInfoObject.getUrl()))
            self.estadisticasResultado.append(estadisticasResultado)
            for estadistica in estadisticasResultado:
                print(estadistica.getcategory())
                print(estadistica.getstatistic())
        self.dibujarSeparador()

    def classificator_paragraph_directory(self):
        self.estadisticasResultado=[]
        path = self.url.get()
        allObjects = leerFicherosWebPageInfo.readAllFilesInDirectory(path + "/")
        for webPageInfoObject in allObjects:
            classificatorObject = classificator(self.ficheroParaEntrenamiento,
                                                self.configuracion.getRutaFicheroEntrenamientoPersistenteParagraphData(),
                                                self.configuracion.getRutaJSONTraining(),
                                                self.ficheroParaEntrenamientoGeneradoParaEntrenamiento)
            print("Cargado Classifier Paragraph...")
            classifier = classificatorObject.getClasifier()
            print("Classifier Cargado")
            clasificator = dataClasificator(webPageInfoObject, classifier)
            # print(clasificator.classifyAllParrafos())
            # print(clasificator.accuracyAll("PARRAFO", "Armas"))
            estadisticasResultado = clasificator.accuracyAllByCategory("PARRAFO", self.configuracion.getRutaFicheroCategorias(),
                                                              URL=webPageInfoObject.getUrl())
            print("Clasificada la URL {0} ".format(webPageInfoObject.getUrl()))
            self.estadisticasResultado.append(estadisticasResultado)
            for estadistica in estadisticasResultado:
                print(estadistica.getcategory())
                print(estadistica.getstatistic())
        self.dibujarSeparador()

    def classificator_metadata_directory(self):
        self.estadisticasResultado=[]
        path = self.url.get()
        allObjects = leerFicherosWebPageInfo.readAllFilesInDirectory(path + "/")
        for webPageInfoObject in allObjects:
            classificatorObject = classificator(self.ficheroParaEntrenamiento,
                                                self.configuracion.getRutaFicheroEntrenamientoPersistenteMetaData(),
                                                self.configuracion.getRutaJSONTraining(),
                                                self.ficheroParaEntrenamientoGeneradoParaEntrenamiento)
            print("Cargado Classifier Meta...")
            classifier = classificatorObject.getClasifier()
            print("Classifier Cargado")
            clasificator = dataClasificator(webPageInfoObject, classifier)
            # print(clasificator.classifyAllMeta())
            # print(clasificator.accuracyAll("META", "Armas"))
            estadisticasResultado = clasificator.accuracyAllByCategory("META", self.configuracion.getRutaFicheroCategorias(),
                                                              URL=webPageInfoObject.getUrl())
            print("Clasificada la URL {0} ".format(webPageInfoObject.getUrl()))
            self.estadisticasResultado.append(estadisticasResultado)
            for estadistica in estadisticasResultado:
                print(estadistica.getcategory())
                print(estadistica.getstatistic())
        self.dibujarSeparador()

    def classificator_span_directory(self):
        self.estadisticasResultado=[]
        path = self.url.get()
        allObjects = leerFicherosWebPageInfo.readAllFilesInDirectory(path + "/")
        for webPageInfoObject in allObjects:
            classificatorObject = classificator(self.ficheroParaEntrenamiento,
                                                self.configuracion.getRutaFicheroEntrenamientoPersistenteSpanData(),
                                                self.configuracion.getRutaJSONTraining(),
                                                self.ficheroParaEntrenamientoGeneradoParaEntrenamiento)
            print("Cargado Classifier Spans...")
            classifier = classificatorObject.getClasifier()
            print("Classifier Cargado")
            clasificator = dataClasificator(webPageInfoObject, classifier)
            # allClasifyElements = clasificator.classifyAllSpan()
            # allClasifyElementsUnique = list(set(allClasifyElements)) #ESTO ELIMINA LOS ELEMENTOS DUPLICADOS EN EL ARRAY
            # print(allClasifyElements)
            # print(allClasifyElementsUnique)
            # print(clasificator.accuracyAll("SPAN", "Armas"))
            estadisticasResultado = clasificator.accuracyAllByCategory("SPAN", self.configuracion.getRutaFicheroCategorias(),
                                                              URL=webPageInfoObject.getUrl())
            print("Clasificada la URL {0} ".format(webPageInfoObject.getUrl()))
            self.estadisticasResultado.append(estadisticasResultado)
            for estadistica in estadisticasResultado:
                print(estadistica.getcategory())
                print(estadistica.getstatistic())
        self.dibujarSeparador()

    def classificator_title_directory(self):
        self.estadisticasResultado=[]
        path = self.url.get()
        allObjects = leerFicherosWebPageInfo.readAllFilesInDirectory(path + "/")
        for webPageInfoObject in allObjects:
            classificatorObject = classificator(self.ficheroParaEntrenamiento,
                                                self.configuracion.getRutaFicheroEntrenamientoPersistenteTitle(),
                                                self.configuracion.getRutaJSONTraining(),
                                                self.ficheroParaEntrenamientoGeneradoParaEntrenamiento)
            print("Cargado Classifier Title...")
            classifier = classificatorObject.getClasifier()
            print("Classifier Cargado")
            clasificator = dataClasificator(webPageInfoObject, classifier)
            # print(clasificator.classifyAllTitles())
            # print(clasificator.accuracyAll("TITLE", "Armas"))
            estadisticasResultado = clasificator.accuracyAllByCategory("TITLE", self.configuracion.getRutaFicheroCategorias(),
                                                              URL=webPageInfoObject.getUrl())
            print("Clasificada la URL {0} ".format(webPageInfoObject.getUrl()))
            self.estadisticasResultado.append(estadisticasResultado)
            for estadistica in estadisticasResultado:
                print(estadistica.getcategory())
                print(estadistica.getstatistic())
        self.dibujarSeparador()

    def dibujarSeparador(self):
        print("-----------------------------------\n\n")


class TextRedirector(object):
    def __init__(self, widget, tag="stdout"):
        self.widget = widget
        self.tag = tag

    def write(self, str):
        self.widget.configure(state="normal")
        self.widget.insert("end", str, (self.tag,))
        self.widget.configure(state="disabled")

    def flush(self):
        pass
