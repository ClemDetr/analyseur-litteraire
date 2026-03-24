"""class Texte"""

import re
from collections import Counter

from exceptions import TexteVideError


class Texte:  # noqa: PLW1641
    """objet Texte"""

    def __init__(self, titre: str, auteur: str, contenu: str, annee: int):
        self._titre = titre
        self.auteur = auteur
        try:
            if contenu:
                self.contenu = contenu
                self.mots = re.sub(r"\s+", " ", self.contenu).split()
            else:
                raise TexteVideError(self.titre)  # noqa: TRY301
        except TexteVideError as e:
            print(f"Error : {e}")

        self.annee = annee

    def __str__(self) -> str:
        return f"{self.titre} ({self.auteur}, {self.annee})"

    def __repr__(self) -> str:
        return (
            f"Texte(titre = {self.titre!r})"
            f"auteur = {self.auteur!r}, année = {self.annee}"
        )

    def __eq__(self, other) -> bool:
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
            e = "Le titre ne peut pas etre vide"
            raise ValueError(e)
        self._titre = nouveau.strip()

    def nombre_mots(self) -> int:
        """compte mots"""
        return len(self.contenu.lower().replace("\n", " ").split())

    def nombre_phrases(self) -> int:
        """compte phrases"""
        return len(self.contenu.lower().replace("\n", " ").split("."))

    def mots_uniques(self) -> set[str]:
        """index mots uniques"""
        mots_uniques: set[str] = set()
        counter = Counter(self.contenu.lower().replace("\n", " ").split())
        for mot, occurences in counter.items():
            if occurences == 1:
                mots_uniques.add(mot)
        return mots_uniques

    def frequences(self) -> dict[str, int]:
        """compteur fréquence"""
        return Counter(self.contenu.lower().replace("\n", " ").split())

    def resume(self) -> str:
        """resume texte"""
        result = " ".join(self.mots[:50]) + " ..."
        print(result)
        return result
