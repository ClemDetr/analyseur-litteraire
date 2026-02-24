class Texte :
    def __init__(self, titre: str, auteur: str, contenu: str, annee: int):
        self._titre = titre
        self.auteur = auteur
        self._contenu = contenu
        self.annee = annee
    @property
    def titre(self) -> str:
        return self._titre
    @titre.setter
    def titre(self, nouveau: str) -> None:
        if not nouveau.strip():
            raise ValueError("Le titre ne peut pas etre vide")
        self._titre = nouveau.strip()
    def nombre_mots(self) -> int:
        return len(self._contenu.split())
    def mots_uniques(self) -> set[str]:
        self.mots_uniques = set[]
        for mot in self._contenu.split :
            if mot not in self.mots_uniques:
                self.mots_uniques.add(mot)