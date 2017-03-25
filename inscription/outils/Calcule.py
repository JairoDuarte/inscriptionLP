from inscription.models.Candidat import Candidat


class CalculeCandidat:
    #candidat_ = Candidat

    def __init__(self, candidat):
        self.candidat_ = candidat

    def calculer(self):
        self.moyenne_1()
        self.moyenne_2()
        self.moyenne()
        self.preselection_note()

    def preselection_note(self):
        self.candidat_.preselection_note = 0.25 * self.candidat_.diplome.moyenne_1_an + \
            0.25 * self.candidat_.diplome.moyenne_2_an + \
            0.15 * self.candidat_.diplomebac.mention.valeur + \
            0.15 * 20 + \
            0.20 * 20

    def moyenne_1(self):
        self.candidat_.diplome.moyenne_1_an = (self.candidat_.diplome.s1_note + self.candidat_.diplome.s2_note) / 2

    def moyenne_2(self):
        self.candidat_.diplome.moyenne_2_an = (self.candidat_.diplome.s3_note + self.candidat_.diplome.s4_note) / 2

    def moyenne(self):
        self.candidat_.diplome.moyenneDiplome = \
            (self.candidat_.diplome.moyenne_1_an() + self.candidat_.diplome.moyenne_2_an()) / 2