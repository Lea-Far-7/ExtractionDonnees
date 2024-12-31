import customtkinter

from Metier.client import Client


class AffichageClient:
    instances = []

    def __init__(self, masterwindow, marker):
        self.__class__.instances.append(self)
        self.masterwindow = masterwindow
        self.marker = marker

        self.window = customtkinter.CTkToplevel()
        self.window.withdraw()
        self.window.overrideredirect(True)
        self.ajoutDonnees()
        self.window.geometry(
            "+%d+%d" % (self.masterwindow.winfo_rootx() + self.masterwindow.winfo_width() - self.window.winfo_width(),
                        self.masterwindow.winfo_rooty() + self.masterwindow.winfo_height() - self.window.winfo_height()))

    @classmethod
    def hide(cls,cls2):
        for i in cls.instances:
            i.window.withdraw()
        for i in cls2.instances:
            i.window.withdraw()

    def update_popup_position(self, event):
        self.window.geometry(
            "+%d+%d" % (self.masterwindow.winfo_rootx() + self.masterwindow.winfo_width() - self.window.winfo_width(),
                        self.masterwindow.winfo_rooty() + self.masterwindow.winfo_height() - self.window.winfo_height()))
        self.window.lift()

    def ajoutDonnees(self):
        client = self.marker.acteur
        label = customtkinter.CTkLabel(self.window, text=client.__str__(), fg_color="transparent")
        label.grid(row=0, column=0, columnspan=1, padx=20, pady=10)

    def afficher(self):
        self.window.geometry(
            "+%d+%d" % (self.masterwindow.winfo_rootx() + self.masterwindow.winfo_width() - self.window.winfo_width(),
                        self.masterwindow.winfo_rooty() + self.masterwindow.winfo_height() - self.window.winfo_height()))
        self.window.lift()
        self.masterwindow.bind('<Configure>', self.update_popup_position)
        self.window.deiconify()


        #TODO : Bien mettre la fenetre, bien organiser les données, problèmes dans l'int princ à cause de popupaff (changer la suppression des marqueurs)



