"""
Corpus est un conteneur de texte
"""
from collections.abc import Iterator
from texte import Texte

class Corpus:
    """conteneur de classe"""

    def __init__(self, name: str):
        self.name = name
        self._textes : list[Texte] = []

    def __len__(self):
        return len(self._textes)

    def __getitem__(self, index):
        return self._textes[index]

    def __iter__(self) -> Iterator[Texte]:
        return iter(self._textes)

    def __contains__(self, titre: str) -> bool:
        return any(texte.titre == titre for texte in self._textes)

    def __add__(self, other:"Corpus"):
        nouveau = Corpus(f"{self.name} + {other.name}")
        for texte in self._textes:
            nouveau.ajouter_texte(texte)
        for texte in other._textes:
            nouveau.ajouter_texte(texte)
        return nouveau


    def ajouter_texte(self, texte: Texte) ->None:
        """ajoute un texte"""
        self._textes.append(texte)

    def total_mots(self) -> int:
        """renvoi nombre mots"""
        return sum(texte.nombre_mots() for texte in self._textes)

    def rechercher_mot(self, mot: str):
        """recherche mot dans texte du corpus"""
        mot_lower = mot.lower()
        for texte in self._textes :
            if mot_lower in texte.contenu.split():
                print(texte.titre)


if __name__ == "__main__":

    roman = Corpus("Romans")

    roman.ajouter_texte(Texte("Droit de la femme", "eMILE", """A LA REINE.


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
    """, 1200))
    roman.ajouter_texte(Texte("asdfghjklllllll","Maurice Chevalier", "rien.", 0))


    for t in roman:
        print(f"-{t.titre}")


    poesie = Corpus("Poésie")
    poesie.ajouter_texte(Texte("Fleurs du Mal", "Baudelaire", "Aïe, ça pique", 2005))
    poesie.ajouter_texte(Texte("Introduction à la poésie", "Les Nuls", "ça rime, c'est bien", 1989))

    for p in poesie:
        print(f"-{p.titre}")
    for p in poesie:
        print(p)

    tout = roman + poesie
    print(len(tout))
    print(tout.name)
