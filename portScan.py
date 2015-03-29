__author__ = "T31337"
#modified by Edwin

import tkinter.ttk, socket
import tkinter as tk
from tkinter import messagebox, Label, Spinbox, Tk, Entry, E, W, END, WORD, Button, Text


LARGE_FONT = ("Verdana", 12)

class PortScanner(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}


        for F in (StartPage, PageOne, PageTwo):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")


        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()



class StartPage(tk.Frame):


    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        mGUI = Tk.Frame(self) #create tk reference object AKA Make A Window/Frame


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
        #mGUI.resizable(width=False,height=False) #Make Window Size Static (Not Resizeable)
        btn = Button(mGUI,text="Commence Port Scan!",command=self.scan)
        btn.grid(row=3,column=1,sticky=W)
        self.txt = Text(mGUI,width=50,height=20,wrap=WORD)
        self.txt.grid(row=4,column=0,columnspan=2,sticky=W)
        mGUI.title('PyPortScanner!') #set Title Of Window
        self.txt.insert(0.0,'Open Ports Will Appear Here After Scan Completes!')

        mGUI.mainloop() #Show GUI Window

    def pscan(self,port):
            try:
                target = self.srvr.get()
                s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                s.connect((target,port))
                return True
            except:
                return False

    def scan(self):
        self.txt.delete(0.0, END)
        print('Scanning', self.srvr.get())
        for x in range(int(self.spnr.get()), int(self.spnr2.get())+1):
            if self.pscan(x):
                print('Port: ',x,'Is Open!')
                msg = "Port "+str(x)+" Is Open!\n"
                self.txt.insert(0.0,msg)
            else:
                print('port: ',x,'Is Closed!')



        messagebox.showinfo(title="PyPortScanner!", message="Scan Completed!")

class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page One", font="LARGE_FONT")
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()
        button3 = tk.Button(self, text="Page two",
                            command=lambda: controller.show_frame(PageTwo))
        button3.pack()

class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page Two", font="LARGE_FONT")
        label.pack(pady=10, padx=10)


        button2 = tk.Button(self, text="Page One",
                            command=lambda: controller.show_frame(PageOne))
        button2.pack()

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()


ps = PortScanner()
ps.mainloop()