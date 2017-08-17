from tkinter import *
from tkinter import ttk
import sys
from tkinter.filedialog import askdirectory
from tkinter.filedialog import askopenfilename
from configElTopo.config import config
from clasificador.classificator import classificator
from clasificador.dataClasificator import dataClasificator
from Entidades.webPageInfo import webPageInfo


class VentanaClasificador():
    def __init__(self):
        self.ventana = Tk()
        self.ventana.title('Clasificador')
        #self.toolbar = Frame(self.ventana)
        #self.toolbar.pack(side="top", fill="x")

        self.marco = ttk.Frame(self.ventana, borderwidth=1)
        self.marco.grid(row=0,column=0)

        self.configuracion = config("./configElTopo/config.json")
        self.webPageInfoObject = webPageInfo(route='/home/usertfm/SalidaJSON/Preproc/google.es.json')
        self.ficheroParaEntrenamiento =self.configuracion.getFicheroParaEntrenamiento()
        self.ficheroParaEntrenamientoGeneradoParaEntrenamiento = self.configuracion.getFicheroParaEntrenamientoGeneradoParaEntrenamiento()


        BTN_Abrirdir = ttk.Button(self.marco, text="Abrir directorio", command=self.ruta_text)
        BTN_Header = ttk.Button(self.marco, text="Header data", command=self.classificator_header)
        BTN_Url = ttk.Button(self.marco, text="Url data", command=self.classificator_url)
        BTN_Paragraph = ttk.Button(self.marco, text="Paragraph data", command=self.classificator_paragraph)
        BTN_Metadata = ttk.Button(self.marco, text="Meta data", command=self.classificator_metadata)
        BTN_Span = ttk.Button(self.marco, text="Span data", command=self.classificator_span)
        BTN_Title = ttk.Button(self.marco, text="Title data", command=self.classificator_title)
        BTN_All = ttk.Button(self.marco, text="All data", command=self.classificator_paragraph)
        self.url = ttk.Entry(self.marco, width=80)


        BTN_Abrirfich = ttk.Button(self.marco, text="Abrir fichero", command=self.ruta_textfich)
        BTN_Headerfich = ttk.Button(self.marco, text="Header data", command=self.classificator_header)
        BTN_Urlfich = ttk.Button(self.marco, text="Url data", command=self.classificator_url)
        BTN_Paragraphfich = ttk.Button(self.marco, text="Paragraph data", command=self.classificator_paragraph)
        BTN_Metadatafich = ttk.Button(self.marco, text="Meta data", command=self.classificator_metadata)
        BTN_Spanfich = ttk.Button(self.marco, text="Span data", command=self.classificator_span)
        BTN_Titlefich = ttk.Button(self.marco, text="Title data", command=self.classificator_title)
        BTN_Allfich = ttk.Button(self.marco, text="All data", command=self.classificator_paragraph)
        self.urlfich = ttk.Entry(self.marco, width=80)


       # Fila 1 :

        BTN_Abrirdir.grid(row=0,column=0)
        self.url.grid(row=0,column=1)

        # Fila 3 :
        BTN_Header.grid(row=2,column=0)
        BTN_Paragraph.grid(row=2,column=1)
        BTN_Span.grid(row=2,column=2)
        BTN_Url.grid(row=2,column=3)


        #Fila 4 :
        BTN_Title.grid(row=3,column=0)
        BTN_All.grid(row=3,column=1)
        BTN_Metadata.grid(row=3,column=2)

        # Fila 6 :

        BTN_Abrirfich.grid(row=5,column=0)
        self.urlfich.grid(row=5,column=1)

        # Fila 8 :
        BTN_Headerfich.grid(row=7,column=0)
        BTN_Paragraphfich.grid(row=7,column=1)
        BTN_Spanfich.grid(row=7,column=2)
        BTN_Urlfich.grid(row=7,column=3)


        #Fila 10 :
        BTN_Titlefich.grid(row=9,column=0)
        BTN_Allfich.grid(row=9,column=1)
        BTN_Metadatafich.grid(row=9,column=2)

        #Fila 11:
        self.text = Text(self.marco, wrap="word")
        #self.text.pack(side="top", fill="both", expand=True)
        self.text.grid(row=10,column=1)
        self.text.tag_configure("stderr", foreground="#b22222")
        sys.stdout = TextRedirector(self.text, "stdout")


        #Fila 13
        BTN_ClasificarFich = ttk.Button(self.marco, text="Clasificar fichero", command=self.ruta_textfich)
        BTN_ClasificarDir = ttk.Button(self.marco, text="Clasificar directorio", command=self.classificator_header)
        BTN_ClasificarDir.grid(row=12,column=0)
        BTN_ClasificarFich.grid(row=12,column=1)





       # BTN_Iniciar.pack(in_=self.toolbar, side="left")
        #BTN_Abrirdir.(in_=self.toolbar, side="left")
        #self.url.pack(in_=self.toolbar, side="left")
        #BTN_Header.pack(in_=self.toolbar, side="bottom")
        #BTN_Url.pack(in_=self.toolbar, side="bottom")
        #BTN_Paragraph.pack(in_=self.toolbar, side="bottom")
        #BTN_Metadata.pack(in_=self.toolbar, side="bottom")
        #BTN_Span.pack(in_=self.toolbar, side="bottom")
        #BTN_Title.pack(in_=self.toolbar, side="bottom")
        #BTN_All.pack(in_=self.toolbar, side="bottom")





    def print_stdout(self):
        # configuracion = config("./configElTopo/config.json")
        # ficheroParaEntrenamiento = self.configuracion.getFicheroParaEntrenamiento()
        # ficheroParaEntrenamientoGeneradoParaEntrenamiento = self.configuracion.getFicheroParaEntrenamientoGeneradoParaEntrenamiento()
        # casificatorObject = classificator(ficheroParaEntrenamiento, self.configuracion.getRutaFicheroEntrenamientoPersistente(), self.configuracion.getRutaSalidaPreProcesador(), ficheroParaEntrenamientoGeneradoParaEntrenamiento)

        print("AQUI SI QUE ENTRA")

        # print(classifier.classify("tumadre"))

    def ruta_text(self):
        result = askdirectory()
        self.url.delete(0, 'end')
        self.url.insert(0, result)
        #self.url.pack(in_=self.marco, side="left")
        self.url.grid(row=0,column=1)

    def ruta_textfich(self):
        result = askopenfilename()
        self.urlfich.delete(0, 'end')
        self.urlfich.insert(0, result)
        #self.url.pack(in_=self.marco, side="left")
        self.urlfich.grid(row=5,column=1)


    def classificator_header(self):


        classificatorObject = classificator(self.ficheroParaEntrenamiento,
                                            self.configuracion.getRutaFicheroEntrenamientoPersistenteHeaderData(),
                                            self.configuracion.getRutaJSONTraining(),
                                            self.ficheroParaEntrenamientoGeneradoParaEntrenamiento)
        classifier = classificatorObject.getClasifier()
        miClass = dataClasificator(self.webPageInfoObject,classifier)

        print(miClass.classifyAllHeaders())


    def classificator_url(self):

        classificatorObject = classificator(self.ficheroParaEntrenamiento,
                                            self.configuracion.getRutaFicheroEntrenamientoPersistenteUrlData(),
                                            self.configuracion.getRutaJSONTraining(),
                                            self.ficheroParaEntrenamientoGeneradoParaEntrenamiento)
        classifier = classificatorObject.getClasifier()
        miClass = dataClasificator(self.webPageInfoObject, classifier)

        print(miClass.classifyAllUrl())



    def classificator_paragraph(self):

        classificatorObject = classificator(self.ficheroParaEntrenamiento,
                                            self.configuracion.getRutaFicheroEntrenamientoPersistenteParagraphData(),
                                            self.configuracion.getRutaJSONTraining(),
                                            self.ficheroParaEntrenamientoGeneradoParaEntrenamiento)
        classifier = classificatorObject.getClasifier()
        miClass = dataClasificator(self.webPageInfoObject, classifier)

        print(miClass.classifyAllParrafos())



    def classificator_metadata(self):


        classificatorObject = classificator(self.ficheroParaEntrenamiento,
                                            self.configuracion.getRutaFicheroEntrenamientoPersistenteMetaData(),
                                            self.configuracion.getRutaJSONTraining(),
                                            self.ficheroParaEntrenamientoGeneradoParaEntrenamiento)
        classifier = classificatorObject.getClasifier()
        miClass = dataClasificator(self.webPageInfoObject, classifier)
        print(miClass.classifyAllMeta())


    def classificator_span(self):

        classificatorObject = classificator(self.ficheroParaEntrenamiento,
                                            self.configuracion.getRutaFicheroEntrenamientoPersistenteSpanData(),
                                            self.configuracion.getRutaJSONTraining(),
                                            self.ficheroParaEntrenamientoGeneradoParaEntrenamiento)

        classifier = classificatorObject.getClasifier()

        miClass = dataClasificator(self.webPageInfoObject, classifier)
        print(miClass.classifyAllSpan())



    def classificator_title(self):


        classificatorObject = classificator(self.ficheroParaEntrenamiento,
                                            self.configuracion.getRutaFicheroEntrenamientoPersistenteTitle(),
                                            self.configuracion.getRutaJSONTraining(),
                                            self.ficheroParaEntrenamientoGeneradoParaEntrenamiento)
        classifier = classificatorObject.getClasifier()
        miClass = dataClasificator(self.webPageInfoObject, classifier)
        print(miClass.classifyAllTitles())

class TextRedirector(object):

    def __init__(self, widget, tag="stdout"):
        self.widget = widget
        self.tag = tag

    def write(self, str):
        self.widget.configure(state="normal")
        self.widget.insert("end", str, (self.tag,))
        self.widget.configure(state="disabled")
