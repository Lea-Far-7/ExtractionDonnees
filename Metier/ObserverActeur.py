import abc # pour classe abstraite

class ObserverActeur(abc.ABC):

    @abc.abstractmethod
    def update(self):
        pass
