from spyder.spyder import spyder
from flask import Flask
from EntidadesRest.SpyderRequest import SpyderRequest
from EntidadesRest.SpyderResponse import SpyderResponse


app = Flask(__name__)

@app.route("/lanzar")
def lanzar():
    theSpyder = spyder("../configElTopo/config.json")
    rutaFicheros = theSpyder.launch()
    spyderResponse = SpyderResponse(FilesPath=rutaFicheros)
    return spyderResponse.toJSON()

if __name__ == "__main__":
    app.run()
