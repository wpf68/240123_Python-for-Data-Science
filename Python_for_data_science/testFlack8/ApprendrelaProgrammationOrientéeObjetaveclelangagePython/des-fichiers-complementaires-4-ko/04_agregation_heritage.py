# Classe "interface" représentant les caractéristiques d'une surface
# vitrée. Elle n'a pour seul attribut que 'surface', mais on pourrait
# imaginer d'autres propriétés de surfaces vitrée comme le ratio de
# transparence, les couches de verres qui la composent, etc.
class Vitre:
    def __init__(self, surface):
        self.__surface = surface

    def surface(self):
        return self.__surface

class Mur:
    def __init__(self, orientation):
        self.__orientation = orientation
        self.__fenetres = []

    def fenetres(self):
        return self.__fenetres

    def surface_vitree(self):
        surface = 0
        for fenetre in self.fenetres():
            surface += fenetre.surface()
        return surface

class Fenetre:
    def __init__(self, mur, surface, protection):
        self.__mur = mur
        # 'Fenetre' délègue la gestion de la surface vitrée à
        # 'Vitre', qui est privée
        self.__vitre = Vitre(surface)
        self.__mur.fenetres().append(self)
        if protection is None:
            raise Exception("Protection obligatoire")
        self.__protection = protection

    # Encapsulation de la surface dans un accesseur, afin de conserver
    # privé l'attribut SurfaceVitrée.
    def surface(self):
        return self.__vitre.surface()

class Maison:
    def __init__(self, murs):
        self.__murs = murs

    def murs(self):
        return self.__murs

    def surface_vitre(self):
        surface = 0
        for mur in self.murs():
            surface += mur.surface_vitree()
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

# Un MurRideau reste un Mur
class MurRideau(Mur):
    def __init__(self, orientation, surface):
        Mur.__init__(self, orientation)
        # Plus d'utilisation litigieuse de 'self' en tant que son
        # propre mur.
        self.__vitre = Vitre(surface)

    def surface_vitree(self):
        return self.__vitre.surface()

mur_rideau = MurRideau("SUD", 10)
maison = Maison([mur_nord, mur_ouest, mur_rideau, mur_est])
print(maison.surface_vitree())
