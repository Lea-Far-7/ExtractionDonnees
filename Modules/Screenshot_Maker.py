from tkinter import messagebox

from Modules.FileManager import FileManager
import mss
import mss.tools

class Screenshot_Maker:

    def __init__(self, repertoire = "..\\Exports"):
        self.repertoire = repertoire
        self.fileManager = FileManager()
        self.__creer_repertoire()

    def __creer_repertoire(self):
        self.fileManager.creer_repertoire(self.repertoire)

    def capture_ecran(self, bbox):
        fichier ="vide"
        try:
            # Capture de la zone définit par le bbox
            with mss.mss() as sct:
                screenshot = sct.grab(bbox)

            # Création du chemin avec le nom de la capture
            fichier = self.fileManager.creer_chemin_fichier(self.repertoire)

            # Enregistrement de la capture d'écran
            mss.tools.to_png(screenshot.rgb, screenshot.size, output=fichier)

            # Affichage d'une confirmation du screenshot
            messagebox.showinfo("Information Screenshot", "La capture d'écran a bien été effectuée.\n"
                                                                    "Vous la trouverez dans le dossier Exports\Screenshots")
        except Exception as e:
            messagebox.showinfo("Erreur", "Une erreur s'est produite lors de la capture d'écran :\n" + str(e) + fichier)


    def get_bbox(self, widget):
        return {
            'left' : widget.winfo_rootx(),
            'top' : widget.winfo_rooty(),
            'width' : widget.winfo_width(),
            'height' : widget.winfo_height()
        }