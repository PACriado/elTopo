from tkinter import *
from tkinter import ttk
import os

class VentanaCrawler():
    def __init__(self):
        self.ventanaC = Tk()
        self.ventanaC.geometry('600x600')
        self.ventanaC.title('Crawler')

        #Inserción terminal
        termf = Frame(self.ventanaC,height = 400, width=500)
        termf.pack(fill=BOTH,expand = YES)
        wid = termf.winfo_id()
        os.system('xterm -into %d -geometry 200x200 -sb &' % wid)
        self.ventanaC.mainloop()

