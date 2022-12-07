import tkinter as tk
from tkinter import *
from tkinter.filedialog import *


class Window:
    def __init__(self, master):
        self.master = master
        self.master.geometry("900x900")
        self.master.title("WirePoulpe")
        self.master.config(bg = '#F0F0E6')
        self.master.resizable(height=False , width = False)

        # Créer l'image de fond sur notre fenetre
        self.image = tk.PhotoImage(file = "./DALL·E 2022-12-02 13.12.31 - monster octopus.png")
        self.limg = Label(self.master, i = self.image)
        self.limg.place(x = 0, y = 0, relwidth = 1, relheight = 1)
        self.master.pack()
        self.showWidgets()

    def showWidgets(self):
        # Titre page principale 
        self.title = Label(self.master, text = "Bienvenue sur WirePoulpe", font = ('Courier', 20), width = 50, height = 5, bg = '#2C514C', fg = 'black')
        self.title.pack(pady = 50)

        self.frame = tk.Frame(self.master)
        self.explorer = self.createButton("Import", lambda: self.openFile())
        self.quit = self.createButton("Quit", lambda : self.closeWindow())

        self.explorer.pack()
        self.quit.pack()
        self.frame.pack()

    def createButton(self, text, command):
        butt = tk.Button(self.master, text = text, font = ('Courier', 15), width = 10, height = 2, bg = '#2C514C', command = command)
        butt.place(x = 0, y = 0, relwidth = 1, relheight = 1)
        return butt

    # Ouvrir un fichier
    def openFile(self):
        self.file = tk.filedialog.askopenfilename(initialdir = "~/", title = "Select a file", filetypes = [("Text files", "*.txt*")])
        self.newWindow(Win2)
        

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

class Win2(Window):
    def __init__(self, master):
        super().__init__(master)
        self.master.title("Visualisateur du trafic réseau")
    
    def showWidgets(self):
        self.frame = tk.Frame(self.master)
        self.frame.pack(fill = BOTH)
        self.frame.grid_columnconfigure(0, weight = 1)
        self.frame.grid_columnconfigure(1, weight = 1)
        self.frame.grid_rowconfigure(0, weight = 1)

        frame1 = Frame(self.frame, bg = "white")
        frame1.grid(row = 0, column = 0, sticky = "nesw")
        frame2 = Frame(self.frame, bg = "red")
        frame2.grid(row = 0, column = 1, sticky = "nesw")
        
root = tk.Tk()
app = Window(root)
root.mainloop()
