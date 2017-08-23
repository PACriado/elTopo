from tkinter import *


class grafico_barras():
    def __init__(self, estadisticasCategoria):

        ventana = Tk()
        ventana.resizable(0, 0)
        ventana.title("Grafico de barras " + estadisticasCategoria[0].geturl())

        c_width = 450
        c_height = 380
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
            datos.append(estadistica.getstatistic() * 10)
            texto.append(estadistica.getcategory() + "\n" + str(round(estadistica.getstatistic() * 100, 2)) + "%")

        for x, y in enumerate(datos):
            x0 = x * x_stretch + x * x_width + x_gap

            y0 = c_height - (y * y_stretch + y_gap)

            x1 = x * x_stretch + x * x_width + x_width + x_gap

            y1 = c_height - y_gap

            c.create_rectangle(x0, y0, x1, y1, fill="red")
            c.create_text(x0 - 2, 380, anchor=SW, text=texto[x])

            c.create_line(0, 360, c_width, 360)

            # print(x0)
            # print(y0)
            # print(x1)
            # print(y1)

            # ventana.mainloop()
