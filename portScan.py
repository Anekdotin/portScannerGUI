__author__ = "ed"

import tkinter.ttk, socket
from tkinter import messagebox, Label, Spinbox, Tk, Entry, E, W, END, WORD, Button, Text

class PortScanner:
    def __init__(self):
            mGUI = Tk() #create tk reference object AKA Make A Window/Frame
            self.srvr = Entry(mGUI,textvariable="server")
            self.srvr.setvar(name="server",value='127.0.0.1')
            self.srvr.grid(row=0,column=1,sticky=W)
            lbl = Label(mGUI,text="Target Address:")
            lbl.grid(row=0,column=0,sticky=W)
            self.spnr = Spinbox(mGUI,from_=1,to=49152,value=1)
            self.spnr.grid(row=1,column=1,sticky=W)
            lbl2 = Label(mGUI,text="Starting Port:")
            lbl2.grid(row=1,column=0,sticky=W)
            self.spnr.grid(row=1,column=1,sticky=W)
            self.spnr2 = Spinbox(mGUI,from_=1,to=49152,value=49152)
            self.spnr2.grid(row=2,column=1,sticky=W)
            lbl3 = Label(mGUI,text="Ending Port")
            lbl3.grid(row=2,column=0,sticky=W)
            mGUI.resizable(width=False,height=False) #Make Window Size Static (Not Resizeable)
            btn = Button(mGUI,text="Commence Port Scan!",command=self.scan)
            btn.grid(row=3,column=1,sticky=W)
            self.txt = Text(mGUI,width=50,height=20,wrap=WORD)
            self.txt.grid(row=4,column=0,columnspan=2,sticky=W)
            mGUI.title('PyPortScanner!') #set Title Of Window
            self.txt.insert(0.0,'Open Ports Will Appear Here After Scan Completes!')

            mGUI.mainloop() #Show GUI Window



ps = PortScanner()