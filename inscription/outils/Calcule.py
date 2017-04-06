import decimal
from datetime import datetime
from locale import str

from builtins import range

from inscription.models.Candidat import Candidat
from inscription.models.models import Age, DiplomeAnnee


class AnneeSemestre:

    @staticmethod
    def getAnnee():
        year = datetime.today().year  # .now() # datetime.date._year
        List = []
        for i in range(1, 5, 1):
            List.append((str(year - 1) + "-" + str(year), str(year - 1) + "-" + str(year)))
            year -= 1
        return List

    #le nombre de redoublement de candidat, utilisé dans la model candidat
    Nbr_Redouble = (
        (0, 'Sans redoublement'),
        (1, 'Un redoublement'),
        (2, 'Deux redoublements ou plus...'),
    )


class CalculeCandidat:
    #candidat_ = Candidat

    @staticmethod
    def preselection_note(diplome, valeur):
        return decimal.Decimal(0.25) * diplome.moyenne_1_an + \
            decimal.Decimal(0.25) * diplome.moyenne_2_an + \
            decimal.Decimal(0.15) * valeur + \
            decimal.Decimal(0.15) * 20 + \
            decimal.Decimal(0.20 * 20)

    @staticmethod
    def validation_diplome(nbrRedouble):
        list_redouble = DiplomeAnnee.objects.order_by('-points').all()
        for nbr in list_redouble:
            if nbrRedouble >= nbr.max_annee:
                return  nbr.points

    @staticmethod
    def age_note(age):
        list_age = Age.objects.order_by('-points').all()
        for _age in list_age:
            if age >= _age.max_annee:
                return  _age.points

    @staticmethod
    def moyenne_1(diplome):
        return (diplome.s1_note + diplome.s2_note) / 2

    @staticmethod
    def moyenne_2(diplome):
        return  (diplome.s3_note + diplome.s4_note) / 2

    @staticmethod
    def moyenne(diplome):
        return (diplome.moyenne_1_an + diplome.moyenne_2_an) / 2