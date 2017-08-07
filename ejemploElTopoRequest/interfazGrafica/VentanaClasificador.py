from tkinter import *
import sys
from tkinter.filedialog import askdirectory
from configElTopo.config import config
from clasificador.classificator import classificator


class VentanaClasificador():

    def __init__(self):

        self.ventana = Tk()
        self.ventana.title('Clasificador')
        self.toolbar = Frame(self.ventana)
        self.toolbar.pack(side="top", fill="x")

        self.configuracion = config("./configElTopo/config.json")
        self.ficheroParaEntrenamiento = self.configuracion.getFicheroParaEntrenamiento()
        self.ficheroParaEntrenamientoGeneradoParaEntrenamiento = self.configuracion.getFicheroParaEntrenamientoGeneradoParaEntrenamiento()
        self.classificatorObject = classificator(self.ficheroParaEntrenamiento,
                                                 self.configuracion.getRutaFicheroEntrenamientoPersistente(),
                                                 self.configuracion.getRutaSalidaPreProcesador(),
                                                 self.ficheroParaEntrenamientoGeneradoParaEntrenamiento)


        BTN_Iniciar = Button(self.ventana, text="Iniciar", command=self.print_stdout)
        BTN_Abrirdir = Button(self.ventana, text="Abrir directorio",command=self.ruta_text)
        BTN_Header = Button(self.ventana, text="Header data", command=self.generate_header)
        BTN_Url = Button(self.ventana, text="Url data", command=self.generate_url)
        BTN_Paragraph = Button(self.ventana, text="Paragraph data", command=self.generate_paragraph)
        BTN_Metadata = Button(self.ventana, text="Meta data", command=self.generate_metadata)
        BTN_Span = Button(self.ventana, text="Span data", command=self.generate_span)
        BTN_Title = Button(self.ventana, text="Title data", command=self.generate_title)
        BTN_All = Button(self.ventana, text="All data", command=self.generate_paragraph)
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
        classifier = self.classificatorObject.getClasifier()
        print(classifier.classify("tumadre"))

    def ruta_text(self):

        result = askdirectory()
        self.url.delete(0,'end')
        self.url.insert(0,result)
        self.url.pack(in_=self.toolbar,side = "left")

    def generate_header(self):
        self.classificatorObject.generateJsonHeaderData()

    def generate_url(self):
        self.classificatorObject.generateJsonUrlData()

    def generate_paragraph(self):
        self.classificatorObject.generateJsonParagraphData()

    def generate_metadata(self):
        self.classificatorObject.generateJsonMetaData()

    def generate_span(self):
        self.classificatorObject.generateJsonSpanData()

    def generate_title(self):
        self.classificatorObject.generateJsonTitleData()



class TextRedirector(object):
    def __init__(self, widget, tag="stdout"):
        self.widget = widget
        self.tag = tag
    def write(self, str):
        self.widget.configure(state="normal")
        self.widget.insert("end", str, (self.tag,))
        self.widget.configure(state="disabled")
