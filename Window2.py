import tkinter as tk
from tkinter import ttk

from tkinter import *
from tkinter.filedialog import *
import os 
from Utils import *
from cleanTrame import *

resultatAnalyseTrame="./outPuts.txt"
ANALYSE=None


class Window:
    def __init__(self, master):
        self.master = master
        self.analyse=None
        self.master.geometry("950x600")
        self.master.resizable(height=False , width = False)
        self.master.title("WirePoulpe")
        self.master.config(bg = '#F0F0E6')

        # Créer l'image de fond sur notre fenetre
        self.image = tk.PhotoImage(file = "./DALL·E 2022-12-02 13.12.31 - monster octopus.png")
        self.limg = Label(self.master, i = self.image)
        self.limg.place(x = 0, y = 0, relwidth = 1, relheight = 1)

        self.showWidgets()

    def showWidgets(self):
        # Titre page principale 
        self.title = Label(self.master, text = "Bienvenue sur WirePoulpe", font = ('Courier', 20), width = 50, height = 5, bg = '#2C514C', fg = 'black')
        self.title.pack(pady = 50)

        self.frame = tk.Frame(self.master)
        self.frame.pack()

        
        b=self.createButton(self.master,"Import",10,2, lambda: self.openFile())
        b.place(x = 0, y = 0, relwidth = 1, relheight = 1)
        self.explorer = b

        self.explorer.pack()

        b = self.createButton(self.master,"Quit",10,2, lambda : self.closeWindow())
        b.place(x = 0, y = 0, relwidth = 1, relheight = 1)
        self.quit=b
        self.quit.pack()



    def createButton(self,where, text,width,height, command):
        butt = tk.Button(where, text = text, font = ('Courier', 15), width = width, height = height, bg = '#2C514C', command = command)
        return butt

    # Ouvrir un fichier
    def openFile(self):
        self.file = askopenfilename(initialdir= os.getcwd(), title = "Selectionner un fichier .txt", filetypes=(("text files", "*.txt"), ("all files", "*.*")))
        #self.file = tk.filedialog.askopenfilename(initialdir = "~/", title = "Select a file", filetypes = [("Text files", "*.txt*")])
        global ANALYSE
        ANALYSE= getTrace(self.file,resultatAnalyseTrame)
        if ANALYSE !=None:
            print(len(ANALYSE.listeDeTrames))
        #update_leftFrame(analyse)
        self.newWindow(Win2)
        
        #print("heh{}".format(self.analyse))
        

    def newWindow(self, _class):
        global win2
        try:
            if _class == Win2:
                if win2.state() == "normal":
                    win2.focus()
        except:
            win2 = tk.Toplevel(self.master, bg = '#F0F0E6')
            _class(win2)

    def closeWindow(self):
        self.master.destroy()
    def getAnalyse(self):
        return self.analyse

