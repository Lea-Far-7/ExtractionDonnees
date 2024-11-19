from tkinter import *
from tkinter import filedialog
from  tkinter import ttk
import customtkinter


class PopUp(customtkinter.CTk):
    def __init__(self, masterwindow):
        super().__init__()

        self.masterwindow = masterwindow

        # Création d'une nouvelle fenêtre
        self.window = customtkinter.CTkToplevel()


        #Focus sur cette nouvelle fenêtre (cela désactive la fenêtre principale)
        self.window.grab_set()

        # Suppression de la topbar (Titre, Minimiser, Maximiser, Fermer)
        self.window.overrideredirect(True)

        # Placement de la fenêtre à des coordonnées relatives à la fenêtre principale
        if (self.masterwindow == None) :
            self.window.geometry("+%d+%d" % (self.window.masterwindow.winfo_rootx()+self.window.masterwindow.winfo_width()/5, self.window.masterwindow.winfo_rooty()+self.window.masterwindow.winfo_height()/4))

