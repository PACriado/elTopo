
import subprocess as sub
from tkinter import *
from tkinter import ttk



p = sub.Popen(["free","-m"],stdout=sub.PIPE,stderr=sub.PIPE)
output, errors = p.communicate()

root = Tk()
text = Text(root)
text.pack()
text.insert(END, output)
root.mainloop()
