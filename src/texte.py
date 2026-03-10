"""class Texte"""
from collections import Counter
import re

class Texte :
    """objet Texte"""

    def __init__(self, titre: str, auteur: str, contenu: str, annee: int):
        self._titre = titre
        self.auteur = auteur
        self.contenu = contenu
        self.mots = re.sub(r"\s+"," ",self.contenu).split()
        self.annee = annee

    def __str__ (self) -> str:
        return f"{self.titre} ({self.auteur}, {self.annee})"

    def __repr__(self) -> str:
        return (f"Texte(titre = {self.titre!r})"
                f"auteur = {self.auteur!r}, année = {self.annee}")

    def __eq__(self, other) ->bool:
        if not isinstance(other, Texte):
            return False
        return self.titre == other.titre and self.auteur == other.auteur

    def __lt__(self, other):
        if not isinstance(other, Texte):
            return False
        return self.annee < other.annee

    @property
    def titre(self) -> str:
        """appel titre"""
        return self._titre

    @titre.setter
    def titre(self, nouveau: str) -> None:
        if not nouveau.strip():
            raise ValueError("Le titre ne peut pas etre vide")
        self._titre = nouveau.strip()

    def nombre_mots(self) -> int:
        """compte mots"""
        return len(self.contenu.lower().replace("\n"," ").split())

    def mots_uniques(self) -> set[str]:
        """index mots uniques"""
        mots_uniques: set[str] = set()
        counter = Counter(self.contenu.lower().replace("\n"," ").split())
        for mot, occurences in counter.items():
            if occurences == 1:
                mots_uniques.add(mot)
        return mots_uniques

    def frequences(self) -> dict[str, int]:
        """compteur fréquence"""
        frequence = Counter(self.contenu.lower().replace("\n"," ").split())
        return frequence

    def resume(self) -> str :
        """resume texte"""
        result = " ".join(self.mots[:50]) + " ..."
        print(result)
        return result




if __name__ == "__main__":



    texte1 = Texte("Droit de la femme", "eMILE", """A LA REINE.


    MADAME,

    Peu faite au langage que l'on tient aux Rois, je n'emploierai point
    l'adulation des Courtisans pour vous faire hommage de cette singulière
    production. Mon but, Madame, est de vous parler franchement; je n'ai
    pas attendu, pour m'exprimer ainsi, l'époque de la Liberté: je me
    suis montrée avec la même énergie dans un temps où l'aveuglement des
    Despotes punissait une si noble audace.

    Lorsque tout l'Empire vous accusait et vous rendait responsable de ses
    calamités, moi seule, dans un temps de trouble et d'orage, j'ai eu la
    force de prendre votre défense. Je n'ai jamais pu me persuader qu'une
    Princesse, élevée au sein des grandeurs, eût tous les vices de la
    bassesse.

    Oui, Madame, lorsque j'ai vu le glaive levé sur vous, j'ai jeté mes
    observations entre ce glaive et la victime; mais aujourd'hui que je
    vois qu'on observe de près la foule de mutins soudoyée, & qu'elle est
    retenue par la crainte des loix, je vous dirai, Madame, ce que je ne
    vous aurois pas dit alors.
    """, 1200)
    texte2 = Texte("asdfghjklllllll","Maurice Chevalier", "rien.", 0)

    liste = [texte1, texte2]
    for l in sorted(liste):
        print(l)

    texte1.resume()
