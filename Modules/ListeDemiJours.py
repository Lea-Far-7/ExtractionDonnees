from Metier.demiJour import DemiJour

class ListeDemiJours(DemiJour):

    listeDJ = [DemiJour(x) for x in range(0,10)]

    @classmethod
    def getlisteDJ(cls)->list:
        return ListeDemiJours.listeDJ

    @classmethod
    def getDJ(cls, index:int)->DemiJour:
        return ListeDemiJours.listeDJ[index]