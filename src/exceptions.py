"""Exceptions Finder"""


class AnalyseurError(Exception):
    """analyse les erreurs"""


class TexteVideError(AnalyseurError):
    """exception contenu vide"""

    def __init__(self, titre):
        self.titre = titre
        super().__init__(f"Ce texte n'a pas de contenu : {titre}")


class FormatInconnuError(AnalyseurError):
    """check format du doc"""

    def __init__(self, titre):
        self.titre = titre
        super().__init__(f"Ce format est inconnu : {titre}")