class Win2(Window):
    def __init__(self, master):
        super().__init__(master)
        self.master.title("Visualisateur du uuuuuuuuuuuuuuuutrafic réseau")
    
    def showWidgets(self):
        #self.topframe = tk.Frame(self.master)
        #self.topframe.pack(side=TOP,pady=10)
        """"
        self.frame1=tk.Frame(self.master,bg="red")
        self.frame1.pack(fill=tk.BOTH,expand=True,side=RIGHT)
        self.frame2=tk.Frame(self.master,background="green")
        self.frame2.pack(fill=tk.BOTH,expand=True,side=RIGHT)
        
    
        self.mainFrame=tk.Frame(self.master,bg='red')
        self.mainFrame.pack(fill=tk.BOTH,expand=True)
        self.bottomFrame=tk.Frame(self.master)
        # Barre de saisie pour filtre
        self.ma_var=StringVar()
        self.user_Entry = Entry(self.bottomFrame, bg = "white",textvariable=self.ma_var)
        self.user_Entry.pack(side=tk.LEFT,padx=10)

        #self.user = Label(self.topframe, text ="here")
        #self.user.pack()

        self.butt=self.createButton(self.bottomFrame,"Valider",10,2, lambda : self.filtreCommande())
        #self.butt = Button(self.topframe, text = "Valider", bg = '#5500ff', fg = "black",command= self.filtreCommande())
        self.butt.pack(side=tk.RIGHT, padx=10)

        self.bottomFrame.pack(side=tk.BOTTOM,pady=10)
        
        """
        self.graheFrame = tk.Frame(self.master, width=700 , height=550,bg="green")
        self.filtreBarre = tk.Frame(self.master, bd=1, bg="blue", relief=SUNKEN)
        self.graheFrame.place(x = 5, y = 55 , width=675 , height=525)
        self.filtreBarre.place(height=50, width=950)


        self.ma_var=StringVar()
        self.user_Entry = Entry(self.filtreBarre, bg = "white",textvariable=self.ma_var,width=50,background="white")
        self.user_Entry.grid(row=0,column=0,padx=10)
        self.user_Entry.insert(0,"--protocol= --adr1= --adr2=")

        self.user = Label(self.filtreBarre, text ="Respectez bien le hhhhhhhhhhhhhhhhhhhhhhformat")
        self.user.grid(row=0,column=1,padx=10)

        self.butt=self.createButton(self.filtreBarre,"Valider",10,2, lambda : self.filtreCommande())
        self.butt.grid(row=0,column=2,padx=10)
       
        #Pour afficher les commentaires:
        self.scrollbarx =Scrollbar(self.master, orient=HORIZONTAL)
        self.scrollbary =Scrollbar(self.master, orient=VERTICAL)

        self.commentsBox = Listbox(self.master, xscrollcommand=self.scrollbarx.set,yscrollcommand=self.scrollbary.set)

        self.scrollbarx.config(command=self.commentsBox.xview)
        self.scrollbary.config(command=self.commentsBox.yview)

        self.scrollbarx.place(x = 685, y = 580, height=15,  width=250)
        self.scrollbary.place(x = 935, y = 55,  height=525, width=15)

        self.commentsBox.place(x = 685 , y = 55, width=250 , height=525)

        
       #Pour la partie Graphe
        grapheCanvas = Canvas(self.graheFrame , width=700 , height=550 )
        grapheCanvas.place(x =0, y = 0, width=675 , height=525)
        ScrollbarX = ttk.Scrollbar(self.graheFrame, orient=HORIZONTAL , command = grapheCanvas.xview)
        ScrollbarX.pack(side = BOTTOM , fill = "x")
     
        ScrollbarY = ttk.Scrollbar(self.graheFrame, orient=VERTICAL , command = grapheCanvas.yview)
        ScrollbarY.pack(side = RIGHT , fill = "y")

        grapheCanvas.configure(xscrollcommand=ScrollbarX.set)
        grapheCanvas.configure(yscrollcommand=ScrollbarY.set)
        
        grapFrame = Frame(grapheCanvas)
        global ANALYSE
        if (ANALYSE!=None):
            trames=ANALYSE.listeTrameTCPetHTTP()
            adressIps=adIPDistinctes(trames)
            print(adressIps)
            if len(adressIps)!=0:
                cpt=0
                l=50
                L=30
                c=490
                C=250
                adip=100
                for ip in adressIps :
                    X=C+cpt*c-20
                    Y=L-10
                    lb=Label(grapFrame, text =ip,bg="green" ,padx=200).grid(row=0,column=cpt)
                    grapheCanvas.create_line(C+cpt*c,L,C+cpt*c,L+len(trames)*l, dash = (3, 2))
                    cpt+=1

                for i in range(2):
                    self.commentsBox.insert(END,"\n")
                self.commentsBox.insert(END,"\n")
                for i in range (len(trames)):
                    self.commentsBox.insert(END, "NUMBEEEEEEEEEEEEEEEEEEEEEEEEEEEEER:")
                    for j in range(3):
                        self.commentsBox.insert(END,"\n")
                    trame = trames[i]
                    ipsource =adressIps.index(formatIPAdress(trame.ipv4.sourceAdress))
                    ipdest = adressIps.index(formatIPAdress(trame.ipv4.destinationAdress))
                    psrc = int("0x"+trame.tcp.srcPort, 16)
                    pdest =int("0x"+trame.tcp.dstPort, 16)

                    if ipsource>ipdest:
                        print("here")
                        grapheCanvas.create_line(C+ipsource*c, L+30 + i*l , C+ipdest*c, L+30 + i*l, fill="green",arrow="first")
                        grapheCanvas.create_text(C+ipsource*c+20,L+30+i*l, text =psrc)
                        grapheCanvas.create_text( C+ipdest*c-20,L+30+i*l, text =pdest)
                        grapheCanvas.create_text( C+ipdest*c+250,L+30+i*l-20, text =trame.getMsgGraphe())


                    else:
                        grapheCanvas.create_line(C+ipsource*c, L+30 + i*l , C+ipdest*c  , L+30+ i*l, fill="green",arrow="last")
                        grapheCanvas.create_text(C+ipsource*c-20,L+30+i*l, text =psrc)
                        grapheCanvas.create_text( C+ipdest*c+20,L+30+i*l, text =pdest)
                        grapheCanvas.create_text( C+ipsource*c+250,L+30+i*l-20, text =trame.getMsgGraphe())

                    

                grapFrame.update()
                grapheCanvas.create_window((5,5) ,window=grapFrame, anchor = NW)
                grapheCanvas.configure(scrollregion=grapFrame.bbox(ALL))
                

    
       
       
    """

        v_s=Scrollbar(self.f1)
        v_s.pack(side=RIGHT,fill=Y)

        h_s=Scrollbar(self.f1,orient='horizontal')
        h_s.pack(side=BOTTOM,fill=X)

        commentsBox = tk.Listbox(self.f1, xscrollcommand=h_s.set,yscrollcommand=v_s)

        h_s.config(command=listbox.xview)
        h_s.config(command=listbox.xview)

        h_s.place(x = 800, y = 560,  width=200)
       
        listbox.place(x = 800 , y = 0, width=200 , height=560)


        #for thing in range(200):
            tk.Button(self.f1,text="nchallah").pack()

        
        my_canvas=Canvas(self.f1)
        my_canvas.pack(side=LEFT,fill=BOTH,expand=1)

        my_scrollBar=ttk.Scrollbar(self.f1,orient=VERTICAL,command=my_canvas.yview)
        my_scrollBar.pack(side=RIGHT,fill=Y)

        my_canvas.configure(yscrollcommand=my_scrollBar)
        my_canvas.bind('<Configure>',lambda e:my_canvas.configure(scrollregion= my_canvas.bbox("all" )))
        self.f12=tk.Frame(my_canvas,bg="red")
        #my_canvas.create_window((0,0),window=self.f12,anchor="nw")

        my_canvas2=Canvas(self.f12)
        my_canvas2.pack(side=BOTTOM,fill=BOTH,expand=1)

        my_scrollBar2=ttk.Scrollbar(self.f1,orient=HORIZONTAL,command=my_canvas2.xview)
        my_scrollBar2.pack(side=BOTTOM,fill=X)

        my_canvas2.configure(xscrollcommand=my_scrollBar2)
        my_canvas2.bind('<Configure>',lambda e:my_canvas2.configure(scrollregion = my_canvas2.bbox("all" )))
        self.f123=tk.Frame(my_canvas2,bg="blue")
        my_canvas2.create_window((0,0),window=self.f123,anchor="sw")
        
        canvas = Canvas(self.f1, bg = "white",scrollregion = (0,0,20,1000))
        vbar = Scrollbar(self.f1, orient = VERTICAL)
        vbar.pack(side = RIGHT, fill = Y)
        vbar.config(command = canvas.yview)
        canvas.config(width = 900, height = 600)
        canvas.config(yscrollcommand = vbar.set)
        canvas.pack(side = LEFT, expand = True, fill = BOTH)
        canvas.bind('<Configure>',lambda e:canvas.configure(scrollregion = canvas.bbox("all" )))

        print(canvas.bbox('all'))
        for thing in range(200):
            tk.Button(self.f1,text="nchallah").pack()

        
            
        #scrollbar  
    
        canvas=tk.Canvas(self.f1,bg="green",scrollregion=(100,100,1000,1000))
        canvas.grid(row=0,column=0)
        y_scroll=tk.Scrollbar(self.f1,orient='vertical',command=canvas.yview)
        y_scroll.grid(row=0,column=1,sticky='ns')
        x_scroll=tk.Scrollbar(self.f1,orient='horizontal',command=canvas.xview)
        x_scroll.grid(row=1,column=0,sticky='ew') 
        print(canvas.bbox('all'))
        canvas.config(xscrollcommand=x_scroll.set,yscrollcommand=y_scroll)  
        canvas.config(scrollregion=canvas.bbox('all'))    
        
        canvas = Canvas(self.f1, bg = "white",scrollregion = (0,0,20,1000))
        vbar = Scrollbar(self.f1, orient = VERTICAL)
        vbar.pack(side = RIGHT, fill = Y)
        vbar.config(command = canvas.yview)
        canvas.config(width = 900, height = 600)
        canvas.config(yscrollcommand = vbar.set)
        canvas.pack(side = LEFT, expand = True, fill = BOTH)
        print(canvas.bbox('all'))
        vbar = Scrollbar(self.f1, orient ="horizontal") 
        vbar.pack(side = BOTTOM, fill = X)
        vbar.config(command = canvas.xview)
        canvas.configure(xscrollcommand = vbar.set)
        canvas.pack(side = LEFT, expand = True, fill = BOTH)
        
        leftCanvas = Canvas(leftFrame , width=800 , height=580 )
        leftCanvas.place(x = 0 , y = 0 , width=800 , height=580)
        scrollbar_l = ttk.Scrollbar(leftFrame, orient="horizontal" , command = leftCanvas.xview)
        scrollbar_l.pack(side = BOTTOM , fill = "x")
        leftCanvas.configure(xscrollcommand=scrollbar_l.set)

        leftCanvas = Canvas(self.f2)
        leftCanvas.place(x = 0 , y = 0)
        scrollbar_l = ttk.Scrollbar(leftFrame, orient="horizontal" , command = leftCanvas.xview)
        scrollbar_l.pack(side = BOTTOM , fill = "x")
        leftCanvas.configure(xscrollcommand=scrollbar_l.set)
       
        self.leftFrame = tk.Frame(self.master , highlightbackground="black" , highlightthickness= 3)
        self.leftFrame.place(x = 0 , y = 0 , width=800 , height=580)
        
        # Scrollbar
        canvas = Canvas(self.topframe, bg = "white", width = 300, height = 300, scrollregion = (0,0,20,1000))
        vbar = Scrollbar(self.topframe, orient = VERTICAL)
        vbar.pack(side = RIGHT, fill = Y)
        vbar.config(command = canvas.yview)
        canvas.config(width = 900, height = 600)
        canvas.config(yscrollcommand = vbar.set)
        canvas.pack(side = LEFT, expand = True, fill = BOTH)
    """
        
    def filtreCommande(self):
        self.user['text']=self.ma_var.get()
        
        
root = tk.Tk()
app = Window(root)
root.mainloop()
