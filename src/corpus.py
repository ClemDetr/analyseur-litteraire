"""
Corpus est un conteneur de texte
"""
from texte import Texte

class Corpus:

    def __init__(self, name: str):
        self.name = name
        self._textes = list[Texte] = []

    def ajouter_texte(self, texte: Texte) ->None:
        self._textes.append(texte)

    def total_mots(self) -> int:
        return sum(texte.nombre_mots() for texte in self._textes)

    def rechercher_mot(self, mot: str):
        liste_texte = list()
        for texte in self._textes :
            if mot in texte._contenu_split:
                liste_texte.append(texte.titre())
