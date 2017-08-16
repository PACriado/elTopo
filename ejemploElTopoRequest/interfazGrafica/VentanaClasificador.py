from tkinter import *
import sys
from tkinter.filedialog import askdirectory
from configElTopo.config import config
from clasificador.classificator import classificator
from clasificador.dataClasificator import dataClasificator
from Entidades.webPageInfo import webPageInfo


class VentanaClasificador():

    def __init__(self):

        self.ventana = Tk()
        self.ventana.title('Clasificador')
        self.toolbar = Frame(self.ventana)
        self.toolbar.pack(side="top", fill="x")

        self.configuracion = config("./configElTopo/config.json")


        self.ficheroParaEntrenamiento = self.configuracion.getFicheroParaEntrenamiento()


        self.ficheroParaEntrenamientoGeneradoParaEntrenamiento = self.configuracion.getFicheroParaEntrenamientoGeneradoParaEntrenamiento()
        self.classificatorObject = classificator(self.ficheroParaEntrenamiento, self.configuracion.getRutaFicheroEntrenamientoPersistente(), self.configuracion.getRutaJSONTraining(), self.ficheroParaEntrenamientoGeneradoParaEntrenamiento)

        self.classificatorObject = classificator(self.ficheroParaEntrenamiento,
                                                 self.configuracion.getRutaFicheroEntrenamientoPersistente(),
                                                 self.configuracion.getRutaSalidaPreProcesador(),
                                                 self.ficheroParaEntrenamientoGeneradoParaEntrenamiento)

        self.classifier = self.classificatorObject.getClasifier()
        self.webPageInfoObject = webPageInfo(route= '/home/usertfm/SalidaJSON/Preproc/google.es.json')
        self.miClass = dataClasificator(self.webPageInfoObject,self.classifier)


        BTN_Iniciar = Button(self.ventana, text="Iniciar", command=self.print_stdout)
        BTN_Abrirdir = Button(self.ventana, text="Abrir directorio",command=self.ruta_text)
        BTN_Header = Button(self.ventana, text="Header data", command=self.classificator_header)
        BTN_Url = Button(self.ventana, text="Url data", command=self.classificator_url)
        BTN_Paragraph = Button(self.ventana, text="Paragraph data", command=self.classificator_paragraph)
        BTN_Metadata = Button(self.ventana, text="Meta data", command=self.classificator_metadata)
        BTN_Span = Button(self.ventana, text="Span data", command=self.classificator_span)
        BTN_Title = Button(self.ventana, text="Title data", command=self.classificator_title)
        BTN_All = Button(self.ventana, text="All data", command=self.classificator_paragraph)
        self.url = Entry(self.ventana,width = 80)

        BTN_Iniciar.pack(in_=self.toolbar, side="left")
        BTN_Abrirdir.pack(in_=self.toolbar, side="left")
        self.url.pack(in_=self.toolbar,side = "left")
        BTN_Header.pack(in_=self.toolbar, side="bottom")
        BTN_Url.pack(in_=self.toolbar, side="bottom")
        BTN_Paragraph.pack(in_=self.toolbar, side="bottom")
        BTN_Metadata.pack(in_=self.toolbar, side="bottom")
        BTN_Span.pack(in_=self.toolbar, side="bottom")
        BTN_Title.pack(in_=self.toolbar, side="bottom")
        BTN_All.pack(in_=self.toolbar, side="bottom")
        self.text = Text(self.ventana, wrap="word")
        self.text.pack(side="top", fill="both", expand=True)
        self.text.tag_configure("stderr", foreground="#b22222")
        sys.stdout = TextRedirector(self.text, "stdout")

    def print_stdout(self):
        #configuracion = config("./configElTopo/config.json")
        #ficheroParaEntrenamiento = self.configuracion.getFicheroParaEntrenamiento()
        #ficheroParaEntrenamientoGeneradoParaEntrenamiento = self.configuracion.getFicheroParaEntrenamientoGeneradoParaEntrenamiento()
        #casificatorObject = classificator(ficheroParaEntrenamiento, self.configuracion.getRutaFicheroEntrenamientoPersistente(), self.configuracion.getRutaSalidaPreProcesador(), ficheroParaEntrenamientoGeneradoParaEntrenamiento)
        print(self.miClass.classifyTitle())
        print("AQUI SI QUE ENTRA")

        #print(classifier.classify("tumadre"))

    def ruta_text(self):
        result = askdirectory()
        self.url.delete(0,'end')
        self.url.insert(0,result)
        self.url.pack(in_=self.toolbar,side = "left")

    def classificator_header(self):
        print(self.miClass.classifyAllHeaders())

    def classificator_url(self):
        print(self.miClass.classifyAllUrl())

    def classificator_paragraph(self):
        print(self.miClass.classifyAllParrafos())

    def classificator_metadata(self):
        print(self.miClass.classifyAllMeta())

    def classificator_span(self):
        print(self.miClass.classifyAllSpan())

    def classificator_title(self):
        print(self.miClass.classifyAllTitles())


class TextRedirector(object):
    def __init__(self, widget, tag="stdout"):
        self.widget = widget
        self.tag = tag
    def write(self, str):
        self.widget.configure(state="normal")
        self.widget.insert("end", str, (self.tag,))
        self.widget.configure(state="disabled")
