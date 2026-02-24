class Texte :
    def __init__(self, titre: str, auteur: str, contenu: str, annee: int):
        self.titre = titre
        self.auteur = auteur
        self.contenu = contenu
        self.annee = annee
    def nombre_mots(self):
        return sum(len(self.contenu.split()))