from tkinter import *
import sys
from tkinter.filedialog import askdirectory
from configElTopo.config import config
from clasificador.classificator import classificator


class VentanaEntrenamiento():
    def __init__(self):
        self.ventanaE = Tk()
        self.ventanaE.title('Entrenamiento')
        self.toolbar = Frame(self.ventanaE)
        self.toolbar.pack(side="top", fill="x")
        self.configuracion = config("./configElTopo/config.json")
        self.ficheroParaEntrenamiento = self.configuracion.getFicheroParaEntrenamiento()
        self.ficheroParaEntrenamientoGeneradoParaEntrenamiento = self.configuracion.getFicheroParaEntrenamientoGeneradoParaEntrenamiento()
        self.classificatorObject = classificator(self.ficheroParaEntrenamiento,
                                                 self.configuracion.getRutaFicheroEntrenamientoPersistente(),
                                                 self.configuracion.getRutaSalidaPreProcesador(),
                                                 self.ficheroParaEntrenamientoGeneradoParaEntrenamiento)

        BTN_Entrenar = Button(self.ventanaE, text="Entrenar", command=self.print_stdout)

        BTN_Entrenar.pack(in_=self.toolbar, side="left")

        self.text = Text(self.ventanaE, wrap="word")
        self.text.pack(side="top", fill="both", expand=True)
        self.text.tag_configure("stderr", foreground="#b22222")
        sys.stdout = TextRedirector(self.text, "stdout")

    def print_stdout(self):
        # configuracion = config("./configElTopo/config.json")
        ficheroParaEntrenamiento = self.configuracion.getFicheroParaEntrenamiento()
        ficheroParaEntrenamientoGeneradoParaEntrenamiento = self.configuracion.getFicheroParaEntrenamientoGeneradoParaEntrenamiento()
        # casificatorObject = classificator(ficheroParaEntrenamiento, self.configuracion.getRutaFicheroEntrenamientoPersistente(), self.configuracion.getRutaSalidaPreProcesador(), ficheroParaEntrenamientoGeneradoParaEntrenamiento)
        # casificatorObject.training()

        # Entrenamos con todas las posibilidades y generamos cada uno de los ficheros de entrenamiento persistente
        classificatorObject = classificator(ficheroParaEntrenamiento,
                                            self.configuracion.getRutaFicheroEntrenamientoPersistenteHeaderData(),
                                            self.configuracion.getRutaJSONTraining(),
                                            ficheroParaEntrenamientoGeneradoParaEntrenamiento)
        classificatorObject.generateJsonHeaderData()
        classificatorObject.training()
        classificatorObject = classificator(ficheroParaEntrenamiento,
                                            self.configuracion.getRutaFicheroEntrenamientoPersistenteUrlData(),
                                            self.configuracion.getRutaJSONTraining(),
                                            ficheroParaEntrenamientoGeneradoParaEntrenamiento)
        classificatorObject.generateJsonUrlData()
        classificatorObject.training()
        classificatorObject = classificator(ficheroParaEntrenamiento,
                                            self.configuracion.getRutaFicheroEntrenamientoPersistenteMetaData(),
                                            self.configuracion.getRutaJSONTraining(),
                                            ficheroParaEntrenamientoGeneradoParaEntrenamiento)
        classificatorObject.generateJsonMetaData()
        classificatorObject.training()
        classificatorObject = classificator(ficheroParaEntrenamiento,
                                            self.configuracion.getRutaFicheroEntrenamientoPersistenteSpanData(),
                                            self.configuracion.getRutaJSONTraining(),
                                            ficheroParaEntrenamientoGeneradoParaEntrenamiento)
        classificatorObject.generateJsonSpanData()
        classificatorObject.training()
        classificatorObject = classificator(ficheroParaEntrenamiento,
                                            self.configuracion.getRutaFicheroEntrenamientoPersistenteTitle(),
                                            self.configuracion.getRutaJSONTraining(),
                                            ficheroParaEntrenamientoGeneradoParaEntrenamiento)
        classificatorObject.generateJsonTitleData()
        classificatorObject.training()




def ruta_text(self):
    result = askdirectory()
    self.url.delete(0, 'end')
    self.url.insert(0, result)
    self.url.pack(in_=self.toolbar, side="left")


class TextRedirector(object):
    def __init__(self, widget, tag="stdout"):
        self.widget = widget
        self.tag = tag

    def write(self, str):
        self.widget.configure(state="normal")
        self.widget.insert("end", str, (self.tag,))
        self.widget.configure(state="disabled")
