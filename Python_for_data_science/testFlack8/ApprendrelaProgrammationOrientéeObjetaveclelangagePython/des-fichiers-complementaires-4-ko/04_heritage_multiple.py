class Mur:
    def __init__(self, orientation):
        self.orientation = orientation
        self.fenetres = []

class Fenetre:
    def __init__(self, mur, surface, protection):
        self.mur = mur
        self.surface = surface
        self.mur.fenetres.append(self)
        if protection is None:
            raise Exception("Protection obligatoire")
        self.protection = protection

class Maison:
    def __init__(self, murs):
        self.murs = murs

    def surface_vitree(self):
        surface = 0
        for mur in self.murs:
            for fenetre in mur.fenetres:
                surface += fenetre.surface
        return surface

mur_nord = Mur("NORD")
mur_ouest = Mur("OUEST")
mur_sud = Mur("SUD")
mur_est = Mur("EST")
fenetre_nord = Fenetre(mur_nord, 0.5, "volet")
fenetre_ouest = Fenetre(mur_ouest, 1, "volet")
fenetre_sud = Fenetre(mur_sud, 2, "store vénitien")
fenetre_est = Fenetre(mur_est, 1, "volet")
maison = Maison([mur_nord, mur_ouest, mur_sud, mur_est])
print(maison.surface_vitree())
# >>> 4.5

class MurRideau(Mur, Fenetre):
    def __init__(self, orientation, surface):
        Mur.__init__(self, orientation)
        Fenetre.__init__(self, self, surface, "Aucune")

mur_rideau = MurRideau("SUD", 10)
maison.murs[2] = mur_rideau
print(maison.surface_vitree())
# >>> 12.5
