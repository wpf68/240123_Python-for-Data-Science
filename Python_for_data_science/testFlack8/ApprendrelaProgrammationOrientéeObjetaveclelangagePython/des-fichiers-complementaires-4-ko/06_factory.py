from enum import Enum
from abc import ABCMeta, abstractmethod

class Nature(Enum):
    ALIMENTAIRE = 1
    SERVICE = 2

class Produit:
    def __init__(self, nature):
        self.nature = nature
        self.prix_ht = 100

class FactureProduit(metaclass=ABCMeta):
    def __init__(self, prix_ht):
        self.prix_ht = prix_ht

    @abstractmethod
    def facturer(self):
        pass

class FactureAlimentaire(FactureProduit):
    def facturer(self):
        return self.prix_ht * 1.055

class FactureService(FactureProduit):
    def facturer(self):
        return self.prix_ht * 1.2

class FactoryFacture:
    def creer(produit):
        prix_ht = produit.prix_ht
        selection_factures = { Nature.ALIMENTAIRE: FactureAlimentaire(prix_ht),
                               Nature.SERVICE: FactureService(prix_ht) }
        return selection_factures.get(produit.nature, "Nature inconnue")

produit = Produit(Nature.ALIMENTAIRE)
prix_ttc = FactoryFacture.creer(produit).facturer()
print(prix_ttc)
# 105.5

produit = Produit(Nature.SERVICE)
prix_ttc = FactoryFacture.creer(produit).facturer()
print(prix_ttc)
# 120
