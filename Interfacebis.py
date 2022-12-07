#import all components from the tkinter library
from tkinter import *
from tkinter import ttk
import tkinter as tk

#import filedialog module
from tkinter import filedialog
from tkinter.filedialog import asksaveasfile
import time

'''
class window:
	def __init(self, master):
		self.master = master
		self.master.geometry("1080x720")
		self.master.title("WirePoulpe")
		self.master.config()
		self.showWidgets(background = '#F0F0E6')

	def showWidgets(self):
		self.frame = tk.Frame(self.master)
		self.explorer
'''
# Création de la fenetre graphique
window = Tk()
window.title("WirePoulpe")
window.geometry("1080x720")
window.config(background = '#F0F0E6')

# Création de la deuxième fenetre
win = False

# Fonction pour enregistrer les fichiers
def saveFile():
	file = asksaveasfile(mode = 'w', defaultextension = ".txt")
	if file is None : 
		return
	text = str(text.get(1.0, END))		
	file.write(text)
	file.close()

# Ouverture du fichier
def openFile():
	global win
	window.file = filedialog.askopenfilename(initialdir = "~/", title = "Select a file", filetypes = (("Text files", "*.txt*"), ("all files", "*.*")))
	win.pack(fill = 'both', expand = True)


def uploadFile():
	pb = ttk.Progressbar(window, orient = HORIZONTAL, length = 300, mode = 'determine')
	pb.place()
	for i in range(5):
		window.update_idletasks()
		pb['value'] += 20
		time.sleep(1)
	pb.destroy()
	Label(window, text = "Fichier importé", fg = "black").place()

'''
# Récupère le chemin du fichier
def chercher_chemin():
	window = tk.Tk()
	window.withdraw()
	chemin = filedialog.askopenfilename()
	return chemin

class newWindow():
    file = chercher_chemin()
	# Ouverture d'une autre fenetre
    win = Toplevel(window)
    win.title("Trafic réseau")
    win.geometry("1080x720")
    Label(win, "Nouvelle fenetre").pack()
'''

# Créer l'image de fond sur notre fenetre
image = tk.PhotoImage(file = "./DALL·E 2022-12-02 13.12.31 - monster octopus.png")
limg = Label(window, i = image)
limg.place(x = 0, y = 0, relwidth = 1, relheight = 1)

# Titre page principale
title = Label(window, text = "Bienvenue dans WirePoulpe", font = ('Courier', 20), width = 50, height = 5, bg = '#C1C1FF', fg = 'black')

# Ajout des boutons
bouton_explore = Button(window, text = "Import", font = ('Courier', 15), width = 10, height = 2, bg = '#9797FF', command = openFile)
bouton_exit = Button(window, text = "Exit", font = ('Courier', 15), width = 10, height = 2, bg = '#9797FF', command = exit)

title.pack(pady = 50)
bouton_explore.pack(padx = 100, pady = 100)
bouton_exit.pack(padx = 100, pady = 20)

# Création de la frame 
win = Toplevel(window, bg = '#F0F0E6')

# Sélection du checkbutton
show_all = tk.BooleanVar()
show_all.set(True)

# Création du menu
menu_bar = Menu(window)
			
menu_file = Menu(menu_bar, tearoff = 0)
#menu_file.add_command(label = "Open", underline = 0, accelerator = "CTRL+O", command = openFile)
menu_file.add_command(label ="Save", underline = 0, accelerator = "CTRL+S", command = saveFile)
menu_file.add_separator()
menu_file.add_command(label = "Exit", command = exit)
menu_bar.add_cascade(label = "File", menu = menu_file)

menu_view = Menu(menu_bar, tearoff = 1)
menu_view.add_checkbutton(label = "Filtre", onvalue = 1, offvalue = 0, variable = show_all)
menu_bar.add_cascade(label = "View", menu = menu_view)

#window.bind_all("<Control-n>", lambda x : newFile())
#window.bind_all("<Control-o>", lambda x : openFile())
window.bind_all("<Control-s>", lambda x : saveFile())

window.config(menu = menu_bar)
'''
# Panels
panel_1 = PanedWindow(bd = 4, relief = "raised", bg = "black")
panel_1.pack(fill = BOTH, expand = 1)

left_label = Label(panel_1, text = "Traffic")
panel_1.add(left_label)

panel_2 = PanedWindow(panel_1, orient = VERTICAL, bd = 4, relief = "raised", bg = "#F0F0E6")
panel_1.add(panel_2)

top = Label(panel_2, text = "Comments")
panel_2.add(top)
		
# Scrollbar
my_scrollbar = Scrollbar(win, orient = VERTICAL)
my_scrollbar.pack(side = RIGHT, fill = Y)

my_tree = ttk.Treeview(win, yscrollcommand = my_scrollbar.set, selectmode = "browse")
my_tree.pack()
#my_scrollbar.config(command = my_tree.yview)
'''

# Affichage de la fenetre
window.mainloop()


	
