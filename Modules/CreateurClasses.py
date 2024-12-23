from abc import ABC, abstractmethod

class CreateurClass(ABC):

    @abstractmethod
    def creer(self, fichier: list):
        pass