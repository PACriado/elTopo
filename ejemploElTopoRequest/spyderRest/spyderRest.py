from spyder.spyder import spyder
from flask import Flask
from flask import request
from EntidadesRest.SpyderRequest import SpyderRequest
from EntidadesRest.SpyderResponse import SpyderResponse


app = Flask(__name__)


@app.route("/lanzar", methods=['GET', 'POST'])
def lanzar():
    dataReq = request.data.decode('UTF-8')
    spyderRequest = SpyderRequest(jsonRequest=dataReq)

    theSpyder = spyder("./configElTopo/config.json")
    rutaFicheros = theSpyder.launch()
    spyderResponse = SpyderResponse(FilesPath=rutaFicheros)
    return spyderResponse.toJSON()

if __name__ == "__main__":
    print("spyderRest.py is being run directly")
    app.run()


def start(serverPort=5000):
    app.run(port=serverPort)
