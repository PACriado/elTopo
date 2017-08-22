from tkinter import *
from tkinter import ttk
import os

class VentanaTerminal():
    def __init__(self):
        self.ventanaT = Tk()
        self.ventanaT.geometry('600x600')
        self.ventanaT.title('Terminal')
        self.ventanaT.resizable(0,0)

        #Inserción terminal
        termf = Frame(self.ventanaT,height = 400, width=500)
        termf.pack(fill=BOTH,expand = YES)
        wid = termf.winfo_id()
        os.system('xterm -into %d -geometry 200x200 -sb &' % wid)

