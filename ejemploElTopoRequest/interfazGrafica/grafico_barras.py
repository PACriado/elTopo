from tkinter import *
from clasificador.entities.categoryStatistic import categoryStatistic


class grafico_barras():
    def __init__(self, estadisticasCategoria):

        ventana = Tk()
        ventana.title("Grafico de barras")

        c_width = 400
        c_height = 350
        c = Canvas(ventana, width=c_width, height=c_height)


        c.pack()

        y_stretch = 30  # ANCHO Y
        y_gap = 20  # POSICION HORIZONTAL
        x_stretch = 50  # ESPACIO ENTRE VARIABLES
        x_width = 20  # ANCHO X
        x_gap = 20  # POSICION VERTICAL

        # Multiplicamos las frecuencias * 10 para que sea más visible


        datos = []
        texto = []

        for estadistica in estadisticasCategoria:
            print(estadistica.getcategory())
            print(estadistica.getstatistic())
            datos.append(estadistica.getstatistic()*10)
            texto.append(estadistica.getcategory())


        for x, y in enumerate(datos):
            x0 = x * x_stretch + x * x_width + x_gap

            y0 = c_height - (y * y_stretch + y_gap)


            x1 = x * x_stretch + x * x_width + x_width + x_gap


            y1 = c_height - y_gap

            c.create_rectangle(x0, y0, x1, y1, fill="red")
            c.create_text(x0 - 2, 340, anchor=SW, text=texto[x])

            c.create_line(0, 330, c_width, 330)

        ventana.mainloop()
