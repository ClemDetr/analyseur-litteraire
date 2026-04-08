import string
import unicodedata

from texte import Texte


def en_minuscules(texte: str) -> str:
    return texte.lower()


def sans_ponctuation(texte: str) -> str:
    return texte.translate(str.maketrans("", "", string.punctuation))


def sans_accents(texte: str) -> str:
    nfkd = unicodedata.normalize("NFD", texte)
    return "".join(c for c in nfkd if unicodedata.category(c) != "Mn")


def nettoyer(texte: Texte) -> str:
    """Pipeline de nettoyage compose."""
    return sans_accents(sans_ponctuation(en_minuscules(texte.contenu)))


# nettoyer("L'Ete, a Paris!") -> "lete a paris"
