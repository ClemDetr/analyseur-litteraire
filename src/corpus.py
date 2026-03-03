"""
Corpus est un conteneur de texte
"""
from texte import Texte

class Corpus:
    """conteneur de classe"""

    def __init__(self, name: str):
        self.name = name
        self._textes = list[Texte]

    def ajouter_texte(self, texte: Texte) ->None:
        """ajoute un texte"""
        self._textes.append(texte)

    def total_mots(self) -> int:
        """renvoi nombre mots"""
        return sum(texte.nombre_mots() for texte in self._textes)

    def rechercher_mot(self, mot: str):
        """recherche mot dans texte du corpus"""
        mot_lower = mot.lower()
        liste_texte = list()
        for texte in self._textes :
            if mot_lower in texte.contenu_split:
                liste_texte.append(texte.titre())
